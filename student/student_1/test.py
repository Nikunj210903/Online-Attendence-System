import os
import pickle
import numpy as np
from scipy.io.wavfile import read
from speakerfeatures import extract_features
import librosa

import time
 
#path to training data
source   = "development_set\\"   

modelpath = "speaker_models\\"

test_file = "development_set_test.txt"        

file_paths = open(test_file,'r')

gmm_files = [os.path.join(modelpath,fname) for fname in
              os.listdir(modelpath) if fname.endswith('.gmm')]
 
#Load the Gaussian gender Models
models    = [pickle.load(open(fname,'rb')) for fname in gmm_files]
speakers   = [fname.split("\\")[-1].split(".gmm")[0] for fname 
              in gmm_files]
 
# Read the test directory and get the list of test audio files 
for path in file_paths:   
     
    path = path.strip()   
    print(path)
    audio,sr=librosa.load(source+path,res_type='kaiser_fast')
    vector   = extract_features(audio,sr)
     
    log_likelihood = np.zeros(len(models)) 
     
    for i in range(len(models)):
        gmm    = models[i]  #checking with each model one by one
        scores = np.array(gmm.score(vector))
        log_likelihood[i] = scores.sum()
        print("probability : ", scores.sum())
     
    winner = np.argmax(log_likelihood)
    #print("winner : ",winner)
    print("\tdetected as - ", speakers[winner])
    #time.sleep(1.0)
