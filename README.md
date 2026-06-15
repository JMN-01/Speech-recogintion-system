# 🎙️ Speech recognition system (Speech-to-text converter)

## Overview
A `real-time` speech-to-text application that utilizes Python speech recognition libraries alongside a microphone stream to dynamically interpret and convert spoken audio into digital text strings.

## Requirements
- Python 3
- SpeechRecognition
- PyAudio

## Setup & Installation

Follow these steps to clone the repository, install the necessary dependencies, and execute the live application on your machine:

1. Clone the repository** to download a full copy of the project files:

```sh
  git clone https://github.com/JMN-01/speech-to-text-recognition.git
  cd speech-to-text-recognition
```
2. Change your directory to step inside the projects root workspace folder:
   
```sh
cd speech-to-text-recognition
```
3. Install dependencies using pip (ensure Python 3 is installed globally):

```sh
pip install SpeechRecognition pyaudio
```
4. Launch the application to initialize the microphone and begin real-time detection:

```sh
python speech_recognition_system.py
```
## Example


![Speech Recognition System Output Preview](Speech%20recognition%20test%201.png)


## Code Explanation
```Python
# Speech recognition system (Speech to text conversion)
import speech_recognition as sr
```

```Python
# This initializes the recognizer (The "Brain")
recognizer = sr.Recognizer()
```

```Python
# Seconds of nonspeaking audio before it stops and considers the sentence complete. 
recognizer.pause_threshold = 1.8
```

```Python
# Seconds of speaking audio before it considers the sentence complete. 
recognizer.phrase_threshold = 0.3
```

```Python
# Seconds of non-speaking audio allowed after speech before cutting off
recognizer.non_speaking_duration = 0.8
```

```Python
# This accesses the Microphone 
with sr.Microphone() as source:
    print("\n--- Speech Recognition system Active ---")
    print("Adjusting for background noise... (please stay quiet)")
```

```Python
 # This adjusts for ambient noise to improve recognition accuracy
    recognizer.adjust_for_ambient_noise(source, duration=3)
    
    print("Ready! Please say a sentence:")
    
    try:
        audio_data = recognizer.listen(source, timeout=5, phrase_time_limit=12)
        print("Processing sound...")
    except sr.WaitTimeoutError:
        print("Error: No speech detected within 5 seconds. System exiting.")
        exit()
```

```Python
# This converts the audio to text using Google's Web Speech API (requires internet connection)
    try:
        text = recognizer.recognize_google(audio_data)
```

```Python
# This calculates the word count by splitting the recognized text into words and counting them to make sure it falls within the 3-10 word requirement
        word_count = len(text.split())
        
        print(f"\nSUCCESS")
        print(f"Recognized Text: {text}")
        print(f"Word Count: {word_count}")
```

```Python
# This handles errors that may occur during the recognition process, such as unrecognizable speech or issues with the API connection.
    except sr.UnknownValueError:
        print("Error: Unable to recognize speech.")
    except sr.RequestError:
        print("Error: Could not reach the speech recognition service (check internet connection).")
```


