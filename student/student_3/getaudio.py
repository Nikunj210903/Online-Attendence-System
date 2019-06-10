import pyaudio
import wave
from array import array

def fun():
    FORMAT=pyaudio.paInt16
    CHANNELS=2
    RATE=44100
    CHUNK=1024
    RECORD_SECONDS=2
    FILE_NAME="audio.wav"
    print("say something")
    audio=pyaudio.PyAudio() #instantiate the pyaudio

    #recording prerequisites
    stream=audio.open(format=FORMAT,channels=CHANNELS, 
                      rate=RATE,
                      input=True,
                      frames_per_buffer=CHUNK)

    #starting recording
    frames=[]

    for i in range(0,int(RATE/CHUNK*RECORD_SECONDS)):
        data=stream.read(CHUNK)
        data_chunk=array('h',data)
        vol=max(data_chunk)
        if(vol>=200):
            #print("something said")
            frames.append(data)
        #5else:
            
            #print("nothing")
        #print("\n")
    print("done")

    #end of recording
    stream.stop_stream()
    stream.close()
    audio.terminate()
    #writing to file
    wavfile=wave.open(FILE_NAME,'wb')
    wavfile.setnchannels(CHANNELS)
    wavfile.setsampwidth(audio.get_sample_size(FORMAT))
    wavfile.setframerate(RATE)
    wavfile.writeframes(b''.join(frames))#append frames recorded to file
    wavfile.close()


