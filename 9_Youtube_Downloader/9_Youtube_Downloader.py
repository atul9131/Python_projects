# from pytube import YouTube

# link = 'https://www.youtube.com/watch?v=MlsRFcs1Bzc'

# youtube_1 = YouTube(link)

# # print(youtube_1.title)
# # print(youtube_1.thumbnail_url)

# videos = youtube_1.streams.all()
# # videos = youtube_1.streams.filter(only_audio=True)
# vid = list(enumerate(videos))
# for i in vid:
#     print(i)
# strm = int(input('Enter : '))
# videos[strm].download()
# print('Successfully Download')


# ***********  For Youtube Playlist ***********


from pytube import Playlist

py = Playlist('https://www.youtube.com/playlist?list=PLjVLYmrlmjGdqdwNZvre2yPI6n5LyQ5M9')
print(f'Downloading : {py.title}')

for video in py.videos:
    video.streams.first().download()


