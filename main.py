import sys
import voice_handler
from time import sleep

engine = voice_handler.init_engine()
voice = voice_handler.get_voice(engine)
voice_handler.speak("Hello, I am your stand up reminder. How many times you want me to remind you to stand up?", voice, engine)
reminder_choice = voice_handler.get_audio()
voice_handler.speak("I will remind you " + reminder_choice + " times today, OK?", voice, engine)

print(reminder_choice)

acceptance = voice_handler.get_audio()

if "yes" in acceptance:
    reminder_times = int(reminder_choice)
    voice_handler.speak("Reminder times are now set. You will receive a reminder in one hour.", voice, engine)
else:
    voice_handler.speak("Please restart me in order to choose another number. I am still not that complicated", voice. engine)
    sys.exit()

print("Starting...")

while reminder_times > 0:
    sleep(60*60) # every hour, but you can make it configurable
    voice_handler.speak("Stand up... Walk with me!", voice, engine)
    voice_handler.speak("Stand up... Look away from the screen!", voice, engine)
    voice_handler.speak("Stand up... Take the much needed break, now!", voice, engine)
    reminder_times -= 1
