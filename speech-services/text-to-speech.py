import azure.cognitiveservices.speech as speechsdk
from dotenv import load_dotenv
import os
load_dotenv()

speech_key = os.getenv("speech_key")
service_region = os.getenv("service_region")

if speech_key is None or service_region is None:
    raise ValueError("Speech key or service region not found in environment variables")

def text_to_speech(text :str):
    try:
        speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
        speech_config.speech_synthesis_voice_name = "en-US-AvaMultilingualNeural"
        speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)
        result = speech_synthesizer.speak_text_async(text).get()
        if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
            print("Speech synthesized to speaker for text [{}]".format(text))
        elif result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = result.cancellation_details
            print("Speech synthesis canceled: {}".format(cancellation_details.reason))
            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                if cancellation_details.error_details:
                    print("Error details: {}".format(cancellation_details.error_details))
            print("Did you update the subscription info?")
    except ValueError as ve:
        print(f"ValueError occurred: {ve}")


text_to_speech("Hi Manthan")
