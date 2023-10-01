import elevenlabs
 	
#elevenlabs.set_api_key("my-api-key")

voice = elevenlabs.Voice(
    voice_id = "TxGEqnHWrfWFTfGW9XjX",#Josh
    settings = elevenlabs.VoiceSettings(
        stability = 0.5,
        similarity_boost = 0.5
    )
)
 
audio = elevenlabs.generate(
    text = "Hi, I'm from the future!",
    voice = voice
)
 
elevenlabs.play(audio)
