
from gtts import gTTS # Text 2 Speech module. Uses Google API. Requires you to remove things marked.
from playsound import playsound # Play audio module so you don't need to manually play it.
# Only remove playsound if you don't want automated messages.

import time # this saves me from having to do time.sleep.dingus.penguin
def wait(t):
    time.sleep(t)

def sound():
    playsound(str(warning.areaDesc) + " " + str(warning.event) + ".wav")  # Remove if playsound is removed

# CHANGE THESE VARIABLES IF YOU NEED TO
Refresh = 180 # How many seconds do you want between announcements?

from nwsapy import nwsapy # NWS API, do not touch!


nwsapy.set_user_agent("Name", "capybaradaddy@gmail.com") # REQUIRED to enter the API.
while 1 == 1:
    wait(5) # Just so it doesn't crash. Checks for anything every 5 seconds.
    Severe = nwsapy.get_active_alerts(event = ["Tornado Warning", "Severe Thunderstorm Warning", "Extreme Wind Warning", "High Wind Warning",
                                        "Tsunami Warning","Flash Flood Warning"]) # General bad stuff.
    Tornadic =  nwsapy.get_active_alerts(event = ["Tornado Warning", "Tornado Watch", "Severe Thunderstorm Warning"]) # Spinny stuff.
    Snow = nwsapy.get_active_alerts(event = ["Blizzard Warning", "Snow Squall Warning", "Winter Storm Warning", "Winter Storm Watch", "Ice Storm Warning", "Freeze Warning", "Wind Chill Warning" ]) # Snow-centric Warnings
    Flooding = nwsapy.get_active_alerts(event = ["Flood Warning", "Flash Flood Warning"]) # Non-Tornadic/Severe Warnings
    Fire = nwsapy.get_active_alerts(event = ["Red Flag Warning", "Fire Weather Watch"]) # Fire
    for warning in Tornadic: # Change "Tornadic" to the event types of your choosing, listed above.
        print(warning.event + " for..." + warning.areaDesc + " Until")
        print(warning.headline)
        tts = gTTS(warning.event + " for..." + warning.areaDesc + " Until") # Remove if gTTS is removed

        tts.save(str(warning.areaDesc) + " " + str(warning.event) + ".wav") # Remove if gTTS is remove
        wait(1) # Will continue to annouce every 3 minutes. Time based in seconds, feel free to change.
        sound() # Remove if you don't want TTS to play.
