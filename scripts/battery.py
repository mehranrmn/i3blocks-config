#!/usr/bin/python3

#shows the capacity and status of the battery

import fontawesome as fa

CapacityPath = "/sys/class/power_supply/BAT0/capacity"
StatusPath = "/sys/class/power_supply/BAT0/status"
with open(CapacityPath,"r") as CAP:
     capacity = CAP.read().replace("\n","")
     pass
with open(StatusPath,"r") as STA:
     status = STA.read().replace("\n","")
     pass

if status == "Discharging" :
    if int(capacity) > 90:
        print(fa.icons["battery-full"]+" "+capacity+"%")
    elif 75 < int(capacity) <= 90:
        print(fa.icons["battery-three-quarters"]+" "+capacity+"%")
    elif 50 < int(capacity) <= 75:
        print(fa.icons["battery-half"]+" "+capacity+"%")
    elif 20 < int(capacity) <= 50:
        print(fa.icons["battery-quarter"]+" "+capacity+"%")
    elif int(capacity) <= 20:
         print(fa.icons["battery-empty"]+" "+capacity+"%")
else:
    print(fa.icons["plug"]+" "+capacity+"%")
