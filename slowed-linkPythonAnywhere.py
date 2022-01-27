#SLOWED---WITH---LINK
from __future__ import unicode_literals
import youtube_dl
import os
link = input('Enter link :  ')
speed = input('Enter speed :  ')
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
    input=title+'.'+'mp3'
    ydl.download([link])
os.rename('./%s'%conc, "input.mp3")

#------------------------------------------------------------------------------#
from scipy.io import wavfile
import wave
import os
import numpy as np
import matplotlib.pyplot as plt
from pydub import AudioSegment

 #Define conversion format function
def trans_mp3_to_wav(filepath):
    song = AudioSegment.from_mp3(filepath)
    song.export("temp.wav", format="wav")
trans_mp3_to_wav("./input.mp3")

import logging
import librosa as lr
import soundfile as sf
from pysndfx.dsp import AudioEffectsChain
logger = logging.getLogger('pysndfx')
logger.setLevel(logging.DEBUG)
apply_audio_effects =     (AudioEffectsChain()
     .speed(speed)
     .reverb()
    )
infile = './temp.wav'
mono, sr = lr.load(infile, sr=None)
stereo, _ = lr.load(infile, sr=None, mono=False)
outfile = 'output.wav'

def test_file_to_file():
    apply_audio_effects(infile, outfile)
    y = lr.load(outfile, sr=None, mono=False)[0]
    sf.write('output.wav', y.T, sr)
    assert lr.util.valid_audio(y, mono=False)
test_file_to_file()
os.remove('./temp.wav')
import pydub
sound = pydub.AudioSegment.from_wav("./output.wav")
sound.export("final.mp3", format="mp3")
os.remove('./output.wav')

os.rename("final.mp3","%s"%full)
os.rename("input.mp3","%s"%input)