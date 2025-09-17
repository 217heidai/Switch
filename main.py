import os
import shutil
import zipfile
from typing import Dict,Any,List,Set

from loguru import logger

from downloader import DOWNLOADER
from utils import UTIL, ITEM
from readme import README


def Download(path_default: str, path_download: str, path_dst: str, itemList: List[ITEM]):
    isSuccess = False
    isUpdate = False
    try:
        # 复制默认文件
        if os.path.exists(path_dst):
            shutil.rmtree(path_dst)
        shutil.copytree(path_default, path_dst)

        # 下载资源
        os.makedirs(path_download, exist_ok=True)
        downloader = DOWNLOADER()
        for item in itemList:
            # 下载资源
            item.isDownload, item.fileName, fileDigest, ifileDate, releaseTag = downloader.down_git_release(item.repo, path_download, item.pattern, proxy=item.proxy)
            
            # 处理文件
            if item.isDownload:
                if ifileDate != item.fileDate or releaseTag != item.releaseTag:
                    item.fileDate = ifileDate
                    item.releaseTag = releaseTag
                    isUpdate = True
                item.process(path_dst)
            else:
                raise Exception("download failed")

        # 重新替换被 atmosphere 覆盖的默认文件
        UTIL.copyFile("%s/atmosphere/config_templates/exosphere.ini"%(path_default), "%s/atmosphere/config_templates/exosphere.ini"%(path_dst))
        UTIL.copyFile("%s/atmosphere/config_templates/override_config.ini"%(path_default), "%s/atmosphere/config_templates/override_config.ini"%(path_dst))
        UTIL.copyFile("%s/atmosphere/config_templates/stratosphere.ini"%(path_default), "%s/atmosphere/config_templates/stratosphere.ini"%(path_dst))
        UTIL.copyFile("%s/atmosphere/config_templates/system_settings.ini"%(path_default), "%s/atmosphere/config_templates/system_settings.ini"%(path_dst))
        UTIL.copyFile("%s/bootloader/res/icon_switch.bmp"%(path_default), "%s/bootloader/res/icon_switch.bmp"%(path_dst))
        if os.path.exists("%s/bootloader/res/icon_payload.bmp"%(path_dst)):
            os.remove("%s/bootloader/res/icon_payload.bmp"%(path_dst))

        isSuccess = True
    except Exception as e:
        logger.exception("%s" % (e))
    finally:
        if isSuccess:
            return isUpdate, itemList
        else:
            return False, itemList

def Entry():
    pwd = os.getcwd()
    path_default  = pwd + "/default"
    path_download = pwd + "/build/download"
    path_dst      = pwd + "/build/switch_sdcard"
    versionFile   = pwd + "/build/version.md"

    readme = README(pwd + "/README.md")
    itemList = readme.getItems(path_dst)
    
    # 资源下载
    logger.info("start download...")
    isUpdate, itemList = Download(path_default, path_download, path_dst, itemList)

    if isUpdate:
        # 打包
        logger.info("start pack...")
        if os.path.exists(path_dst + '.zip'):
            os.remove(path_dst + '.zip')
        with zipfile.ZipFile(path_dst + '.zip', 'w') as zipObj:
            for root, dirs, files in os.walk(path_dst):
                path = root.replace(path_dst, "")
                for file in files:
                    zipObj.write(os.path.join(root, file), os.path.join(path, file))
    
        # 更新readme
        logger.info("generate version file...")
        readme.generate(itemList, path_dst, versionFile)

    # 删除多余文件
    if os.path.exists(path_download):
        shutil.rmtree(path_download)
    if os.path.exists(path_dst):
        shutil.rmtree(path_dst)


if __name__ == "__main__":
    Entry()
