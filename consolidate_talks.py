#!/usr/bin/env/python3

# Usage: python consolidate_talks.py
# Will only show talks that more than one person is attending.

import urllib.request
from collections import Counter
import json

friend_ids = {
              "your_name":'your unique halfnarp string',
              "your_friend":'their unique halfnarp string',
              "ccc_buddy":'and so on'
              }
# dict of all talks each person is attending
all_talks = {}
# list of all talks each person is attending, with duplicates
big_list = []
# get all the data from the halfnarp API
every_info = urllib.request.urlopen("https://halfnarp.events.ccc.de/-/talkpreferences").read().decode("utf-8")
info_json = json.loads(every_info)

for name in friend_ids.keys():
    chosen_talks = urllib.request.urlopen("https://halfnarp.events.ccc.de/-/talkpreferences/public/" + friend_ids[name]).read()
    info_dict = chosen_talks.decode("utf-8")
    info_dict = json.loads(info_dict)
    all_talks[name] = info_dict["talk_ids"]

for name in all_talks.keys():
   big_list.extend(all_talks[name]) 
# time to count how many people are going to what
c = Counter(big_list).most_common(len(big_list))
# now we check who has those talks in their lists
# this is not optimized. at all.
for item in c:
    if item[1] > 1:
        for event in info_json:
            if item[0] == event["event_id"]:
                print('%s : %d' %(event["title"], item[1]))
                print("Attending: ")
                for name in all_talks.keys():
                    if item[0] in all_talks[name]:
                        print(name)
                print()
