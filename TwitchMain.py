#Stan Borsh Twitch Main 
#Chatter Tracker
import json
import requests
import DatabaseFile as dbF


def getChatters(streamer):
    headers={"Content-Type":"text"}
    url = "https://tmi.twitch.tv/group/user/" + streamer + "/chatters"
    response = requests.request("GET", url, headers=headers)
    chatterData = response.json()
    return chatterData

def loadData(chatterData):
    #load broadcaster into db
    for i in range(len(chatterData['chatters']['broadcaster'])):
        dbF.insertData(chatterData['chatters']['broadcaster'][i],'broadcaster',"BROADCASTERS",chatterData['chatters']['broadcaster'][0])
    #load vips into db
    for i in range(len(chatterData['chatters']['vips'])):
        dbF.insertData(chatterData['chatters']['vips'][i],'vip',"VIPS",chatterData['chatters']['broadcaster'][0])
    #load mods into db
    for i in range(len(chatterData['chatters']['moderators'])):
        dbF.insertData(chatterData['chatters']['moderators'][i],'moderator',"MODERATORS",chatterData['chatters']['broadcaster'][0])
    #load viewers into db
    for i in range(len(chatterData['chatters']['viewers'])):
        dbF.insertData(chatterData['chatters']['viewers'][i],'viewer',"VIEWERS",chatterData['chatters']['broadcaster'][0])

def main():
    #load database
    dbF.createTable()
    
    #grab from users search/from users browser
    streamer = "atrioc"

    chatterData = getChatters(streamer)    

    print(chatterData['chatter_count'])
    print(chatterData['chatters']['broadcaster'])
    print(chatterData['chatters']['vips'])
    print(chatterData['chatters']['moderators'])
    #print(chatterData['chatters']['viewers'])

    #loadData
    loadData(chatterData)

    #combineData into USERS
    dbF.combineData()
    dbF.dupRemove()


if __name__ == '__main__':
    main()
