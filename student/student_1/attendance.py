import requests
#import getid
import getaudio
#import feature_extraction
import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
import weakref
from speakerfeatures import extract_features 
import librosa
import numpy as np


import os
import pickle


flag=0
year="year-3"
branch="CP"
sem="Sem-6"
#subject="C"
id_no="52"

from kivy.config import Config
Config.set('graphics','width','850')
Config.set('graphics','height','120')


class gridlayout(GridLayout):
    
    def set_credential(self):
        print( "button 2....",self.ids["b2"].disabled)
        global flag
        global year
        global branch
        global sem
        #global subject
        global id_no
        if flag==0:
            self.ids["b2"].text="Set_Credential"
            self.ids.box.clear_widgets()
            self.ids["b1"].disabled=True
            
            T=TextInput(text="year:")
            self.ids.box.add_widget(Label(text="year:"))
            self.ids.box.add_widget(T)
            self.ids["year"]=weakref.ref(T)
            
            T=TextInput(text="branch:")
            self.ids.box.add_widget(Label(text="branch:"))
            self.ids.box.add_widget(T)
            self.ids["branch"]=weakref.ref(T)

            T=TextInput(text="sem:")
            self.ids.box.add_widget(Label(text="sem:"))
            self.ids.box.add_widget(T)
            self.ids["sem"]=weakref.ref(T)
            
            #T=TextInput(text="subject:")
            #self.ids.box.add_widget(Label(text="subject:"))
            #self.ids.box.add_widget(T)
            #self.ids["subject"]=weakref.ref(T)

            #T=TextInput(text="id_no:")
            #self.ids.box.add_widget(Label(text="id_no:"))
            #self.ids.box.add_widget(T)
            #self.ids["id_no"]=weakref.ref(T)

            self.ids.year.text=year
            self.ids.branch.text=branch
            self.ids.sem.text=sem
            #self.ids.subject.text=subject
            #self.ids.id_no.text=id_no
            flag=1
        else:
           self.ids["b2"].text="Change_Credential"
           self.ids["b1"].disabled=True
           year=self.ids.year.text
           branch=self.ids.branch.text
           sem=self.ids.sem.text
           #subject=self.ids.subject.text
           #id_no=self.ids.id_no.text 
           self.ids["b1"].disabled=False
           self.ids.box.clear_widgets()
           
           T=TextInput(text="Press any Button:",font_size=32)
           self.ids.box.add_widget(T)
           self.ids["entry"]=weakref.ref(T)
           
           flag=0
           print(year,branch)
        print("hello...")



    def change(self):
        print("hello1")
        self.ids.entry.text="Speak something"
        self.ids["b1"].disabled=True
        self.ids["b2"].disabled=True
        print("in change..", self.ids["b2"].disabled)    


    def send_credential(self):
        print("in send credential..", self.ids["b2"].disabled)    

        #self.ids.entry.text="Speak your Id no"
        self.ids["b1"].disabled=True
        getaudio.fun("audio.wav")
        #feature_extraction.fun("audio.wav","data")
        #idno1=getid.fun(feature_extraction.fun("audio.wav"))
        #got_idno=idno1
        #print(got_idno)




        modelpath = "speaker_models/"
        gmm_files = [os.path.join(modelpath,fname) for fname in
                      os.listdir(modelpath) if fname.endswith('.gmm')]

        models    = [pickle.load(open(fname,'rb')) for fname in gmm_files]
        speakers   = [fname.split("\\")[-1].split(".gmm")[0] for fname 
                      in gmm_files]
        
    
        audio,sr=librosa.load("audio.wav",res_type='kaiser_fast')
        vector   = extract_features(audio,sr)
        log_likelihood = np.zeros(len(models))
        for i in range(len(models)):
            gmm    = models[i]  #checking with each model one by one
            scores = np.array(gmm.score(vector))
            log_likelihood[i] = scores.sum()
            print("score : ", scores.sum())
     
        winner = np.argmax(log_likelihood)
        print(winner)
        print("\tdetected as - ", speakers[winner])

        
        

        
        if speakers[winner]=="speaker_models/nikunj":
            u="http://localhost:5000/attendence?year=" + year + "&branch=" + branch + "&sem=" + sem  + "&id_no=" + id_no
            r=requests.post(url=u)
            print(r.text)
            self.ids.entry.text=r.text
            self.ids.entry.text="Nikunj"
        else:
            self.ids.entry.text="you are not id_no : "+id_no
            self.ids.entry.text="Not Nikunj"
        self.ids["b1"].disabled=False
        self.ids["b2"].disabled=False
        
    
class Student(App):
    #self.height=220
    def build(self):
        
        return gridlayout()

Student().run()




