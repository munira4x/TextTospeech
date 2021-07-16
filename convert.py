url = 'https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/f817b9d7-38b4-491a-86b7-1a0ea5888912'
apikey = 'R4KLNIlE97YzWbcdoMRQRJd_yCZWkVndMOB7Vbm0eiMS'

from ibm_watson import TextToSpeechV1 
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


apikey ='Ji5U7aNqFY7GNQy1Ae3eb2yLRXcicIS_ayweLvE1WgA1'
url ='https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/c685fde4-f9a7-44bf-b5fa-e77e3e969e54'

authenticator = IAMAuthenticator(apikey)
tts = TextToSpeechV1(authenticator = authenticator)
tts.set_service_url(url)

with open('voice.mp3' , 'wb') as audio_file:
     res = tts.recognize('Hello world' , accept='audio/mp3' , voice='en-US_AllisonV3Voice').get_result()
     audio_file.write(res.content)

with open('Hello.txt' , 'r') as f:
    text = f.readlines()
    text

with open('./voice.mp3' , 'wb') as audio_file :
    res = tts.synthesize(text, accept='audio/mp3' , voice='en-US_AllisonV3Voice').get_result()
    audio_file.write[res.content]

