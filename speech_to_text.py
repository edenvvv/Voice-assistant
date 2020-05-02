def google_search(name):
    # import library:
    import webbrowser
    webbrowser.open(f"https://www.google.com/search?q={name}")


def input_text():
    """
    import library:
    pip install pipwin
    pipwin install pyaudio
    """
    import speech_recognition as sr
    # Initialize recognizer class (for recognizing the speech)
    r = sr.Recognizer()
    # Reading Microphone as source
    # listening the speech and store in audio_text variable
    with sr.Microphone() as source:
        print("Talk please")
        audio_text = r.listen(source)
        print("thanks ╰(*°▽°*)╯")

        while True:
            try:
                # using google speech recognition
                print(f"Text: {r.recognize_google(audio_text)} ")
                return r.recognize_google(audio_text)
            except sr.UnknownValueError:
                print("Sorry, I did not get that, please try again.")


if __name__ == "__main__":
    search_name = input_text()
    google_search(search_name)
