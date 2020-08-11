
from google.cloud import texttospeech
import os


def convertTextToMp3(inputText):
    parent = os.path.abspath(os.path.join(__file__, '../..'))
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = parent + \
        '/keys/acgApiKey.json'
    client = texttospeech.TextToSpeechClient()

    synthesis_input = texttospeech.SynthesisInput(
        text=inputText)

    voice = texttospeech.VoiceSelectionParams(
        language_code='es-US',
        name='es-ES-Standard-A',
        ssml_gender=texttospeech.SsmlVoiceGender.FEMALE)

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3)

    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    with open(inputText.replace(" ", "_") + '.mp3', 'wb') as out:
        out.write(response.audio_content)
