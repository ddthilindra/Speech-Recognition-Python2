import speech_recognition as sr
import pyttsx3

#Intialize the recognizer
r = sr.Recognizer()

#Function to convert text to speech
def SpeakText(cmd):

        #Initialize the engine
    engine = pyttsx3.init()
    engine.say(cmd)
    engine.runAndWait()

##SpeakText('Hello world')

#use the microphone as source  or input.
with sr.Microphone() as source2:
        # wait for a second to let the recognizer
        # adjust the energy threshold based on
        # the surrounding noise Level

    print("Silence please, calibrating background noise")
    r.adjust_for_ambient_noise(source2,duration=2)
    print("Calibrated, now spealk...")

    #Listen for the user's input
    audio2=r.listen(source2)

    #Using google to recognize audio
    MyText = r.recognize_google(audio2)
    MyText =MyText.lower()
    print("Did you say '"+MyText+"'")
    SpeakText(MyText)
