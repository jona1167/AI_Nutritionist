from characterai import PyCAI#pip install characterai
from whisper_mic.whisper_mic import WhisperMic
import keyboard
#import pyttsx3
import elevenlabs

client = PyCAI('')#write your token inside
client.start()
char = 'fq6_grwY_YHUNfb_ha18r_pp40-GudgMDhtFnu7cxsI'#can change now is  Nutritionist
#https://beta.character.ai/chat?char=fq6_grwY_YHUNfb_ha18r_pp40-GudgMDhtFnu7cxsI
#chat = client.chat.get_chat(char)
chat = client.chat.new_chat(char)
history_id = chat['external_id']
participants = chat['participants']

mic = WhisperMic("small")#small

#engine = pyttsx3.init()
# voice speed
#rate = engine.getProperty('rate')
#engine.setProperty('rate', rate-50)#rate 200

voice = elevenlabs.Voice(
    voice_id = "XB0fDUnXU5powFXDhCwa",#Charlotte
    settings = elevenlabs.VoiceSettings(
        stability = 0.5,
        similarity_boost = 0.5
    )
)

def show_history():#print one line
    history = client.chat.get_history(history_id)
    h = history['messages'][0]
    name = h['src_char']['participant']['name']
    text = h['text']
    print(f'{name}: {text}')
    speak(text)

def gpt(tgt,message):
    data = client.chat.send_message(chat['external_id'], tgt, message)
    name = data['src_char']['participant']['name']
    text = data['replies'][0]['text']
    print(f"{name}: {text}")
    speak(text)
       
def start_listening():
    show_history()
    tgt = participants[1]['user']['username']#mean 0 is Nutritionist 1 is user
    print("Presss 'z' to speak\n")   
    while True:
        if keyboard.is_pressed('z'):
            result = mic.listen()
            print("You: "+result)
        #message = input('You: ')
            gpt(tgt,result)
            print("Presss 'z' to speak\n")  
        
def speak(message):
        #engine.say(message)
        #engine.runAndWait()
    audio = elevenlabs.generate(
    text = message,
    voice = voice
    )
    elevenlabs.play(audio)
    


if __name__ == '__main__':
    start_listening() 