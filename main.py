import speech_recognition as sr
import win32com.client
import os
import webbrowser
import datetime
import random
import ctypes
import wikipedia as wiki
import time
import pyautogui
import pywhatkit
import requests
import wolframalpha
import pyfiglet
import array
import json
from colorama import init, Fore
from io import BytesIO
from PIL import Image
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class EchoAI:
    def __init__(self):
        self.speaker = win32com.client.Dispatch("SAPI.SpVoice")
        self.openrouter_api_key = ""
        self.stability_api_key = ""
        self.wolfram_app_id = "LUY8P4-LPGQRX5GVK"
        self.news_api_key = "40b18b18746d4cce8688abe08f9ec91c"
        self.weather_api_key = "30d4741c779ba94c470ca1f63045390a"
        self.output_dir = r"C:\Users\ASUS\Desktop\Resp"
        self.initialize_data()
        
    def initialize_data(self):
        self.greetings = ["hi", "hello", "hi there", "hey", "greetings", "salutations", "howdy", "welcome", "hi how are you", "hey what's up", "hola", "bonjour", "ciao", "namaste", "konnichiwa", "guten tag", "sawasdee"]
        
        self.humorous_responses = ["Hmm, that's an interesting one! Unfortunately, it's beyond my capabilities right now.", "I'm like a magician, but even I can't decode that command. Maybe try something else?", "You've stumped me with this one! Can you ask another question?", "Oops! Looks like I missed that lesson in virtual assistant school. What else can I do for you?", "Well, this is awkward. My virtual brain seems to be on vacation. Please try another command!", "Oh dear, that went over my head. Let's try a different approach, shall we?", "I'm afraid this is where my knowledge hits a roadblock. How about something else?", "Hmmm, I'm trying to be smart, but this one has me stumped. Any other requests?", "I'm a fast learner, but this command is next-level. Give me a simpler task, please!", "You found a hidden easter egg! But I'm not sure what it does. Can you try a valid command?"]
        
        self.sites = [["google", "https://www.google.co.in"], ["youtube", "https://www.youtube.com"], ["facebook", "https://www.facebook.com"], ["amazon", "https://www.amazon.in"], ["flipkart", "https://www.flipkart.com"], ["linkedin", "https://www.linkedin.com"], ["netflix", "https://www.netflix.com"], ["spotify", "https://open.spotify.com"]]
        
        self.functionality_titles = ["Operating System and Web-related Tasks", "Opening Websites", "Opening the Photo Gallery", "Opening the Games Folder", "AI-based Responses", "Generating Images", "Computational Intelligence", "Time", "Mathematical Calculations", "Web Search and Information Retrieval", "Searching on Google", "Searching on Wikipedia", "Searching on Spotify", "Sending WhatsApp Messages", "System Shutdown", "Aborting System Shutdown", "Weather Information", "Password Generation"]
        
        self.compliments = ["great job", "well done", "you nailed it", "impressive", "fantastic", "nice work", "bravo", "excellent", "you're awesome", "outstanding", "you rock", "good going", "keep it up", "you're the best", "kudos", "thumbs up", "superb", "you're amazing", "terrific", "spot on"]
        
        self.responses = ["Thank you!", "I appreciate that!", "Glad to hear that!", "I'm here to help!", "You're too kind!", "I'm always at your service!", "Thanks a bunch!", "It's a pleasure assisting you!", "You make my day!", "I'm delighted to be of assistance!", "You're making me blush (if I could)!", "Your feedback is motivating!", "I'm just doing my job!", "You're awesome too!", "I'm here to make things easier for you!", "Thanks for the encouragement!", "I'll keep up the good work!", "I aim to please!", "Your words mean a lot!", "I'm here to make your life better!"]
        
        self.abusive_words = ["fuck", "shit", "bitch", "motherfucker", "ass"]
        
        self.english_jokes = ["Why don't scientists trust atoms? Because they make up everything!", "Did you hear about the mathematician who's afraid of negative numbers? He'll stop at nothing to avoid them!", "Why don't skeletons fight each other? They don't have the guts!", "Why don't oysters donate to charity? Because they are shellfish!", "What did one wall say to the other wall? I'll meet you at the corner!", "Why don't eggs tell jokes? Because they might crack up!", "Why did the scarecrow win an award? Because he was outstanding in his field!", "What do you call fake spaghetti? An impasta!", "Why did the tomato turn red? Because it saw the salad dressing!", "How do you organize a space party? You planet!"]
        
        self.hindi_jokes = ["एक आदमी दूसरे आदमी से: तेरी बीवी मेरे लिए बहुत खतरनाक साबित हुई है, पिछले साल तो इंसानों की संख्या 2 से घट गई।", "एक बच्चा: तू कहां रहता है? दूसरा बच्चा: पीछे मोदी जी के बगीचे में. बच्चा: वाह! वहां पर कैसी सुरक्षा होती है? दूसरा बच्चा: अरे नहीं यार, वहीं तो बगीचे की खुरपीयां और पौधे होते हैं।"]

    def display_welcome(self):
        init(autoreset=True)
        figlet_text = pyfiglet.figlet_format("E  C  H  O", font="slant")
        colored_text = Fore.BLUE + figlet_text
        print(colored_text, "version:1.0")
        welcome_message = "Hi, im Echo, your personal A I"
        print(welcome_message)
        self.speaker.Speak(welcome_message)
        
        greeting = "how can i help you?"
        print(greeting)
        self.speaker.speak(greeting)

    def generate_password(self):
        MAX_LEN = 12
        DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<']
        
        COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS
        
        temp_pass = random.choice(DIGITS) + random.choice(UPCASE_CHARACTERS) + random.choice(LOCASE_CHARACTERS) + random.choice(SYMBOLS)
        
        for _ in range(MAX_LEN - 4):
            temp_pass += random.choice(COMBINED_LIST)
            
        temp_pass_list = array.array('u', temp_pass)
        random.shuffle(temp_pass_list)
        
        password = ''.join(temp_pass_list)
        print(password)
        return password

    def ai_query(self, prompt):
        api_endpoint = "https://openrouter.ai/api/v1/chat/completions"
        headers = {"Authorization": f"Bearer {self.openrouter_api_key}", "Content-Type": "application/json"}
        data = {"model": "sao10k/l3.1-euryale-70b", "messages": [{"role": "user", "content": prompt}]}
        
        response = requests.post(api_endpoint, headers=headers, data=json.dumps(data))
        
        if response.status_code == 200:
            response_json = response.json()
            response_text = response_json.get("choices", [{}])[0].get("message", {}).get("content", "")
            print(response_text)
            
            text = f"OpenRouter API response for: {prompt}\n\n***********************\n{response_text}"
            if not os.path.exists("OpenRouterResponses"):
                os.mkdir("OpenRouterResponses")
            with open(f"OpenRouterResponses/prompt-{random.randint(1, 50)}.txt", "w") as f:
                f.write(text)
        else:
            print(f"Error: {response.status_code} - {response.text}")

    def generate_image(self, prompt):
        api_url = "https://api.stability.ai/v2beta/stable-image/generate/sd3"
        data = {"prompt": prompt, "output_format": "jpeg"}
        files = {"none": ''}
        
        try:
            response = requests.post(api_url, headers={"authorization": f"Bearer {self.stability_api_key}", "accept": "image/*"}, files=files, data=data)
            
            if response.status_code == 200:
                if not os.path.exists(self.output_dir):
                    os.makedirs(self.output_dir)
                output_path = os.path.join(self.output_dir, f"{prompt}.jpeg")
                with open(output_path, 'wb') as file:
                    file.write(response.content)
                print(f"Image saved as {output_path}")
            else:
                raise Exception(f"Error: {response.status_code}, {response.json()}")
        except requests.RequestException as e:
            print(f"An error occurred: {e}")

    def computational_intelligence(self, question):
        try:
            client = wolframalpha.Client(self.wolfram_app_id)
            answer = client.query(question)
            answer = next(answer.results).text
            print(answer)
            return answer
        except:
            self.speaker.speak("Sorry sir I couldn't fetch your question's answer. Please try again")
            return None

    def fetch_news(self, country_code='in'):
        NEWS_API_URL = 'https://newsapi.org/v2/top-headlines'
        params = {'apiKey': self.news_api_key, 'country': country_code}
        
        response = requests.get(NEWS_API_URL, params=params)
        
        if response.status_code == 200:
            news_data = response.json()
            articles = news_data['articles']
            for index, article in enumerate(articles, start=1):
                print(f"{index}. {article['title']}")
                print(f"   {article['description']}")
                print(f"   Read more: {article['url']}")
                print()
        else:
            print('Error fetching news:', response.status_code)

    def take_user_input(self):
        #query=input()  # Switch between voice and chat
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.pause_threshold = 0.7
            audio = r.listen(source)
            try:
                query = r.recognize_google(audio, language="en-in")
                query = str(query)
                print("User said:" + query)
                return str(query)
            except Exception as e:
                self.speaker.speak("Could not hear you. Please speak again.")
                print("Could not hear you. Please speak again.")
                return None

    def get_weather(self, city):
        weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={self.weather_api_key}")
        
        if weather_data.json()['cod'] == '404':
            print("No City Found")
        else:
            weather = weather_data.json()['weather'][0]['main']
            temp = round(weather_data.json()['main']['temp'])
            tempc = (temp - 32) * 5 / 9
            print(f"The weather in {city} is: {weather}")
            print(f"The temperature in {city} is: {round(tempc,2)}ºC")
            self.speaker.speak(f"The weather in {city} is: {weather}")
            self.speaker.speak(f"The temperature in {city} is: {round(tempc,2)}ºCelcius")

    def tell_joke(self):
        self.speaker.Speak("Sure! Which language do you prefer? English or Hindi?")
        language = self.take_user_input()
        
        if language and language.lower() == "english":
            joke = random.choice(self.english_jokes)
            print(joke)
            self.speaker.Speak(joke)
        elif language and language.lower() == "hindi":
            joke = random.choice(self.hindi_jokes)
            print(joke)
            self.speaker.Speak(joke)
        else:
            self.speaker.Speak("I'm sorry, I don't have jokes in that language.")

    def process_command(self, query):
        query = query.lower().replace("echo ", "")
        
        if any(word in self.abusive_words for word in query.split()):
            self.speaker.speak("Please use appropriate language.")
            return
            
        if any(query.startswith(greeting) for greeting in self.greetings):
            self.speaker.speak(random.choice(self.greetings))
            return
            
        if "what can you do for me" in query:
            self.speaker.speak("I can do many tasks for you quiet efficiently, here's a list")
            for title in self.functionality_titles:
                print(title)
                
        elif "the time" in query:
            strfTime = datetime.datetime.now().strftime("%H hours ,%M minutes ,%S seconds")
            print(strfTime)
            self.speaker.Speak(f"The time is{strfTime}")
            
        elif "open photo gallery" in query:
            self.speaker.Speak("opening gallery")
            os.system(r"start C:\Users\ASUS\Pictures")
            
        elif "open games" in query:
            self.speaker.Speak("opening games folder")
            os.system(r"start D:\GAMES")
            
        elif "exit" in query:
            self.speaker.speak("thank you.Bye")
            exit()
            
        elif "using artificial intelligence" in query:
            print("Hold on a sec, Im on it")
            self.speaker.speak("Hold on a sec, Im on it")
            self.ai_query(prompt=query)
            
        elif "search on google" in query:
            search_query = query.replace("search on google", "")
            self.speaker.speak(f"Searching {search_query}on google")
            pywhatkit.search(search_query)
            
        elif "search on wiki" in query:
            search_query = query.replace("search ", "").replace(" on wiki ", "")
            self.speaker.speak("Enlightening you,,,,,hold on")
            try:
                info = wiki.summary(search_query)
                print(info)
                ctypes.windll.user32.MessageBoxW(0, info[:4000000], search_query, 0)
                self.speaker.speak(info)
            except Exception:
                self.speaker.speak("please specify")
                print("please specify")
                
        elif "on spotify" in query:
            search_query = query.replace("play ", "").replace(" on spotify", "")
            webbrowser.open(f"https://open.spotify.com/search/{search_query}")
            pyautogui.click(x=1040, y=600)
            time.sleep(10)
            pyautogui.click(x=1040, y=600)
            self.speaker.speak(f"Playing {search_query}")
            
        elif "using image generator" in query:
            image_query = query.replace(" using image generator generate", "")
            self.speaker.speak("sure,I can do that")
            self.speaker.speak("Generated image will shortly be available in R E S P folder on the desktop")
            self.generate_image(prompt=image_query)
            
        elif "on youtube" in query:
            search_query = query.replace("play ", "").replace(" on youtube", "")
            self.speaker.speak(f"playing{search_query} on youtube")
            pywhatkit.playonyt(search_query)
            
        elif "send a whatsapp message" in query:
            self.speaker.speak("enter receivers number")
            ph_number = input()
            self.speaker.speak("enter the message you want to send")
            message = input()
            self.speaker.speak("Sending Your message, please hold on")
            pywhatkit.sendwhatmsg_instantly(ph_number, message, 10, False)
            time.sleep(10)
            self.speaker.speak("message sent successfully")
            
        elif "shutdown the system" in query:
            self.speaker.speak("Shutting down the system")
            pywhatkit.shutdown(20)
            self.speaker.speak("Shutting down the system in 20 seconds, command me if u want to abort")
            
        elif "abort" in query:
            self.speaker.speak("Aborting")
            pywhatkit.cancel_shutdown()
            self.speaker.speak("Abort successful")
            
        elif any(word in query for word in ["calculate", "when", "why", "which", "how", "what", "who", "where"]):
            self.speaker.speak("Hold on a sec")
            answer = self.computational_intelligence(query)
            if answer:
                self.speaker.speak(answer)
                
        elif "weather in" in query:
            city = query.replace("weather in ", "")
            self.get_weather(city)
            
        elif "generate a password" in query:
            password = self.generate_password()
            self.speaker.speak("Here's the password , I'll keep it a secret, I promise!!!")
            
        elif "tell me a joke" in query:
            self.tell_joke()
            
        elif "tell me about yourself" in query:
            self.speaker.speak("My Name Is Echo. Version-0.1. Created by Mr. ANSHUL")
            print("I am your virtual assistant created using Python. I am designed to perform various tasks such as speech recognition, web browsing, opening applications, answering questions, and more.")
            print("My purpose is to assist you and make your tasks easier. I can provide information from Wikipedia, search the web, play music, set reminders, and even solve math problems using Wolfram Alpha.")
            print("Feel free to ask me anything or give me commands, and I'll do my best to help you!")
            
        elif query in self.compliments:
            response = random.choice(self.responses)
            print(response)
            self.speaker.Speak(response)
            
        elif "tell news" in query:
            self.speaker.speak("Fetching news")
            self.fetch_news()
            
        elif "recommend me a movie" in query:
            self.speaker.Speak("what type of movie would you like to watch")
            movie_type = self.take_user_input()
            if movie_type:
                self.speaker.Speak("Fetching movies that you'd like. Hold on a sec")
                print("Fetching...Hold On")
                self.ai_query(prompt=f"recommend me 5 movies like {movie_type}")
                
        else:
            for site in self.sites:
                if f"open {site[0]} website" in query:
                    self.speaker.Speak(f"opening{site[0]} for you!")
                    webbrowser.open(site[1])
                    return
                    
            rand_reply = random.choice(self.humorous_responses)
            print(rand_reply)
            self.speaker.speak(rand_reply)

    def run(self):
        self.display_welcome()
        
        while True:
            print("Listening.....")
            query = self.take_user_input()
            
            if query:
                self.process_command(query)
            else:
                self.speaker.speak("Could not hear you. Please speak again.")

if __name__ == "__main__":
    echo = EchoAI()
    echo.run()
