# Speech recognition system (Speech to text conversion)
import speech_recognition as sr

# This initializes the recognizer (The "Brain")
recognizer = sr.Recognizer()

# Seconds of nonspeaking audio before it stops and considers the sentence complete. 
recognizer.pause_threshold = 1.8
# Seconds of speaking audio before it considers the sentence complete. 
recognizer.phrase_threshold = 0.3
# Seconds of non-speaking audio allowed after speech before cutting off
recognizer.non_speaking_duration = 0.8


# This accesses the Microphone 
with sr.Microphone() as source:
    print("\n--- Speech Recognition system Active ---")
    print("Adjusting for background noise... (please stay quiet)")
    
    # This adjusts for ambient noise to improve recognition accuracy
    recognizer.adjust_for_ambient_noise(source, duration=3)
    
    print("Ready! Please say a sentence:")
    
    try:
        audio_data = recognizer.listen(source, timeout=5, phrase_time_limit=12)
        print("Processing sound...")
    except sr.WaitTimeoutError:
        print("Error: No speech detected within 5 seconds. System exiting.")
        exit()

    try:
        # This converts the audio to text using Google's Web Speech API (requires internet connection)
        text = recognizer.recognize_google(audio_data)
        
        # This calculates the word count by splitting the recognized text into words and counting them to make sure it falls within the 3-10 word requirement
        word_count = len(text.split())
        
        print(f"\nSUCCESS")
        print(f"Recognized Text: {text}")
        print(f"Word Count: {word_count}")
        
    except sr.UnknownValueError:
        print("Error: Unable to recognize speech.")
    except sr.RequestError:
        print("Error: Could not reach the speech recognition service (check internet connection).")

