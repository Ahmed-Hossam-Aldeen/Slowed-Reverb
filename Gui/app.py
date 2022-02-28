from PyQt5 import QtGui, QtWidgets, uic
import sys
from PyQt5.uic.properties import QtCore
import numpy
from scipy.io import wavfile
import wave
import numpy as np
from pydub import AudioSegment
import logging
import librosa as lr
import soundfile as sf
from pysndfx.dsp import AudioEffectsChain
import pydub
import youtube_dl
import os
from threading import *
import time 

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('slowed.ui', self)
        self.setWindowTitle("[Slow + Reverb]")
        self.slow.clicked.connect(self.thread1)
        self.slow.clicked.connect(self.thread2)
        self.label.hide()    
        self.label2.hide() 
        self.show()
    
    def trans_mp3_to_wav(filepath):
            song = AudioSegment.from_mp3(filepath)
            song.export("temp.wav", format="wav")
            
            
    def thread1(self):
        t1=Thread(target=self.slowed)
        t1.start()
        
    def thread2(self):
        t2=Thread(target=self.bar)
        t2.start()    
        self.label.hide() 
        self.label2.show()
        
    def bar(self):   
        for i in range(95):
            time.sleep(0.2)
            self.progressBar.setValue(i+1)
        
    def slowed(self):
        self.label2.setHidden(False)
        link = self.link.text()
        ydl_opts = {
            'outtmpl': "audio" +'.%(mp3)s','format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320',}],}

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            title = info_dict.get('title', None)
            id=video_id = info_dict.get("id", None)
            ful= title+' '+"[slowed + reverb]"+'.'+'mp3'
            ful2=title+'.'+'mp3'
            con= title+'-'+id+'.'+'mp3'
            conc=con.replace("|","_")
            full=ful.replace("|","_")
            full2=ful2.replace("|","_")
            print(conc)
            ydl.download([link])
        os.rename("audio.mp3", "input.mp3")

        #------------------------------------------------------------------------------#
        
        speed = float(self.speed.text())
        #Define conversion format function
        
        #trans_mp3_to_wav("./input.mp3")
        song = AudioSegment.from_mp3("./input.mp3")
        song.export("temp.wav", format="wav")
        
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
        
        sound = pydub.AudioSegment.from_wav("./output.wav")
        sound.export("final.mp3", format="mp3")
        os.remove('./output.wav')
        #------------------------------------------------------------------------------#
        os.rename("final.mp3","%s"%full)
        os.rename("input.mp3","%s"%full2)
        self.label2.hide()
        self.label.show()
        self.progressBar.setValue(100)
app = 0
app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()        
