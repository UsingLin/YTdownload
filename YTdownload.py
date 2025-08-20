import ssl
from pytubefix import YouTube
import os

# print(yt.title)           # 影片標題
# print(yt.length)          # 影片長度 ( 秒 )
# print(yt.author)          # 影片作者
# print(yt.channel_url)     # 影片作者頻道網址
# print(yt.thumbnail_url)   # 影片縮圖網址
# print(yt.views)           # 影片觀看數
#------------------------------------------------------------------------
#ANSI碼
    # print("\033[31m這是紅色\033[0m")
    # print("\033[32m這是綠色\033[0m")
    # print("\033[33m這是黃色\033[0m")
    # print("\033[34m這是藍色\033[0m")
    # print("\033[35m這是紫色\033[0m")
    # print("\033[36m這是青色\033[0m")
    # print("\033[0m回到預設顏色")

#ssl憑證
if hasattr(ssl, "_create_unverified_context"):
    ssl._create_default_https_context = ssl._create_unverified_context

#音樂下載
def Download_mp3(url):
    try:
        yt = YouTube(url)
        print("\033[34mDownloading... \033[0m" + yt.title)

        #下載檔案位置
        if not os.path.exists('C:/Users/USER/Downloads'):
            print("該路徑不存在")

        stream =yt.streams.filter(only_audio=True).first()  # only audio
        out_file = stream.download(output_path= 'C:/Users/USER/Downloads')    # 檔案下載

        # file name
        base, ext = os.path.splitext(out_file)
        new_file = base + ".mp3"
        os.rename(out_file, new_file)

        print("\033[32m下載完成: \033[0m", new_file)

    except Exception as e:
        print("\033[31m下載失敗: \033[0m", e)

if __name__ == "__main__":
    Download_mp3(input())