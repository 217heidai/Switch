import os
import shutil
import zipfile
import re

from loguru import logger

class UTIL(object):
    @staticmethod
    def copyFile(fileSrc: str, fileDst: str):
        if os.path.exists(fileSrc):
            if os.path.exists(fileDst):
                os.remove(fileDst)
            os.makedirs(os.path.dirname(fileDst), exist_ok=True) # 先创建目录
            shutil.copy(fileSrc, fileDst)
        else:
            raise Exception("%s not found"%(fileSrc))

    @staticmethod
    def renameFile(fileSrc: str, fileDst: str):
        if os.path.exists(fileSrc):
            if os.path.exists(fileDst):
                os.remove(fileDst)
            os.rename(fileSrc, fileDst)
        else:
            raise Exception("%s not found"%(fileSrc))
        
class ITEM(object):
    def __init__(self, repo:str, pattern:str, version:str="", date:str="", dst:str="", remark:str="", proxy:str = None):
        self.repo = repo
        self.url = "https://github.com/" + self.repo
        self.pattern = pattern
        self.fileName = ""
        self.dst = dst
        self.proxy = proxy
        self.isDownload = False
        self.fileDate = date
        self.releaseTag = version
        self.remark = remark
    
    def process(self, path: str):
        try:
            if len(self.dst) == 0:
                self.dst = path
            else:
                self.dst = os.path.join(path, self.dst)
            
            if self.fileName[self.fileName.rfind("."):] == ".zip":
                with zipfile.ZipFile(self.fileName, 'r') as zip_ref:
                    zip_ref.extractall(self.dst)
            elif self.fileName[self.fileName.rfind("."):] in (".bin", ".nro", ".config"):
                UTIL.copyFile(self.fileName, self.dst)
            else:
                pass

            # 特殊处理
            ## switch硬破，需要将 hekate_ctcaer_x.x.x.bin 重命名为 payload.bin 放入 SD 卡根目录
            if re.match("^hekate.*sc.zip$", os.path.basename(self.fileName)):
                fileSrc = "%s/hekate_ctcaer_%s.bin"%(self.dst, self.releaseTag[1:])
                fileDst = "%s/payload.bin"%(self.dst)
                UTIL.renameFile(fileSrc, fileDst)
        except Exception as e:
            logger.exception("%s" % (e))