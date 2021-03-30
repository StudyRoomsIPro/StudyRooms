import json
from urllib.request import Request, urlopen

url="https://pop.weclarify.com/data/ssb.iit.edu_Fall2021.json"
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read().decode('utf-8')
data = json.loads(webpage)

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

                    
with open('f2021Info.json', 'w') as json_file:
    json.dump(finalDict, json_file, indent=2)
