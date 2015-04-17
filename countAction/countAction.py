#! /usr/bin/python3.4


# ./refactor.py isldb.json | wc -l
# ./refactor.py isldb.json | cat -n
# ./refactor.py isldb.json result.txt | sort | uniq -c

  
import json
import sys

move_toPA = []
explorePA = []
glimpsePA = []
scoutPA = []
landPA = []
exploitPA =[]
stopPA = []

tabAction = []

def moyenne(tableau):
    return sum(tableau, 0.0) / len(tableau)

def variance(tableau):
    m=moyenne(tableau)
    return moyenne([(x-m)**2 for x in tableau])

def ecartype(tableau):
    return variance(tableau)**0.5

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
				move_toPA.append(info["data"]["cost"])
			elif tabAction[-1] == "explore":
				explorePA.append(info["data"]["cost"])
			elif tabAction[-1] == "glimpse":
				glimpsePA.append(info["data"]["cost"])
			elif tabAction[-1] == "scout":
				scoutPA.append(info["data"]["cost"])
			elif tabAction[-1] == "land":
				landPA.append(info["data"]["cost"])
			elif tabAction[-1] == "exploit":
				exploitPA.append(info["data"]["cost"])
			elif tabAction[-1] == "stop":
				stopPA.append(info["data"]["cost"])

tabAction.sort()
tabCount = {k: tabAction.count(k) for k in set(tabAction)}

for action in tabCount.keys():
	if action == "move_to":
		print(action , tabCount[action] , "| cost =" , sum(move_toPA, 0), "| ecartType =" , ecartype(move_toPA), file=out_file)
	if action == "explore":
		print(action , tabCount[action] , "| cost =" , sum(explorePA, 0), "| ecartType =" , ecartype(explorePA)  , file=out_file)
	if action == "glimpse":
		print(action , tabCount[action] , "| cost =" , sum(glimpsePA, 0), "| ecartType =" , ecartype(glimpsePA)  , file=out_file)
	if action == "scout":
		print(action , tabCount[action] , "\t| cost =" , sum(scoutPA, 0), " | ecartType =" , ecartype(scoutPA)  , file=out_file)
	if action == "land":
		print(action , tabCount[action] , "\t\t| cost =" , sum(landPA, 0), "  | ecartType =" , ecartype(landPA)  , file=out_file)
	if action == "exploit":
		print(action , tabCount[action] , "| cost =" , sum(exploitPA, 0), "| ecartType =" , ecartype(exploitPA)  , file=out_file)
	if action == "stop":
		print(action , tabCount[action] , "\t\t| cost =" , sum(stopPA, 0), "  | ecartType =" , ecartype(stopPA)  , file=out_file)






		
