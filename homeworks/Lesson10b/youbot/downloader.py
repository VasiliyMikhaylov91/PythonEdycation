from pytube import YouTube

def tube_title(url:str):
    return YouTube(url).title

def tube_download(url):
    video = YouTube(url)
    video_dwl = video.streams.get_highest_resolution()
    video_dwl.download()
    
# if __name__ == '__main__':
#     my_url = 'https://www.youtube.com/watch?v=7BXJIjfJCsA'
#     print(tube_title(my_url))
#     # tube_download(my_url)

# vid = YouTube('https://www.youtube.com/watch?v=kn8ZuOCn6r0')
# print('Downloading ', vid.title)
# print('Views: ', vid.views)
# print('Length: ', vid.length, 'seconds')
# print('Description: ', vid.description)
# print('Ratings: ', vid.rating)
# vid_download = vid.streams.get_highest_resolution() 
# print(vid_download)
# vid_download.download()

# # importing the module  
# from pytube import YouTube  
# # download location of the file  
# DOWNLOAD_PATH = " G:\GeekBrains\PythonEdycation\homeworks\Lesson10b\youbot"   
# # link of the video to be downloaded  
# link="https://www.youtube.com/watch?v=kn8ZuOCn6r0"  
# try:  
#     # creating youtube object using YouTube  
#     youtube_obj = YouTube(link)  
# except:  
#     print("Connection Error") #to handle exception  
# # filters out all the files with "mp4" extension  
# mp4files = youtube_obj.streams
# #to set the name of the file  
# # youtube_obj.set_filename('Downloaded Video')  
# # get the video with the extension and  
# # resolution passed in the get() function  
# d_video = youtube_obj.streams.get_highest_resolution() 
# try:  
#     # downloading the video  
#     d_video.download()  
# except:  
#     print("The is Some Error!")  
# print('Task is Completed!')