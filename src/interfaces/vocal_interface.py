from src.interfaces.interface_device import InterfaceDevice

import speech_recognition as sr
import pyttsx3


class VocalIO(InterfaceDevice):
    """Get commands through talking"""

    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.speaker = pyttsx3.init()
        self.voices = self.speaker.getProperty("voices")
        self.speaker.setProperty("voice", self.voices[11].id)

    def get_input(self) -> str:
        while True:
            with sr.Microphone() as source:
                self.recognizer.adjust_for_ambient_noise(source, duration=0.2)
                audio = self.recognizer.listen(source)

            try:
                command = self.recognizer.recognize_google(audio).lower()
                if command is not None:
                    print("\a")
                    return command

            except sr.UnknownValueError:
                self.send_output("Repeat please")

            except sr.RequestError:
                self.send_output("Can't connect to recognition server")

    def send_output(self, msg: str):
        self.speaker.say(msg)
        self.speaker.runAndWait()
