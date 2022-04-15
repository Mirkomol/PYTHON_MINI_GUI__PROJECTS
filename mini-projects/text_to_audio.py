from gtts import gTTS

from playsound import playsound

audio = 'turkısh.mp3'
language = 'tr'

sp = gTTS(text="selamun aleykum arkadaşlar"
          , lang=language, slow=False)

sp.save(audio)
playsound(audio)
