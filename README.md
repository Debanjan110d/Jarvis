# Jarvis Voice Assistant

This is a simple voice-activated assistant named Jarvis, created by Debanjan Dutta. It can perform various tasks like opening websites, searching the web, playing music, and providing information from Wikipedia.

## Features

-  **Open Websites**: Open popular websites like StackOverflow, Gmail, and a music library.
-  **Play Music**: Play music directly from YouTube by specifying the song name.
-  **Search the Web**: Perform a Google search for any query.
-  **Run Applications**: Run local applications on your computer.
-  **Wikipedia Information**: Get summaries from Wikipedia on any topic.

## Setup

### Prerequisites

-  Python 3.x
-  Required Python libraries (specified in `requirements.txt`)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Debanjan110d/Jarvis.git
   cd Jarvis
   ```

2. **Install the required libraries:**
   ```bash
   pip install -r requirements.txt
   ```

**Important Note:**
After running `pip install -r requirements.txt`, you may encounter an issue with pyAudio installation. To resolve this, run the following command:
`bash
    pip install pyaudio
    `

### Usage

1. **Run the script:**

   ```bash
   python main.py
   ```

2. **Interact with Jarvis:**
   -  Say "Jarvis" to wake up the assistant.
   -  Give a command, such as:
      -  "Open StackOverflow"
      -  "Play [song name]"
      -  "Search [query]"
      -  "Run [application]"
      -  "Tell me about [topic]"

### Commands

-  **Open Websites**:
   -  Example: "Open StackOverflow"
-  **Play Music**:
   -  Example: "Play Shape of You"
-  **Search the Web**:
   -  Example: "Search Python tutorials"
-  **Run Applications**:
   -  Example: "Run notepad"
-  **Wikipedia Information**:
   -  Example: "Tell me about Python programming"

## Troubleshooting

If you encounter any issues, make sure your microphone is working correctly and that you have a stable internet connection for voice recognition and web searches.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Feel free to fork the repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## Acknowledgments

-  This project uses [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) for voice recognition.
-  [Pyttsx3](https://pypi.org/project/pyttsx3/) is used for text-to-speech.
-  [Wikipedia API](https://pypi.org/project/wikipedia-api/) is used to fetch information from Wikipedia.
