import os
import shutil
import re
import datetime

import httpx
from git import Repo
from loguru import logger

class DOWNLOADER:
    def __init__(self):
        self.client = httpx.Client(http2=True)

    def down_direct(self, url: str, path: str, fileName: str):
        isDownload = False
        try:
            fileName = path + '/' + fileName
            logger.info("download %s[%s]..."%(fileName, url))
            if not os.path.exists(fileName):
                response = self.client.get(url)
                response.raise_for_status()
                with open(fileName, 'wb') as f:
                    f.write(response.content)
            isDownload = True
        except Exception as e:
            logger.exception("%s" % (e))
        finally:
            return isDownload, fileName

    def down_git_release(self, repo: str, path: str, pattern: str, proxy: str=None):
        isDownload = False
        try:
            logger.info("download %s[%s]..."%(pattern, repo))
            # 获取 release 信息
            url = "https://api.github.com/repos/" + repo + "/releases" # 不使用 /latest 接口，部分项目存在多重 release ，需所有 release 信息
            response = self.client.get(url)
            response.raise_for_status()
            releaselist = response.json()
            for release in releaselist:
                tag = release.get("tag_name", None)
                assets = release.get("assets", [])
                if tag is None or len(assets) < 1:
                    raise Exception("no release tag")
                #message = release.get("body", "")
                #logger.info(message)
                # 下载 release 资源
                for asset in assets:
                    fileName = asset.get("name", None)
                    url = asset.get("browser_download_url", None)
                    if proxy and url:
                        url = proxy + url
                    fileDigest = asset.get("digest", "")
                    fileDate = datetime.datetime.strptime(asset.get("updated_at", ""), "%Y-%m-%dT%H:%M:%SZ")
                    fileDate = datetime.datetime.strftime(fileDate, '%Y%m%d')
                    if re.match(pattern, fileName) and url is not None:
                        fileName = path + '/' + fileName
                        if not os.path.exists(fileName): # 不重复下载
                            response = self.client.get(url)
                            response.raise_for_status()
                            with open(fileName, 'wb') as f:
                                f.write(response.content)
                        isDownload = True
                        break
                if isDownload:
                    break
        except Exception as e:
            logger.exception("%s" % (e))
        finally:
            if isDownload:
                return isDownload, fileName, fileDigest, fileDate, tag
            else:
                return isDownload, None, None, None, None

    def down_git_repository(self, repo: str, path: str, branch: str=None, proxy: str=None):
        isDownload = False
        try:
            fileName = path + '/' + repo.split('/')[-1]
            logger.info("download %s[%s]..."%(fileName, repo))
            if os.path.exists(fileName):
                shutil.rmtree(fileName)
            if proxy:
                repo = proxy + repo
            repository = Repo.clone_from(repo, fileName)
            if branch:
                repository.git.checkout(branch)
            date = repository.commit().committed_datetime
            commint_date = datetime.datetime.strftime(date, '%Y%m%d')
            commint_id = repository.head.commit.hexsha
            #commint_message = repository.commit().message
            #logger.info(commint_message)
            isDownload = True
        except Exception as e:
            logger.exception("%s" % (e))
        finally:
            if isDownload:
                return isDownload, fileName, commint_id, commint_date
            else:
                return isDownload, None, None, None