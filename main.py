from nwsapy import nwsapy  # NWS API, do not touch! Allows Python to interact with the National Weather Service's API.
# NWSAPy is only used for data stream. It is an extension / module. Created by Brandon Molyneaux on GitHub.
from gtts import gTTS  # Text 2 Speech module. Uses Google's API6
# gTTS is used for Text-To-Speech synthesis. Created by Pierre Nicolas Durette on GitHub.
from playsound import playsound  # Play audio module, so you don't need to manually play it.
# playsound is pretty self-explanatory. Created by Taylor Marks on GitHub.
import tkinter as tk
from tkinter import ttk


# create the root window
def player(warningco):
    for warning in warningco:
        global WarningNumber
        WarningNumber += 1
        print(warning.headline)
        tts = gTTS(warning.event + " for..." + warning.areaDesc)
        tts.save("Warning" + str(WarningNumber) + ".mp3")  # Saves the .mp3 file for playback
        playsound("Warning" + str(WarningNumber) + ".mp3")


frame = ttk.Frame(height=800, width=800)
frame.pack(fill=tk.BOTH, padx=5, pady=5)
# create a list box
langs = ("911 Telephone Outage Emergency",
         "Extreme Cold Watch",
         "High Wind Watch",
         "Small Craft Advisory For Rough Bar",
         "Administrative Message",
         "Extreme Fire Danger",
         "Hurricane Force Wind Warning",
         "Small Craft Advisory For Winds",
         "Air Quality Alert",
         "Extreme Wind Warning",
         "Hurricane Force Wind Watch",
         "Small Stream Flood Advisory",
         "Air Stagnation Advisory",
         "Fire Warning",
         "Hurricane Local Statement",
         "Snow Squall Warning",
         "Arroyo And Small Stream Flood Advisory",
         "Fire Weather Watch",
         "Hurricane Warning",
         "Special Marine Warning",
         "Ashfall Advisory",
         "Flash Flood Statement",
         "Hurricane Watch",
         "Special Weather Statement",
         "Ashfall Warning",
         "Flash Flood Warning",
         "Hydrologic Advisory",
         "Storm Surge Warning",
         "Avalanche Advisory",
         "Flash Flood Watch",
         "Hydrologic Outlook",
         "Storm Surge Watch",
         "Avalanche Warning",
         "Flood Advisory",
         "Ice Storm Warning",
         "Storm Warning",
         "Avalanche Watch",
         "Flood Statement",
         "Lake Effect Snow Advisory",
         "Storm Watch",
         "Beach Hazards Statement",
         "Flood Warning",
         "Lake Effect Snow Warning",
         "Blizzard Warning",
         "Flood Watch",
         "Lake Effect Snow Watch",
         "Tornado Warning",
         "Blizzard Watch",
         "Freeze Warning",
         "Lake Wind Advisory",
         "Tornado Watch",
         "Blowing Dust Advisory",
         "Freeze Watch",
         "Lakeshore Flood Advisory",
         "Tropical Depression Local Statement",
         "Blowing Dust Warning",
         "Freezing Fog Advisory",
         "Lakeshore Flood Statement",
         "Tropical Storm Local Statement",
         "Brisk Wind Advisory",
         "Freezing Rain Advisory",
         "Lakeshore Flood Warning",
         "Tropical Storm Warning",
         "Child Abduction Emergency",
         "Freezing Spray Advisory",
         "Lakeshore Flood Watch",
         "Tropical Storm Watch",
         "Civil Danger Warning",
         "Frost Advisory",
         "Law Enforcement Warning",
         "Tsunami Advisory",
         "Civil Emergency Message",
         "Gale Warning",
         "Local Area Emergency",
         "Tsunami Warning",
         "Coastal Flood Advisory",
         "Gale Watch",
         "Low Water Advisory",
         "Tsunami Watch",
         "Coastal Flood Statement",
         "Hard Freeze Warning",
         "Marine Weather Statement",
         "Typhoon Local Statement",
         "Coastal Flood Warning",
         "Hard Freeze Watch",
         "Nuclear Power Plant Warning",
         "Typhoon Warning",
         "Coastal Flood Watch",
         "Hazardous Materials Warning",
         "Radiological Hazard Warning",
         "Typhoon Watch",
         "Dense Fog Advisory",
         "Hazardous Seas Warning",
         "Red Flag Warning",
         "Urban And Small Stream Flood Advisory",
         "Dense Smoke Advisory",
         "Hazardous Seas Watch",
         "Rip Current Statement",
         "Volcano Warning",
         "Dust Advisory",
         "Hazardous Weather Outlook",
         "Severe Thunderstorm Warning",
         "Wind Advisory",
         "Dust Storm Warning",
         "Heat Advisory",
         "Severe Thunderstorm Watch",
         "Wind Chill Advisory",
         "Earthquake Warning",
         "Heavy Freezing Spray Warning",
         "Severe Weather Statement",
         "Wind Chill Warning",
         "Evacuation - Immediate",
         "Heavy Freezing Spray Watch",
         "Shelter In Place Warning",
         "Wind Chill Watch",
         "Excessive Heat Warning",
         "High Surf Advisory",
         "Short Term Forecast",
         "Winter Storm Warning",
         "Excessive Heat Watch",
         "High Surf Warning",
         "Small Craft Advisory",
         "Winter Storm Watch",
         "Extreme Cold Warning",
         "High Wind Warning",
         "Small Craft Advisory For Hazardous Seas",
         "Winter Weather Advisory")

var = tk.Variable(value=langs)

listbox = tk.Listbox(
    frame,
    listvariable=var,
    selectmode=tk.EXTENDED)

listbox.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)
# link a scrollbar to a list
scrollbar = ttk.Scrollbar(
    frame,
    orient=tk.VERTICAL,
    command=listbox.yview
)

listbox['yscrollcommand'] = scrollbar.set
scrollbar.pack(side=tk.LEFT, expand=False, fill=tk.Y)
nwsapy.set_user_agent("W4LLST0NE", "pyoeas@gmail.com")  # API Keywords to access it. Can work without it.


# This is where you will change the types of warnings.
def items_selected(event):
    # get selected indices
    selected_indices = listbox.curselection()
    # get selected items
    selected_warns = ",".join([listbox.get(i) for i in selected_indices])
    global WarningCount
    WarningCount = nwsapy.get_active_alerts(event=[selected_warns])


listbox.bind('<<ListboxSelect>>', items_selected)


def buttonpress():
    global WarningCount
    player(WarningCount)


start = ttk.Button(
    frame,
    text="Start",
    command=buttonpress

)

start.pack(side=tk.BOTTOM, expand=False, fill=tk.X)
# Categories can be found in file types.txt
WarningNumber = 0
print(items_selected)
frame.mainloop()

