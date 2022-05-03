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

        self.root.geometry("600x350")
        self.root.title("vocal prediction")
        self.root.resizable(0,0)
        self.root.configure(background="#17122b")

        self.warning=tk.Label(self.root, text="This voice save every 5 seconds",bg="#17122b",font=("Lucida Sans", 12))
        self.photo_image = tk.PhotoImage(file="../gender_voice_recognition/GUI/start.png")
        self.voice=tk.Button(self.root,image=self.photo_image ,command=self.save_voice, height = 120, width = 100)
        
        self.gender=tk.Label(self.root, text="You're gender is :")
        self.gender_predict=tk.Label(self.root, text="")
        
        self.warning.configure(foreground="red")
        self.gender.configure(foreground="green",bg="#17122b",font=("Century Gothic", 11))
        self.gender_predict.configure(foreground="green",bg="#17122b",font=("Century Gothic", 11))
        self.warning.place(x=190,y=20)
        self.voice.place(x=265,y=120)
        self.gender.place(x=195,y=290)
        self.gender_predict.place(x=325,y=290)
        
        
    ####################################3  function to save voice to '.wav'    
    def save_voice(self):
        freq = 44100
        duration=3
        recording = sd.rec(int(duration * freq),samplerate=freq, channels=2)
        sd.wait()
        wv.write("../gender_voice_recognition/voice/saving_voice.wav", recording, freq, sampwidth=2)
        self.gender_predict.config(text = "{}".format(self.p))

