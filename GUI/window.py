import tkinter as tk
import sounddevice as sd
import wavio as wv
from predict_voice import * 

class window_tk(tk.Frame):
    
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)

        tk.Frame.grid(self,row=0,column=0,sticky="NW")
        tk.Frame.update(self)
        self.root = parent
        self.p=predict_voice().predict_value()
        
        
        ###################################  designe my GUI  #################################

        self.root.geometry("300x400")
        self.root.title("vocal prediction")
        self.root.resizable(0,0)

        self.warning=tk.Label(self.root, text="you need to determine duration for saving you're voice")#,bg="#000042")
        self.checktime=tk.Entry(self.root, textvariable = "number_of_duration", width = 8)
        self.photo_image = tk.PhotoImage(file="../gender_voice_recognition/GUI/yy.png")
        self.voice=tk.Button(self.root,image=self.photo_image ,command=self.save_voice, height = 50, width = 70)
        
        self.gender=tk.Label(self.root, text="gender predection :")
        self.gender_predict=tk.Label(self.root, text="")
        
        self.warning.configure(foreground="red")
        self.gender.configure(foreground="green")
        self.gender_predict.configure(foreground="green")
        self.warning.place(x=5,y=20)
        self.voice.place(x=110,y=170)
        self.checktime.place(x=120,y=120)
        self.gender.place(x=35,y=270)
        self.gender_predict.place(x=175,y=270)
        
        
    ####################################3  function to save voice to '.wav'    
    def save_voice(self):
        freq = 44100
        
        if self.checktime.get() == "":
            duration=2
        else:
            duration = int(self.checktime.get())
            
        recording = sd.rec(int(duration * freq),samplerate=freq, channels=2)
        sd.wait()
        wv.write("../gender_voice_recognition/voice/saving_voice.wav", recording, freq, sampwidth=2)
        self.gender_predict.config(text = "{}".format(self.p))

