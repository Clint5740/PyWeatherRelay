from nwsapy import nwsapy  # NWS API, do not touch! Allows Python to interact with the National Weather Service's API.
# NWSAPy is only used for data stream. It is an extension / module. Created by Brandon Molyneaux on GitHub.
from gtts import gTTS  # Text 2 Speech module. Uses Google's API6
# gTTS is used for Text-To-Speech synthesis. Created by Pierre Nicolas Durette on GitHub.
from playsound import playsound  # Play audio module, so you don't need to manually play it.
# playsound is pretty self-explanatory. Created by Taylor Marks on GitHub.


nwsapy.set_user_agent("W4LLST0NE", "pyoeas@gmail.com")  # API Keywords to access it. Can work without it.

# This is where you will change the types of warnings.
print("Please type the warning types you are looking to announce.")
print("Please seperate by comma, and capitalize the first letter of each type.")
print("If the type selected is invalid, please refresh the script.")
print("Example : Tornado Warning, Severe Thunderstorm Warning ")
WarningType = input("Input Warning Type : ")
# Categories can be found in file types.txt
WarningNumber = 0
WarningCount = nwsapy.get_active_alerts(event=[WarningType])
types = "Alert or Update"


for warning in WarningCount:
    WarningNumber += 1
    print(warning.headline)
    tts = gTTS(warning.event + " for..." + warning.areaDesc)
    tts.save("Warning" + str(WarningNumber) + ".mp3")  # Saves the .mp3 file for playback
    playsound("Warning" + str(WarningNumber) + ".mp3")
