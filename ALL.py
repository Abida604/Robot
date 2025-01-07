import speech_recognition as sr
listener = sr.Recognizer()
with sr.Microphone() as source:
    voice = listener.listen(source)
    command= listener.recognize_google(voice)
    print(command)
    
import pyttsx3
def speak(text):
    speaker = pyttsx3.init()
    speaker.setProperty('rate',150)
    voices= speaker.getProperty('voices')
    speaker.setProperty('voice',voices[1].id)
    speaker.say(text)
    speaker.runAndWait()
if __name__=="__main__":
    a= "hello"
    speak(a) 

import speech_recognition as sr
listener = sr.Recognizer()
with sr.Microphone() as source:
    voice = listener.listen(source)
    command=listener.recognize_google(voice)
    print(command)
import pyttsx3
def speak(text):
    speaker = pyttsx3.init()
    speaker.setProperty('rate',150)
    voices=speaker.getProperty('voices')
    speaker.setProperty('voice',voices[0].id)
    speaker.say(text)
    speaker.runAndWait()
        
if _name=="_main":
    a="hello hi how are you"
    speak(a)


import pygame
import os
def play_mp3(file_path):
    pygame.mixer.init()
    if not os.path.exists(file_path):
        print(f"The file {file_path} does not exist.")
        return
    try:
        # Load and play the MP3 file
        pygame.mixer.music.load(file_path)
        print(f"Playing {os.path.basename(file_path)}...")
        pygame.mixer.music.play()
        
        #Wait for the music to finish playing
        while pygame.mixer.music.get_busy():
            continue
    except Expectation as e:
        print(f"An error occurred while playing the file: {e}")
    finally:
        # Stop the music and quit pygame mixer
        pygame.mixer.music.stop()
        pygame.mixer.quit()
       
if __name__=="__main__" :
    mp3_file_path = r"C:\Users\ironm\Downloads\Unstoppable(Pagal-World.Com.In).mp3"
    play_mp3(mp3_file_path)       
    

import pyttsx3
import requests
import speech_recognition as sr

# Initialize the text-to-speech engine
speaker = pyttsx3.init()

# Set speech rate and voice (optional)
speaker.setProperty('rate', 130)  # Adjust the rate to your preference
voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[1].id)  # Change index for different voices

# Your OpenWeatherMap API key
API_KEY = '3ec136d4c475adee4efe3c3219d70892'
WEATHER_URL = 'http://api.openweathermap.org/data/2.5/weather'

# Initialize speech recognizer
recognizer = sr.Recognizer()

def speak(text):
    """Function to speak out the given text."""
    speaker.say(text)
    speaker.runAndWait()

def get_weather(city):
    """Fetches the weather information for a given city."""
    try:
        params = {
            'q': city,
            'appid': API_KEY,
            'units': 'metric'
        }
        response = requests.get(WEATHER_URL, params=params)
        data = response.json()

        if data['cod'] == 200:
            city_name = data['name']
            weather_desc = data['weather'][0]['description']
            temp = data['main']['temp']
            report = f"The weather in {city_name} is currently {weather_desc} with a temperature of {temp} degrees Celsius."
            return report
        else:
            return "Sorry, I couldn't get the weather information for that location."
    except Exception as e:
        print(f'An error occurred while fetching weather information: {e}')
        return "Sorry, I couldn't get the weather information."

def listen_for_city():
    """Listen for the city name from the user."""
    with sr.Microphone() as source:
        print("Listening for city name...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        
        try:
            city_name = recognizer.recognize_google(audio)
            print(f"City name received: {city_name}")
            return city_name
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            speak("Sorry, I did not understand that.")
            return None
        except sr.RequestError:
            print("Sorry, there was a problem with the request.")
            speak("Sorry, there was a problem with the request.")
            return None

if __name__== '__main__':
    speak("Please tell me the name of the city you want the weather for.")
    city = listen_for_city()
    
    if city:
        weather_report = get_weather(city)
        print(weather_report)
        speak(weather_report)
    else:
        speak("Unable to get the city name.")  
        
import pyttsx3
import PyPDF2

def speak(text):
    speaker = pyttsx3.init()
    speaker.setProperty('rate',150)
    voices = speaker.getProperty('voices')
    speaker.setProperty('voice',voices[1].id)
    speaker.say(text)
    speaker.runAndWait()
    
def read_pdf(file_path):
    try:
        # Open the PDF file
        with open(file_path, 'rb') as pdf_file:
            pdf_reader =PyPDF2.PdfReader(pdf_file)
            
            # Iterate through the pages and read texts
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text= page.extract_text()
                print(f"Reading page {page_num + 1}...")
                speak(text)
    except Exception as e:
        print(f"An error occurred: {e}")
        speak("Sorry, I couldn't read the PDF file.") 

if __name__=="__main__":
    pdf_file_path = r"C:\Users\ironm\OneDrive\Attachments\.ipynb_checkpoints\ROBOTICS.pdf"
    read_pdf(pdf_file_path)           

import pyttsx3
import requests
import speech_recognition as sr

# Initialize the text-to-speech engine
speaker = pyttsx3.init()

# Set speech rate and voice (optional)
speaker.setProperty('rate', 130)  # Adjust the rate to your preference
voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[1].id)  # Change index for different voices

# DuckDuckGo Instant Answer API URL
DUCKDUCKGO_URL = 'https://api.duckduckgo.com/'

# Initialize the recognizer for speech recognition
listener = sr.Recognizer()

def speak(text):
    """Function to speak out the given text."""
    speaker.say(text)
    speaker.runAndWait()

def truncate_text(text, word_limit=30):
    """Truncates the text to a specified number of words."""
    words = text.split()
    if len(words) > word_limit:
        return ' '.join(words[:word_limit]) + '...'
    return text

def search_duckduckgo(query):
    """Searches DuckDuckGo for a given query and returns the abstract of the result."""
    try:
        params = {
            'q': query,
            'format': 'json',
            'no_redirect': '1',
            'no_html': '1',
            'skip_disambig': '1'
        }
        response = requests.get(DUCKDUCKGO_URL, params=params)
        data = response.json()
        
        if 'AbstractText' in data and data['AbstractText']:
            return truncate_text(data['AbstractText'])
        elif 'RelatedTopics' in data and data['RelatedTopics']:
            # Get the first related topic's text if available
            return truncate_text(data['RelatedTopics'][0]['Text'])
        else:
            return "Sorry, I couldn't find any relevant information."
    except Exception as e:
        print(f'An error occurred while searching: {e}')
        return "Sorry, I couldn't complete the search."

def listen_for_command():
    """Listens for voice input and returns it as text."""
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            return command
    except sr.UnknownValueError:
        return ''
    except sr.RequestError:
        return ''
    except Exception as e:
        print(f'An error occurred while listening: {e}')
        return ''

if __name__ == '__main__':
    # Start with a prompt
    speak("Please tell me what you want to search.")
    query = listen_for_command()
    if query:
        print(f"Searching for: {query}")
        result = search_duckduckgo(query)
        print(result)
        speak(result)
    else:
        speak("Sorry, I didn't catch that. Please try again.")        