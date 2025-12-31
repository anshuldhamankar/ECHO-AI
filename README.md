# ECHO AI - Personal Voice Assistant

A Python-based personal AI assistant with voice recognition and text-to-speech capabilities. ECHO AI can perform various tasks including web searches, weather updates, AI-powered responses, image generation, and system operations.

## Features

### 🎤 Voice Recognition & Speech
- Voice command recognition using Google Speech Recognition
- Text-to-speech responses using Windows SAPI
- Support for both English and Hindi interactions

### 🌐 Web & Search Operations
- Open popular websites (Google, YouTube, Facebook, Amazon, etc.)
- Google search integration
- Wikipedia information retrieval
- Spotify music search and playback
- YouTube video playback

### 🤖 AI-Powered Features
- AI-based query responses using OpenRouter API
- Image generation using Stability AI
- Computational intelligence via Wolfram Alpha
- Movie recommendations

### 📱 Communication & Social
- WhatsApp message sending
- Latest news fetching
- Weather information for any city

### 🛠️ System Operations
- System shutdown with abort functionality
- Photo gallery access
- Games folder access
- Password generation

### 🎭 Entertainment
- Joke telling (English & Hindi)
- Interactive conversations
- Compliment responses

## Installation

### Prerequisites
- Python 3.7 or higher
- Windows OS (for SAPI voice support)
- Microphone for voice input

### Required Dependencies
```bash
pip install speech-recognition
pip install pywin32
pip install wikipedia
pip install pyautogui
pip install pywhatkit
pip install requests
pip install wolframalpha
pip install pyfiglet
pip install colorama
pip install pillow
pip install smtplib
```

### API Keys Required
You'll need to obtain and configure the following API keys in the code:

1. **OpenRouter API Key** - For AI responses
2. **Stability AI API Key** - For image generation
3. **Wolfram Alpha App ID** - For computational queries
4. **News API Key** - For news fetching
5. **OpenWeatherMap API Key** - For weather information

## Setup

1. Clone or download the repository
2. Install required dependencies
3. Update API keys in the `__init__` method of the `EchoAI` class
4. Ensure your microphone is working properly
5. Run the application:
   ```bash
   python main.py
   ```

## Usage

### Voice Commands

#### Basic Interactions
- "Hi" / "Hello" - Greet ECHO
- "What can you do for me" - List available features
- "Tell me about yourself" - Learn about ECHO
- "Exit" - Close the application

#### Web & Search
- "Open [website] website" - Open popular websites
- "Search [query] on Google" - Google search
- "Search [topic] on wiki" - Wikipedia search
- "Play [song] on Spotify" - Spotify music
- "Play [video] on YouTube" - YouTube videos

#### AI Features
- "[Query] using artificial intelligence" - AI-powered responses
- "Generate [description] using image generator" - Create images
- "Calculate [math problem]" - Mathematical calculations
- "Recommend me a movie" - Get movie suggestions

#### Information & Utilities
- "What's the time" - Current time
- "Weather in [city]" - Weather information
- "Tell news" - Latest news headlines
- "Generate a password" - Secure password creation
- "Tell me a joke" - Entertainment

#### System Operations
- "Open photo gallery" - Access pictures
- "Open games" - Access games folder
- "Shutdown the system" - System shutdown
- "Abort" - Cancel shutdown

#### Communication
- "Send a WhatsApp message" - Send messages via WhatsApp

## Configuration

### File Paths
Update these paths in the code according to your system:
- Photo gallery path: `C:\Users\ASUS\Pictures`
- Games folder path: `D:\GAMES`
- Output directory for images: `C:\Users\ASUS\Desktop\Resp`

### API Configuration
Replace placeholder API keys with your actual keys:
```python
self.openrouter_api_key = "your_openrouter_key"
self.stability_api_key = "your_stability_key"
self.wolfram_app_id = "your_wolfram_id"
self.news_api_key = "your_news_key"
self.weather_api_key = "your_weather_key"
```

## Output Directories

The application creates the following directories:
- `OpenRouterResponses/` - Stores AI response logs
- `Resp/` (on Desktop) - Stores generated images

## Troubleshooting

### Common Issues
1. **Microphone not working**: Ensure microphone permissions are granted
2. **API errors**: Verify API keys are valid and have sufficient credits
3. **Voice recognition fails**: Check internet connection for Google Speech Recognition
4. **Module import errors**: Install missing dependencies using pip

### Voice Input Alternative
Uncomment the line `query=input()` in `take_user_input()` method to use text input instead of voice.

## Contributing

Feel free to contribute to this project by:
- Adding new features
- Improving existing functionality
- Fixing bugs
- Enhancing documentation

## License

This project is open source. Please ensure you comply with the terms of service for all integrated APIs.

## Author

Created by ANSHUL

## Version

Current Version: 1.0

---

**Note**: This application requires active internet connection for most features including voice recognition, AI responses, weather data, and news fetching.