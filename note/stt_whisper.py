#pip install whisper-mic
#https://github.com/sankhadeepdutta/whisper_mic/tree/main
from whisper_mic.whisper_mic import WhisperMic
import keyboard
mic = WhisperMic("small")

# make a loop if keyboard z is press cointinous mic.listen_loop and print it 
#result = mic.listen()
#print(result)
print('You: ')
while True:      
    if keyboard.is_pressed('z'):
        result = mic.listen()
        print(result)