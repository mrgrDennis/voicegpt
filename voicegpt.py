import speech_recognition as sr
import openai
import pyttsx3

# configure OpenAI API key and engine for text-to-speech
openai.api_key = "your_api_key_here"
engine = pyttsx3.init()

# function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# function to listen for specific word
def listen_for_word(word):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(f"Say {word}...")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print(f"You said: {text}")
        if word in text.lower():
            return True
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
    return False

# main function to prompt OpenAI API and speak response
def prompt_openai_api():
    prompt = input("What do you want to ask OpenAI? ")
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=60,
        n=1,
        stop=None,
        temperature=0.7,
    )
    speak(response.choices[0].text)

# example usage
word_spoken = False
while not word_spoken:
    word_spoken = listen_for_word("stop")
    if not word_spoken:
        prompt_openai_api()
