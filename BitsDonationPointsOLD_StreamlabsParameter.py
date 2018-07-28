# -*- coding: cp1252 -*-

#---------------------------------------
#	Import Libraries
#---------------------------------------
import clr, sys, json, os, codecs, time
clr.AddReference("IronPython.SQLite.dll")
clr.AddReference("IronPython.Modules.dll")
from ast import literal_eval


#---------------------------------------
#	[Required]	Script Information
#---------------------------------------
ScriptName = "DonationPoints"
Website = ""
Creator = "Yaz12321"
Version = "1.0"
Description = "Give points to donations: $donationpoints($amount,ratio)"

#---------------------------------------
#   Version Information
#---------------------------------------

# Version:

# > 1.0< 
    # Official Release


#---------------------------------------
# Initialize Data on Load
#---------------------------------------
def Init():

    # End of Init
    return


## TESTING: $donationpoints[$bits,1]
## Alternative Testing: $donationpoints[$username,$bits,1]

## Bits: $donationpoints[$bits,10]
## Donations: $donationpoints[$amount,10]

### Bits: $donationpoints[$username,$bits,10]
### Donations: $donationpoints[$username,$amount,10]


def donationpoints(amount,ratio): #(user,amount,ratio)
    try:

        points = int(float(amount)*float(ratio))

        return points # (user,points)
    except:

        return -1 # (user,-1)


def Parse(parseString, userid, username, targetid, targetname, message):

    if "$donationpoints" in parseString:
        stringsplit = parseString.split(" ") #.split("|")
        for i in stringsplit:
            if "$donationpoints" in i:

                donation = i.replace("$","")
                donation1 = donation.replace("[","(")
                donation2 = donation1.replace("]",")")

                P = eval(donation2)

                if P >= 0: #if P[1]>= 0:

                    added = Parent.AddPoints(userid,P) #(P[0].lower(),P[1])
                    if added:

                        parseString = parseString.replace(i,"") #Will this work?
                    else:
                        parseString = parseString + " Unable to add {} points to {}".format(P,userid)
                
                    
        return parseString
    return parseString




def Tick():
    return
