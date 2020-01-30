#Necessary libraries
import requests
import json
import datetime
import time

#Gets all posts ever made by a reddit account
def getPosts(user,startdate):
    accountJson = dict()

    #Get the current timestamp, and set relevant variables
    now = datetime.datetime.now().timestamp()
    increment = 2592000
    monthcount = 1

    #While the start date variable is before the now variable, request a months worth of their posts
    while startdate < now:
        url = f"https://api.pushshift.io/reddit/submission/search?author={user}&after={startdate}&before={startdate+increment}&size=1000"
        month = requests.get(url)

        #If the request was good, add data to the return dictionary, and increment the variables
        if month.ok:
            accountJson[f'{monthcount}'] = json.loads(month.content.decode('utf-8'))
            startdate += increment
            print(monthcount)
            monthcount += 1
        #Else print the error code, and try the url again
        else:
            print(f"{month.status_code}: {url}")

        #Sleep 1 second to be nice to their servers
        time.sleep(1)

    #Once data is gathered, export the dictionary to a file as a JSON
    fp = open(f'{user}_posts.json','w')
    json.dump(accountJson,fp)
    fp.close()

#It's the same function as above, but with different parameters basically (I was lazy and just copy-pasted it)
def getComments(user,startdate):
    accountJson = dict()
    now = datetime.datetime.now().timestamp()
    increment = 2592000
    monthcount = 1
    while startdate < now:
        url = f"https://api.pushshift.io/reddit/comment/search?author={user}&after={startdate}&before={startdate+increment}&size=1000"
        month = requests.get(url)
        if month.ok:
            accountJson[f'{monthcount}'] = json.loads(month.content.decode('utf-8'))
            startdate += increment
            print(monthcount)
            monthcount += 1
        else:
            print(f"{month.status_code}: {url}")
        time.sleep(1)
    fp = open(f'{user}_comments.json','w')
    json.dump(accountJson,fp)
    fp.close()

#Use the functions to get the whole account
def getAccount(user,startdate):
    getPosts(user,startdate)
    getComments(user,startdate)