

import azure.cognitiveservices.speech as speechsdk
speech_key, service_region = "d6ef2de1bca84a48961bdf477384c176", "southeastasia"
def translation_once_from_mic():
    translation_config = speechsdk.translation.SpeechTranslationConfig(
        subscription=speech_key, region=service_region,
        speech_recognition_language='th-TH',
        target_languages=('de', 'fr', 'zh-Hans'))
        #target_languages=('de', 'fr', 'zh-Hans'))
    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
    recognizer = speechsdk.translation.TranslationRecognizer(
    translation_config=translation_config, audio_config=audio_config)
    result = recognizer.recognize_once()

    #ตรวจสอบผลลัพธ์
    if result.reason == speechsdk.ResultReason.TranslatedSpeech:
        print("""Recognized: {}
        German translation: {}
        French translation: {}
        Chinese translation: {}""".format(
            result.text, result.translations['de'],
            result.translations['fr'],
            result.translations['zh-Hans'],))
    elif result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print("Recognized: {}".format(result.text))
    elif result.reason == speechsdk.ResultReason.NoMatch:
        print("No speech could be recognized: {}".format(result.no_match_details))
    elif result.reason == speechsdk.ResultReason.Canceled:
        print("Translation canceled: {}".format(result.cancellation_details.reason))
        if result.cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(result.cancellation_details.error_details))

translation_once_from_mic()