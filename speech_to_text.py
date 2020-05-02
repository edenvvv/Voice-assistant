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
    recorder = sr.Recognizer()
    # Reading Microphone as source
    # listening the speech and store in audio_text variable
    with sr.Microphone() as source:
        while True:
            print("Talk please")
            audio_text = recorder.listen(source)
            print("thanks ╰(*°▽°*)╯")

            try:
                # using google speech recognition
                print(f"Text: {recorder.recognize_google(audio_text)} ")
                return recorder.recognize_google(audio_text)
            except sr.UnknownValueError:
                print("Sorry, I did not get that, please try again.")


def translate(name):
    from googletrans import Translator
    """
    LANGUAGES:
    import googletrans
    print(googletrans.LANGUAGES)
    """
    translator = Translator()
    # English -> Hebrew
    result = translator.translate(name, 'he', 'en')
    print(result.text)
    """
    Hebrew -> English
    result2 = translator.translate(name, 'en', 'he')
    print(result2.text)
    """
    return result.text


if __name__ == "__main__":
    search_name = input_text()
    # google_search(search_name)
    translate(search_name)
