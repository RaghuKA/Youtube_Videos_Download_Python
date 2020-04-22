from __future__ import unicode_literals
import youtube_dl
import os

with open('Download_inputs.txt') as f:
    my_list = list(f)

ydl_opts = {}
os.mkdir('Downloaded_videos')
os.chdir('Downloaded_videos')
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
     ydl.download(my_list)
