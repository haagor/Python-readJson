#! /usr/bin/python3.4


# ./refactor.py isldb.json | wc -l
# ./refactor.py isldb.json | cat -n
# ./refactor.py isldb.json result.txt | sort | uniq -c

  
import json
import sys

move_toPA = 0
explorePA = 0
glimpsePA = 0
scoutPA = 0
landPA = 0
exploitPA =0
stopPA = 0

tabAction = []

# main --------------------------
in_file = open(sys.argv[1], "r")
#out_file = sys.stdout
out_file = open(sys.argv[2], "w")

json_dict = json.load(in_file)

for info in json_dict:
	if "data" in info:
		if "action" in info["data"]:
			tabAction.append(info["data"]["action"])
		if "cost" in info["data"]:
			if tabAction[-1] == "move_to":
				move_toPA = move_toPA + info["data"]["cost"]
			elif tabAction[-1] == "explore":
				explorePA = explorePA + info["data"]["cost"]
			elif tabAction[-1] == "glimpse":
				glimpsePA = glimpsePA + info["data"]["cost"]
			elif tabAction[-1] == "scout":
				scoutPA = scoutPA + info["data"]["cost"]
			elif tabAction[-1] == "land":
				landPA = landPA + info["data"]["cost"]
			elif tabAction[-1] == "exploit":
				exploitPA = exploitPA + info["data"]["cost"]
			elif tabAction[-1] == "stop":
				stopPA = stopPA + info["data"]["cost"]

tabAction.sort()
tabCount = {k: tabAction.count(k) for k in set(tabAction)}

for action in tabCount.keys():
	if action == "move_to":
		print(action , tabCount[action] , "| cost =" , move_toPA  , file=out_file)
	if action == "explore":
		print(action , tabCount[action] , "| cost =" , explorePA  , file=out_file)
	if action == "glimpse":
		print(action , tabCount[action] , "| cost =" , glimpsePA  , file=out_file)
	if action == "scout":
		print(action , tabCount[action] , "| cost =" , scoutPA  , file=out_file)
	if action == "land":
		print(action , tabCount[action] , "\t\t| cost =" , landPA  , file=out_file)
	if action == "exploit":
		print(action , tabCount[action] , "| cost =" , exploitPA  , file=out_file)
	if action == "stop":
		print(action , tabCount[action] , "\t\t| cost =" , stopPA  , file=out_file)






		
