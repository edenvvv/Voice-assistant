"""
import library:
pip install pipwin
pipwin install pyaudio
"""
import speech_recognition as sr


def input_text():
    # Initialize recognizer class (for recognizing the speech)
    r = sr.Recognizer()
    # Reading Microphone as source
    # listening the speech and store in audio_text variable
    with sr.Microphone() as source:
        print("Talk please")
        audio_text = r.listen(source)
        print("thanks ╰(*°▽°*)╯")

        try:
            # using google speech recognition
            print(f"Text: {r.recognize_google(audio_text)} ")
        except sr.UnknownValueError:
            print("Sorry, I did not get that, please try again")


if __name__ == "__main__":
    input_text()
