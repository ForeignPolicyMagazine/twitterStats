#!/usr/bin/env python
# twitterStats.py
# Tracks a group of Twitter user's stats and saves to csv
# Based on Tony Papousek's twitterStats.rb

# Copyright (C) Foreign Policy.


import csv, tweepy, os.path, time, sys

def print_line():
            print "======================================================================"


def save_stats(savePath):
    print "Saving to " + savePath + "..."
    if os.path.isfile(savePath):
        fileBuffer = open(savePath, 'ab')
        try:
            writer = csv.writer(fileBuffer, quoting=csv.QUOTE_NONNUMERIC)
            writer.writerow((realName, user.screen_name, str(user.statuses_count), str(user.followers_count), formattedTime))
        finally:
            fileBuffer.close()
    else:
        # Writes data to new file
        fileBuffer = open(savePath, 'wb')
        try:
            writer = csv.writer(fileBuffer, quoting=csv.QUOTE_NONNUMERIC)
            writer.writerow(('Name', 'Twitter Handle', 'Tweets', 'Followers', 'Time'))
            writer.writerow((realName, user.screen_name, str(user.statuses_count), str(user.followers_count), formattedTime))
        finally:
            fileBuffer.close()

# Clear Display
os.system('cls' if os.name == 'nt' else 'clear')

formattedTime = time.strftime("%a-%b.%e.%Y-%I.%M.%S%p-Eastern", time.localtime())
print_line()
print "twitterStats.py\nTrack a user's Twitter stats and saves them to a file.\n"

print "Current Time: " + formattedTime + "\n"


print "Connecting to Twitter..."


#
# Enter Twitter api key here. Do NOT push back to GitHub
# Register at https://dev.twitter.com/
#

consumer_key = ''
consumer_secret = ''

access_token = ''
access_token_secret = ''


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


api = tweepy.API(auth)

print "Twitter variables set!"
print_line()



with open(str(sys.argv[1]), 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:

        twitterHandle = row[0]
        user = api.get_user(twitterHandle)
        realName = row[1]
        print "Name: " + realName
        print "Twitter Handle: " + user.screen_name
        print "Followers: " + str(user.followers_count)
        "Preparing to save..."
        masterPath = 'data/twitterData-all.csv'
        save_stats(masterPath)
        timePath = 'data/twitterData-' + formattedTime + '.csv'
        save_stats(timePath)
        print_line()

