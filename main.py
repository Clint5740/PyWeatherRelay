from gtts import gTTS # Text 2 Speech module. Uses Google API. Requires you to remove things marked.
from playsound import playsound # Play audio module so you don't need to manually play it.
# Only remove playsound if you don't want automated messages.

import time # this saves me from having to do time.sleep.dingus.penguin
def wait(t):
    time.sleep(t)


# CHANGE THESE VARIABLES IF YOU NEED TO
Refresh = 180 # How many seconds do you want between announcements?

from nwsapy import nwsapy # NWS API, do not touch!


nwsapy.set_user_agent("Name", "capybaradaddy@gmail.com") # REQUIRED to enter the API.
while 1 == 1:
    wait(5) # Just so it doesn't crash. Checks for anything every 5 seconds.
    Extreme = nwsapy.get_active_alerts(event = ["Tornado Warning", "Severe Thunderstorm Warning", "Extreme Wind Warning", "High Wind Warning",
                                        "Tsunami Warning", ])
    TornadoEx =  nwsapy.get_active_alerts(event = ["Tornado Warning", "Tornado Watch", "Severe Thunderstorm Warning"])
    Snow = nwsapy.get_active_alerts(event = ["Blizzard Warning", "Snow Squall Warning", "Winter Storm Warning" ]) # Snow-centric Warnings
    Moderate = nwsapy.get_active_alerts(event = ["Flood Warning", "Flash Flood Warning"]) # Non-Tornadic/Severe Warnings
    for warning in Extreme:
        print(warning.headline)
        tts = gTTS(warning.headline) # Remove if gTTS is removed
        tts.save('alert.wav') # Remove if gTTS is remove
        playsound('/Users/walkerstone/PycharmProjects/NWS/alert.wav') # Remove if playsound is removed
        wait(Refresh) # Will continue to annouce every 3 minutes. Time based in seconds, feel free to change.
