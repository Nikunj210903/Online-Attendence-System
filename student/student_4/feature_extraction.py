import librosa
import librosa.display
import IPython
import numpy as np
import pandas as pd
import scipy
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder 

def sigmoid (x):
    return 1/(1 + np.exp(-x))

def fun():
    x,sr1=librosa.load('audio.wav',res_type='kaiser_fast')
    #print(len(x))
    #print(sr1)

    mfccs=np.mean(librosa.feature.mfcc(y=x,sr=sr1,n_mfcc=40).T,axis=0)
    data1=mfccs.tolist()

    data2=np.array([data1])
    data=sigmoid(data2)

    data.dump(open('data/iddata.npy','wb'))

fun()
