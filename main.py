from nwsapy import nwsapy  # NWS API, do not touch! Allows Python to interact with the National Weather Service's API.
# NWSAPy is only used for data stream. It is an extension / module. Created by Brandon Molyneaux on GitHub.
from gtts import gTTS  # Text 2 Speech module. Uses Google API. Requires you to remove things marked.
# gTTS is used for Text-To-Speech synthesis. Created by Pierre Nicolas Durette on GitHub.
from playsound import playsound  # Play audio module, so you don't need to manually play it.
# playsound is pretty self-explanatory. Created by Taylor Marks on GitHub.
import time
import os.path

def wait(t):  # I'm more suited for Lua, so this saves me from having to delete and retype stuff.
    time.sleep(t)

def filestart():
    playsound("alert" + str(WC) + ".wav")

nwsapy.set_user_agent("W4LLST0NE", "pyoeas@gmail.com")  # API Keywords to access it. Can work without it.

# This is where you will change the types of warnings.
print("Please type the warning types you are looking to annouce.")
print("Please seperate by comma, and capitalize the first letter of each type.")
print("If the type selected is invalid, please refresh the script.")
print("Example : Tornado Warning, Severe Thunderstorm Warning ")
warningtype = input("")
# Categories can be found in file types.txt

warnging = nwsapy.get_active_alerts(event=[warningtype])

warningcount = 1


# Hydrologic Outlook
types = "Alert or Update"
WC3 == WC
def run():
    global warningcount
    global WC
    global WC2
    WC2 = True
    global WC3
    if WC3 != WC:
        warningcount += 1
        wait(0.1)
    while warningcount != 0:
        warningcount = 0
        if nwsapy.get_active_alerts(type=types):
            if nwsapy.get_active_alerts(event=[warningtype]):
                for warning in warnging:
                    warningcount += 1
                    WC += 1
                    print(warning.headline)
                    tts = gTTS(warning.event + " for..." + warning.areaDesc)
                    tts.save("alert" + str(WC) + ".wav")  # Saves the .wav file for playback.
                    filestart()
                    wait(0.2)
                    warningcount -= 1
                    WC3 == WC
while 1==1:
    run()