from pytube import *

try:
    url = input("Please put url of Youtbe video that you want to download : ")
except:
    print("Invalid url")

my_video = YouTube(url)
yt = my_video.title
print(yt, "\n")
print("Your Download has been started")

my_video = my_video.streams.get_highest_resolution()
my_video.download()
