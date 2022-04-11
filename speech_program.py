import pyttsx3
print('Welcome to Voice program \U0001F603, you can use commands.\n voice_gender(), voice_rate(), end()')
num = int(input('chose voice (0: male/1: female): '))
rate = 150
while True:
    text = input('say your message: ')
    if text == 'voice_gender()':
        num = int(input('chose gender of voice (0: male/1: female): '))
    elif text == 'end()':
        print('see you later \U0001F600!')
        break
    elif text == 'voice_rate()':
        rate = int(input('chose voice rate: '))
    sound = pyttsx3.init()
    voices = sound.getProperty('voices')
    sound.setProperty('voice', voices[num].id)
    sound.setProperty('rate', rate)
    sound.say(text)
    sound.runAndWait()
