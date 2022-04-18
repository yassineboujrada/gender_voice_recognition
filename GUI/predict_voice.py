# import librairies
import numpy as np
from scipy.io import wavfile
import pandas as pd
from sklearn.model_selection import train_test_split as tts
from sklearn.ensemble import RandomForestClassifier as RF
import pickle

################### class to get setting of audio ####################

class get_proprieties:
    
    def __init__(self):
        self.path="../gender_voice_recognition/voice/saving_voice.wav"
        self.setting=self.audio_data()
    
    def transfer_KHz(self,parametre):
        return parametre/1000
    
    def audio_data(self):
        fs, data = wavfile.read(self.path)
        
        # use the first channel only
        if data.ndim > 1:
            data = data[:, 0]
            
        spec = np.abs(np.fft.rfft(data))
        freq = np.fft.rfftfreq(len(data), d=1/fs)
        assert len(spec) == len(freq)
        amp = spec / spec.sum()
        amp_cumsum = amp.cumsum()
        assert len(amp_cumsum) == len(freq)
        q25 = freq[len(amp_cumsum[amp_cumsum < 0.25])]
        q75 = freq[len(amp_cumsum[amp_cumsum < 0.75])]
        mean=(freq * amp).sum()
        median = freq[len(amp_cumsum[amp_cumsum <= 0.5]) + 1]
        sd = np.sqrt(np.sum(amp * ((freq - mean) ** 2)))
        IQR = q75 - q25
        z = amp - amp.mean()
        w = amp.std()
        skew = ((z ** 3).sum() / (len(spec) - 1)) / w ** 3
        kurt = ((z ** 4).sum() / (len(spec) - 1)) / w ** 4
        mode = freq[amp.argmax()]
        
        return [
            self.transfer_KHz(mean),
            self.transfer_KHz(sd),
            self.transfer_KHz(median),
            self.transfer_KHz(mode),
            self.transfer_KHz(q25),
            self.transfer_KHz(q75),
            self.transfer_KHz(IQR),
            self.transfer_KHz(skew),
            self.transfer_KHz(kurt)
        ]

#######################  class of predict which gender is from audio ###########################

class predict_voice:
    p=get_proprieties().audio_data()
    
    def model(self):
        file="../gender_voice_recognition/data/model_for_voice_rcognition.sav"
        model = pickle.load(open(file, 'rb'))
        return model
    
    def predict_value(self):
        self.X_pred=np.array([self.p])
        y_predict=self.model().predict(self.X_pred)
        if int(y_predict)==1:
            return "male"
        else:
            return "female"
        