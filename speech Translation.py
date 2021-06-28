import azure.cognitiveservices.speech as speechsdk
speech_key, service_region = "#enteryourkey here", "enterthe region"
speeach_config =speechsdk.SpeechConfig(subscription = speech_key, region =service_region)

speech_recognizer = speechsdk.SpeechRecognizer(speech_config= speeach_config)
print("Say somthing...")
result = speech_recognizer.recognize_once()

if result.reason == speechsdk.ResultReason.RecognizedSpeech:
    print("Recognized: {}".format(result.text))
elif result.reason == speechsdk.ResultReason.NoMatch:
    print("No speech could be recongized: {}".format(result.no_match_details))
elif result.reason == speechsdk.ResultReason.Canceld:
    cancellation_details = result.cancellation_details
    print("Speech Recognition canceled: {}.format(cancellation_details.reason)")
    if cancellation_details.reason ==speechsdk.CancellationReason.Erro:
        print("Error details: {}".format(cancellation_details.error_details))