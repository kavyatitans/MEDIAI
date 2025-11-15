#Step1a: Setup Text to Speech TTS model (gTTS & Eleven Labs)

# from gtts import gTTS

# def text_to_speech_with_gtts(input_text,output_filepath):
#     language ="en"

#     audioobj= gTTS(
#         text= input_text,
#         lang=language,
#         slow=False
#     )
#     audioobj.save(output_filepath)

# input_text = "Hi, this is AI with Kavya"
# text_to_speech_with_gtts(input_text=input_text,output_filename = "gtts_testing.mp3")
import os 
from gtts import gTTS

def text_to_speech_with_gtts_old(input_text, output_filepath):
    language = "en"

    audioobj = gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)

input_text = "Hi, this is AI with Kavya"
# text_to_speech_with_gtts_old(input_text=input_text, output_filepath="gtts_testing.mp3")

# #Step1b: Setup Text to Speech-TTS-Model with ElevenLabs
# import elevenlabs 
# from elevenlabs.client import ElevenLabs

# ELEVENLABS_API_KEY= os.environ.get("ELEVENLABS_API_KEY")

# def text_to_speech_with_elevenlabs(input_text, output_filepath):
#     client=Elevenlabs(api_key=ELEVENLABS_API_KEY)  
#     audio=client.generate(
#         text= input_text,
#         voice = "Aria",
#         output_format= "mp3_22050_32",
#         model = "eleven_turbo_v2"
#     )
#     elevenlabs.save(audio,output_filepath = "elevenlabs_testing.mp3")

from dotenv import load_dotenv


import os
import elevenlabs
from elevenlabs.client import ElevenLabs

load_dotenv()

ELEVENLABS_API_KEY = os.environ.get("ELEVEN_LABS_API_KEY")

def text_to_speech_with_elevenlabs_old(input_text, output_filepath):
    client = ElevenLabs(api_key=ELEVENLABS_API_KEY)

    audio = client.generate(
        text=input_text,
        voice="Aria",
        output_format="mp3_22050_32",
        model="eleven_turbo_v2"
    )

    # ✅ Corrected: Just pass the filename as the second argument
    elevenlabs.save(audio, output_filepath)

# Call the function
# text_to_speech_with_elevenlabs_old(input_text, "elevenlabs_testing.mp3")

#Step2: Use Model for Text Output to Voice 

import subprocess
import platform
import time
# def text_to_speech_with_gtts(input_text, output_filepath):
#     language = "en"

#     audioobj = gTTS(
#         text=input_text,
#         lang=language,
#         slow=False
#     )
#     audioobj.save(output_filepath)
#     os_name = platform.system()
#     try:
#         if os_name == "Darwin":  # macOS
#             subprocess.run(["afplay", output_filepath])

#         elif os_name == "Windows":
#             subprocess.run(["powershell", "-c", f'(New-Object Media.SoundPlayer "{output_filepath}").PlaySync();'])

#         elif os_name == "Linux":
#             subprocess.run(["aplay", output_filepath])  # Alternative: use 'mpg123' or 'ffplay'

#         else:
#             raise OSError("Unsupported operating system")

#     except Exception as e:
#         print(f"An error occurred while trying to play the audio: {e}")

# input_text = "Hi, this is AI with Kavya.... Auto Play Testing"
# text_to_speech_with_gtts(input_text=input_text, output_filepath="gtts_testing_autoplay.mp3")

# def text_to_speech_with_elevenlabs(input_text, output_filepath):
#     client = ElevenLabs(api_key=ELEVENLABS_API_KEY)

#     audio = client.generate(
#         text=input_text,
#         voice="Aria",
#         output_format="mp3_22050_32",
#         model="eleven_turbo_v2"
#     )

#     # ✅ Corrected: Just pass the filename as the second argument
#     elevenlabs.save(audio, output_filepath)
#     os_name = platform.system()

#     try:
#         if os_name == "Darwin":  # macOS
#             subprocess.run(["afplay", output_filepath])

#         elif os_name == "Windows":
#             subprocess.run(["powershell", "-c", f'(New-Object Media.SoundPlayer "{output_filepath}").PlaySync();'])

#         elif os_name == "Linux":
#             subprocess.run(["aplay", output_filepath])  # Alternative: use 'mpg123' or 'ffplay'

#         else:
#             raise OSError("Unsupported operating system")

#     except Exception as e:
#         print(f"An error occurred while trying to play the audio: {e}")
# # Call the function
# # text_to_speech_with_elevenlabs(input_text, "elevenlabs_testing.mp3")



# Improved version of step 2

def autoplay_audio(output_filepath):
    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            os.system(f"afplay '{output_filepath}'")
        elif os_name == "Windows":
            os.startfile(output_filepath)  # ✅ supports MP3!
        elif os_name == "Linux":
            os.system(f"xdg-open '{output_filepath}'")  # fallback
        else:
            raise OSError("Unsupported OS")
    except Exception as e:
        print(f"Error playing audio: {e}")


# --- gTTS Function ---
def text_to_speech_with_gtts(input_text, output_filepath):
    tts = gTTS(text=input_text, lang="en", slow=False)
    tts.save(output_filepath)
    print(f"✔ gTTS audio saved at {output_filepath}")
    #autoplay_audio(output_filepath)
    return output_filepath

# --- ElevenLabs Function ---
# def text_to_speech_with_elevenlabs(input_text, output_filepath):
#     client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
#     audio = client.generate(
#         text=input_text,
#         voice="Aria",
#         output_format="mp3_22050_32",
#         model="eleven_turbo_v2"
#     )
#     # save(audio, output_filepath)
#     elevenlabs.save(audio, output_filepath)

#     print(f"✔ ElevenLabs audio saved at {output_filepath}")
#     autoplay_audio(output_filepath)

# --- ElevenLabs Function (updated for new SDK) ---
# 

#Updated code
def text_to_speech_with_elevenlabs(input_text, output_filepath):
    # Initialize client
    client = ElevenLabs(api_key=ELEVENLABS_API_KEY)

    # Generate audio using the new API
    response = client.text_to_speech.convert(
        voice_id="pNInz6obpgDQGcFmaJgB",  # Default ElevenLabs voice ID for "Aria"
        model_id="eleven_turbo_v2",
        text=input_text
    )

    # Save streamed chunks to file
    with open(output_filepath, "wb") as f:
        for chunk in response:
            if chunk:
                f.write(chunk)

    print(f"✔ ElevenLabs audio saved at {output_filepath}")
    #autoplay_audio(output_filepath)
    return output_filepath

# --- Example usage ---
# if __name__ == "__main__":
#     input_text = "Hi, this is AI with Kavya. Let's test auto playback."

#     # Uncomment the one you want to test:
#     text_to_speech_with_gtts(input_text, "gtts_testing_autoplay_v2.mp3")
#     time.sleep(3)
#     text_to_speech_with_elevenlabs(input_text, "elevenlabs_testing_autoplay.mp3")