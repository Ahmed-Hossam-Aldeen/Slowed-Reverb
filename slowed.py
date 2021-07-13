 #------------------------------------------------------------------------------#    
from scipy.io import wavfile
import wave
import os
import numpy as np
import matplotlib.pyplot as plt
from pydub import AudioSegment
speed = input('Enter speed :  ') 
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





