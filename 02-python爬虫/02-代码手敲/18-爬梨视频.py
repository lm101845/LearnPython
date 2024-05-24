# @Date : 2024/3/22 14:05
# @Author : liming

import requests

url = "https://www.pearvideo.com/video_1792985"
contId = url.split("_")[1]

videoStatus = f"https://www.pearvideo.com/videoStatus.jsp?contId={contId}&mrd=0.685191403667422"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    #防盗链
    "Referer": "https://www.pearvideo.com/video_1792985"
}

resp = requests.get(videoStatus,headers=headers)

# print(resp.text)
# print(resp.json())
dic = resp.json()
srcUrl = dic["videoInfo"]["videos"]["srcUrl"]
systemTime = dic["systemTime"]
srcUrl = srcUrl.replace(systemTime, f"cont-{contId}")
print(srcUrl)
# 真实链接：https://video.pearvideo.com/mp4/short/20240321/cont-1792985-71106188-hd.mp4
# 拿到的链接：https://video.pearvideo.com/mp4/short/20240321/1711088269442-71106188-hd.mp4

