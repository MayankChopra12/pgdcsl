import os
import pickle
import speech_recognition as sr
import pyaudio
from python_speech_features import mfcc
from scipy.io.wavfile import write

def record_and_save_voice(user_id):
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    print("Please say something for voice enrollment.")

    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    # Save the recorded audio as a WAV file
    audio_path = f"user_{user_id}.wav"
    with open(audio_path, "wb") as file:
        file.write(audio.get_wav_data())

    print(f"Voice sample saved as {audio_path}")

    # Extract MFCC features from the recorded audio
    sample_rate, signal = sr.AudioFile(audio_path).read()
    mfcc_features = mfcc(signal, sample_rate)

    # Save the MFCC features in a file
    features_path = f"user_{user_id}_features.pkl"
    with open(features_path, "wb") as file:
        pickle.dump(mfcc_features, file)

    print(f"MFCC features saved as {features_path}")

def authenticate_user(user_id):
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    print("Please say something for authentication.")

    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    # Extract MFCC features from the recorded audio
    sample_rate, signal = sr.AudioData(audio.frame_data, audio.sample_rate, audio.sample_width)
    mfcc_features = mfcc(signal, sample_rate)

    # Load the stored MFCC features from the database
    features_path = f"user_{user_id}_features.pkl"
    with open(features_path, "rb") as file:
        stored_features = pickle.load(file)

    # Compare the features (you may use a proper distance metric)
    if len(mfcc_features) == len(stored_features):
        print("Authentication successful!")
    else:
        print("Authentication failed.")

if __name__ == "__main__":
    user_id = 1

    # Uncomment the line below to enroll a new user
    # record_and_save_voice(user_id)

    # Uncomment the line below to authenticate a user
    # authenticate_user(user_id)
