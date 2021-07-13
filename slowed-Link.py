#SLOWED---WITH---LINK
from __future__ import unicode_literals
import youtube_dl
link = input('Enter link :  ') 
speed = input('Enter speed :  ') 
ydl_opts = {
    #'outtmpl': '/input.mp3',
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',
        
    }],
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([link]) 
    
print('Youtube Downloader'.center(40, '_'))

URL = input('Change the downloaded file name to input.mp3 :  ')    
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
apply_audio_effects = \
    (AudioEffectsChain()
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