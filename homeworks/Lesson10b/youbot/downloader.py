from turtle import down
from pytube import YouTube
from os.path import isfile


async def tube_download(url:str) -> str:
    video = YouTube(url)
    vid_title = video.title.replace('|','')\
                            .replace(':','')\
                            .replace('.','')\
                            .replace('<','')\
                            .replace('>','')\
                            .replace('/','')\
                            .replace('\ '.replace(' ',''),'')\
                            .replace('?','') + '.mp4'
    
    video_dwl = video.streams.get_highest_resolution()
    video_dwl.download('homeworks\Lesson10b\youbot')
    while not isfile('homeworks\Lesson10b\youbot\ '.replace(' ','')+vid_title):
        continue
    return vid_title

