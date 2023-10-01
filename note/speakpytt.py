import pyttsx3

engine = pyttsx3.init()
# voice speed
rate = engine.getProperty('rate')
print(rate)
engine.setProperty('rate', rate-50)
# voice volume
volume = engine.getProperty('volume')
print(volume)
engine.setProperty('volume', volume+0.50)
# voice speak
engine.say("Hello, This is the test for the pyttsx3")
engine.runAndWait()



