from threading import Thread


def google_search(name):
    # import library:
    import webbrowser
    webbrowser.open(f"https://www.google.com/search?q={name}")


def youtube_search(name):
    """
    import library:
    pip install youtube-search
    """
    import webbrowser
    from youtube_search import YoutubeSearch
    results = YoutubeSearch(name, max_results=1).to_json()
    # print(results)
    results_start = results.find("/watch?v=")  # Finds the beginning of the link
    results = results[results_start:]  # Removes the irrelevant part of the string (without link)
    results_end = results.find(',')  # Marking the end of the link
    webbrowser.open(f"https://www.youtube.com{results[:results_end]}")


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
            audio_text = recorder.listen(source)
            speech("thanks")

            try:
                # using google speech recognition
                print(f"Text: {recorder.recognize_google(audio_text)} ")
                return str(recorder.recognize_google(audio_text))
            except sr.UnknownValueError:
                speech("Sorry, I did not get that, please try again.")


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


def main_speech():
    funcs = {
        "youtube": youtube_search,
        "google": google_search,
        "translate": translate,
        "write to document": to_text_file,
    }

    try:
        speech("What do you want to do?")
        speech("You can choose a song from YouTube")
        speech("or Search Google")
        speech("Or translate to Hebrew")
        speech("Or write to document")
        speech("Or to exit")
        request = input_text().lower()
        speech("Feel free to start talking")
        func_request = input_text().lower()
        funcs[request](func_request)
    except:
        speech("Sorry, I did not get that, please try again")


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
    p2 = Thread(target=main_speech)

    p1.setDaemon(True)
    p1.start()
    p2.start()
