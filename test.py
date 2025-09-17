import os

path = os.getcwd() + "/tmp"

def test_down_direct():
    from downloader import DOWNLOADER

    downloader = DOWNLOADER()
    downloader.down_direct("https://raw.githubusercontent.com/217heidai/Switch/refs/heads/main/LICENSE", path,"LICENSE")

def test_down_repository():
    from downloader import DOWNLOADER
    
    downloader = DOWNLOADER()
    isDownload, fileName, commint_id, commint_date = downloader.down_git_repository("https://github.com/217heidai/Switch", path, "main", proxy="https://ghfast.top/")
    if isDownload:
        print(fileName, commint_id, commint_date)

def test_down_release():
    from downloader import DOWNLOADER

    downloader = DOWNLOADER()
    isDownload, fileName, fileDigest, fileDate = downloader.down_git_release("https://github.com/217heidai/OpenWrt-Builder", path, ".*gateway.config$", proxy="https://ghfast.top/")
    if isDownload:
        print(fileName, fileDigest, fileDate)

if __name__ == "__main__":
    if not os.path.exists(path):
        os.makedirs(path)
    
    #test_down_direct()
    #test_down_repository()
    test_down_release()