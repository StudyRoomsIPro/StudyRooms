import json

with open('s2021.json') as f:
    data = json.load(f)

finalDict = {} #contains all rooms and their occupied times
allRooms = []
lst = []

for clas in data:#'clas' is a dictionary
    if clas["is_offered"] == True:
        for section in clas["semesters"][0]['sections']:#'section' is a list
            for meeting in section['meetings']:#'meeting' is a dictionary
                if not meeting['where'] == 'TBA': 
                    room = meeting['where'] #room name in the format of 'building name room number"

                    allRooms.append(room) #could be useful

                    lst = []
                    lst.append(meeting['days'])
                    lst.append(meeting['time'])

                    if room in finalDict.keys():
                        finalDict[room].append(lst)
                    else:
                        finalDict[room] = [lst]
                    
with open('roomInfo.json', 'w') as json_file:
    json.dump(finalDict, json_file, indent=2)
