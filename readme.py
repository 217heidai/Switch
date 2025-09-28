import os
import re
from typing import Dict,Any,List,Set

from loguru import logger

from utils import ITEM


class README(object):
    def __init__(self, fileName):
        self.fileName = fileName
    
    def getItems(self, path_dst:str):
        itemList = []
        try:
            with open(self.fileName, "r") as f:
                lines = f.readlines()
            for line in lines:
                line = line.replace('\n', '')
                if re.match('^\|.*\|.*\|.*\|.*\|.*\|$', line):
                    line = line[1:-1].split('|')
                    line = [x.strip() for x in line]
                    if line[0] in ("项目", "---"):
                        continue
                    itemList.append(ITEM(line[0][line[0].find("(") + 1 + len("https://github.com/"):-1], line[2][1:-1], line[3][1:-1] if len(line[3]) > 2 else "", line[4], path_dst[:path_dst.rfind("/")+1] + line[5][1:-1], line[6])) # 生产
                    #itemList.append(ITEM(line[0][line[0].find("(") + 1 + len("https://github.com/"):-1], line[2][1:-1], line[3][1:-1] if len(line[3]) > 2 else "", line[4], path_dst[:path_dst.rfind("/")+1] + line[5][1:-1], line[6], proxy = "https://ghfast.top/")) # 测试
        except Exception as e:
            logger.exception("%s" % (e))
        finally:
            return itemList
    
    def generate(self, itemList: List[ITEM], path_dst: str, versionFile: str):
        fileTmp = self.fileName + '.tmp'
        try:
            with open(fileTmp, "w") as f:
                f.write("# Switch\n")
                f.write("自用 Switch 整合包，根据以下整合清单，自动更新打包\n")
                f.write("\n")
                f.write("## 整合清单\n")
                f.write("\n")
                f.write("| 项目 | 作者 | 软件 | 版本 | 更新日期 | 存放路径 | 备注 |\n")
                f.write("| --- | --- | --- | --- | --- | --- | --- |\n")
                for item in itemList:
                    f.write("| [%s](%s) | %s | `%s` | `%s` | %s | `%s` | %s |\n"%(item.repo[item.repo.find("/") + 1:], item.url, item.repo[:item.repo.find("/")], item.pattern, item.releaseTag, item.fileDate, item.dst.replace(path_dst, path_dst[path_dst.rfind("/") + 1:]), item.remark))
            os.remove(self.fileName)
            os.rename(fileTmp, self.fileName)

            with open(versionFile, "w") as f:
                f.write("# 整合清单\n")
                f.write("\n")
                f.write("| 项目 | 作者 | 版本 | 更新日期 |\n")
                f.write("| --- | --- | --- | --- |\n")
                for item in itemList:
                    f.write("| [%s](%s) | %s | `%s` | %s |\n"%(item.repo[item.repo.find("/") + 1:], item.url, item.repo[:item.repo.find("/")], item.releaseTag, item.fileDate))
        except Exception as e:
            logger.exception("%s" % (e))
        finally:
            if os.path.exists(fileTmp):
                os.remove(fileTmp)
