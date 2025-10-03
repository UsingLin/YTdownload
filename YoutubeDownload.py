import ssl
from pytubefix import YouTube
import os
import sys
import customtkinter as ctmtk
from tkinter import Tk, filedialog

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
def Download_mp3(url, download_address):
    try:
        yt = YouTube(url)

        print(download_address)
        #下載檔案位置是否存在
        if not os.path.exists(download_address):
            print("該路徑不存在")
            sys.exit()

        print("\033[33mMP3\033[0m -> \033[34mDownloading... \033[0m" + yt.title)
        stream =yt.streams.filter(only_audio=True).first()  # only audio
        out_file = stream.download(output_path= download_address)    # 檔案下載

        # file name
        base, ext = os.path.splitext(out_file)
        new_file = base + ".mp3"
        os.rename(out_file, new_file)

        print("\033[32m下載完成: \033[0m", new_file)

    except Exception as e:
        print("\033[31m下載失敗: \033[0m", e)

#影片下載
def Download_mp4(url, download_address):
    try:
        yt = YouTube(url)

        print(download_address)
        if not os.path.exists(download_address):
            print("該路徑不存在")
            sys.exit()

        print("\033[33mMP4\033[0m -> \033[34mDownloading... \033[0m" + yt.title)
        out_file = yt.streams.filter().get_highest_resolution().download(output_path= download_address)

        #file name
        base, ext = os.path.splitext(out_file)
        new_file = base + ".mp4"
        os.rename(out_file, new_file)

        print("\033[32m下載完成: \033[0m", new_file)

    except Exception as e:
        print("\033[31m下載失敗: \033[0m", e)

#選擇下載位置
def choose_download_path():
    root = Tk()
    root.mainloop()
    folder = filedialog.askdirectory(title="選擇下載資料夾")
    if not folder:
        print("沒有選擇資料夾")
        sys.exit()
    return os.path.normpath(folder)

#主程式
if __name__ == "__main__":
    while True:
            videos = int(input("1. mp3  2. mp4, Input 1 or 2: "))

            if videos ==1:
                download_address = choose_download_path()
                url = input("輸入想要下載音樂的網址(連結) ")
                Download_mp3(url, download_address)
            elif videos == 2:
                download_address = choose_download_path()
                url = input("輸入想要下載影片的網址(連結) ")
                Download_mp4(url, download_address)
            elif videos == 9:
                break


