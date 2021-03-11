import json

with open('s2021.json') as f:
    data = json.load(f)

finalDict = {} #contains all rooms and their occupied times
allRooms = []

for clas in data:#'clas' is a dictionary
    if clas["is_offered"] == True:
        for section in clas["semesters"][0]['sections']:#'section' is a list
            campus = section['campus']
            for meeting in section['meetings']:#'meeting' is a dictionary
                if not meeting['where'] == 'TBA': 
                    room = meeting['where'] #room name in the format of 'building name room number"

                    allRooms.append(room) #could be useful

                    lst = []
                    lst.append(meeting['days'])
                    lst.append(meeting['time'])

                    if room in finalDict.keys():
                        finalDict[room]['scheduled'].append(lst)
                    else:
                        finalDict[room] = {'scheduled': [lst]}

                    finalDict[room]['campus'] = campus
            
for key in finalDict.keys():
    temp = key.rsplit(' ', 1)
    building = temp[0]
    roomNumber = temp[1]
    finalDict[key]['building'] = building
    finalDict[key]['room_number'] = roomNumber

                    
with open('roomInfo.json', 'w') as json_file:
    json.dump(finalDict, json_file, indent=2)
