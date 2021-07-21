#SLOWED---WITH---LINK
from __future__ import unicode_literals
import youtube_dl
import os
link = input('Enter link :  ')
ydl_opts = {
    #'outtmpl': '/' + str(input) +'.%(mp3)s',
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',

    }],
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    info_dict = ydl.extract_info(link, download=False)
    title = info_dict.get('title', None)
    id=video_id = info_dict.get("id", None)
    ful= title+' '+"[slowed + reverb]"+'.'+'mp3'
    con= title+'-'+id+'.'+'mp3'
    conc=con.replace("|","_")
    full=ful.replace("|","_")
    print(conc)
    ydl.download([link])
os.rename('./%s'%conc, "input.mp3")

#------------------------------------------------------------------------------#
import slowed
os.rename("final.mp3","%s"%full)