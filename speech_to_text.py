from threading import Thread


def google_search(name):
    # import library:
    import webbrowser
    webbrowser.open(f"https://www.google.com/search?q={name}")


def input_text():
    """
    import library:
    pip install SpeechRecognition
    OR
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
            print("thanks ಠ_ಠ")

            try:
                # using google speech recognition
                print(f"Text: {recorder.recognize_google(audio_text)} ")
                return recorder.recognize_google(audio_text)
            except sr.UnknownValueError:
                print("Sorry, I did not get that, please try again.")


def translate(name):
    """
    import library:
    pip install googletrans
    """
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


def speech(name="BLOB"):
    """
    import library:
    pip install pywin32
    """
    import win32com.client as wincl
    speak = wincl.Dispatch("SAPI.SpVoice")
    speak.Speak(name)


def to_text_file(title="1", text="None"):
    with open(f"{title}.txt", "a+") as f:
        f.write(text)


def main_gui():
    import pyglet

    animation = pyglet.image.load_animation('BLOB.gif')
    animSprite = pyglet.sprite.Sprite(animation)

    w = animSprite.width
    h = animSprite.height

    window = pyglet.window.Window(width=w, height=h)

    r, g, b, alpha = 0.5, 0.5, 0.8, 0.5

    pyglet.gl.glClearColor(r, g, b, alpha)

    @window.event
    def on_draw():
        window.clear()
        animSprite.draw()

    pyglet.app.run()


if __name__ == "__main__":
    p1 = Thread(target=main_gui)
    p2 = Thread(target=input_text)
    p3 = Thread(target=speech)
    p4 = Thread(target=translate)
    p5 = Thread(target=to_text_file)

    p1.start()
    x = p2.start()
    p3.start()

    # T = input_text()
    # search_name = input_text()
    # google_search(search_name)
    # translate(search_name)
    # speech("nigger")
    # to_text_file(T, search_name)
