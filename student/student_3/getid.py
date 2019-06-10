import numpy as np

def sigmoid (x):
    return 1/(1 + np.exp(-x))

def getoutput(X,wh,bh,wout,bout):
    hidden_layer_input1=np.dot(X,wh)
    hidden_layer_input=hidden_layer_input1 + bh
    hiddenlayer_activations = sigmoid(hidden_layer_input)
    output_layer_input1=np.dot(hiddenlayer_activations,wout)
    output_layer_input= output_layer_input1+ bout
    output = sigmoid(output_layer_input)
    return output

wout=np.load(open('parameter/wout.npy','rb'))
bout=np.load(open('parameter/bout.npy','rb'))
wh=np.load(open('parameter/wh.npy','rb'))
bh=np.load(open('parameter/bh.npy','rb'))

def fun():
    X=np.load(open('data/iddata.npy','rb'))
    y=getoutput(X,wh,bh,wout,bout)

    return y




