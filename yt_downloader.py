from yt_dlp import YoutubeDL
from sys import argv

link = argv[1]
yt = YoutubeDL(link)

print("Title:", yt.title)

print("View:", yt.views)

yt = yt.streams.get_highest_resolution()

yt.download('/Users/sjbsr/Desktop/MINE_OLD')

