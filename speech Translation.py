import azure.cognitiveservices.speech as speechsdk
#Creates an instance of a speech config with specified subsription key and service region.
#Replace with your own subcription key and serive region(eg:"westus").

speech_key, service_region = "YourSubscriptionKey", "YourServiceRegion"
speeach_config =speechsdk.SpeechConfig(subscription = speech_key, region =service_region)

#Creates a recognizer with the given setting 
speech_recognizer = speechsdk.SpeechRecognizer(speech_config= speeach_config)

print("Say somthing...")
#Starts speech recognition, and returns after a single utterance is recognized. 
#The end of a single utterance is determined by listening for silence at the end 
#Or until a maximum of 15 seconds of audio prcessed.
#Seconds of audio is processed, The task returns the reconginition text as a result.
#Note: Since recogize_once() return only a single utterance, it is suitable only for single.
#For long-running multi_utterance recoginition, use start_countinous_recogition()insted.

result = speech_recognizer.recognize_once()

#Checks result
if result.reason == speechsdk.ResultReason.RecognizedSpeech:
    print("Recognized: {}".format(result.text))
elif result.reason == speechsdk.ResultReason.NoMatch:
    print("No speech could be recongized: {}".format(result.no_match_details))
elif result.reason == speechsdk.ResultReason.Canceld:
    cancellation_details = result.cancellation_details
    print("Speech Recognition canceled: {}.format(cancellation_details.reason)")
    if cancellation_details.reason ==speechsdk.CancellationReason.Erro:
        print("Error details: {}".format(cancellation_details.error_details))