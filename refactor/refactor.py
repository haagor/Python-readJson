#! /usr/bin/python3.4


# ./refactor.py isldb.json | wc -l
# ./refactor.py isldb.json | cat -n
# ./refactor.py isldb.json result.txt | sort | uniq -c

  
import json
import sys

line = 1
exploitRess = ""
transformRess = ""

def handleLand(dico):
    print(line, dico["data"]["action"] , file=out_file, end="(")
    print("people =" + str(dico["data"]["parameters"]["people"]) + ")" , file=out_file)

def handleGlimpse_Explorer(dico):
    print(line, dico["data"]["action"] , file=out_file, end="(")
    print(str(dico["data"]["parameters"]["range"]) + "," + dico["data"]["parameters"]["direction"] + ")" , file=out_file, end=" => ")

def handleGlimpse_Engine(dico):
	i = 0
	while i < len(dico["data"]["extras"]["report"]):
		j = 0
		while j < len(dico["data"]["extras"]["report"][i]):
			print(str(dico["data"]["extras"]["report"][i][j][0]) + "(" + str(dico["data"]["extras"]["report"][i][j][1]) + ")", file=out_file, end=",")
			j = j + 1
		print(" | " ,file=out_file, end="")
		i = i + 1
	print("-)" ,file=out_file)


def handleExplore_Explorer(dico):
    print(line, dico["data"]["action"] , file=out_file, end="(")

def handleExplore_Engine(dico):
	i = 0
	while i < len(dico["data"]["extras"]["resources"]):
		print(dico["data"]["extras"]["resources"][i]["resource"] + "(" + dico["data"]["extras"]["resources"][i]["amount"] + ")",file=out_file, end=",")
		i = i + 1
	print("-)" ,file=out_file)


def handleMove_to(dico):
    print(line, dico["data"]["action"] , file=out_file, end="(")
    print(dico["data"]["parameters"]["direction"] + ")" , file=out_file)


def handleExploit_Explorer(dico):
    print(line, dico["data"]["action"] , file=out_file, end="(")
    print(dico["data"]["parameters"]["resource"] + ")" , file=out_file)


def handleExploit_Engine(dico):
	if exploitRess == resource[0] :
		global av1
		avancement[0] = avancement[0] + dico["data"]["extras"]["amount"]
	elif exploitRess == resource[1] :
		global av2
		avancement[1] = avancement[1] + dico["data"]["extras"]["amount"]
	elif exploitRess == resource[2] :
		global av3
		avancement[2] = avancement[2] + dico["data"]["extras"]["amount"]
	elif exploitRess == resource[3] :
		global av4
		avancement[3] = avancement[3] + dico["data"]["extras"]["amount"]
	elif exploitRess == resource[4] :
		global av5
		avancement[4] = avancement[4] + dico["data"]["extras"]["amount"]

def handleTransform_Explorer(dico):
    print(line, dico["data"]["action"] , file=out_file, end="(")
    print(dico["data"]["parameters"], ")" , file=out_file)

def handleTransform_Engine(dico):
	transformRess = dico["data"]["extras"]["kind"]
	if transformRess == resource[0] :
		global av1
		avancement[0] = avancement[0] + dico["data"]["extras"]["production"]
	elif transformRess == resource[1] :
		global av2
		avancement[1] = avancement[1] + dico["data"]["extras"]["production"]
	elif transformRess == resource[2] :
		global av3
		avancement[2] = avancement[2] + dico["data"]["extras"]["production"]
	elif transformRess == resource[3] :
		global av4
		avancement[3] = avancement[3] + dico["data"]["extras"]["production"]
	elif transformRess == resource[4] :
		global av5
		avancement[4] = avancement[4] + dico["data"]["extras"]["production"]


def handleScout_Explorer(dico):
    print(line, dico["data"]["action"] , file=out_file, end="(")
    print(dico["data"]["parameters"]["direction"] + ")" , file=out_file, end=" => ")

def handleScout_Engine(dico):
	i = 0
	while i < len(dico["data"]["extras"]["resources"]):
		print(dico["data"]["extras"]["resources"][i] ,file=out_file, end=",")
		i = i + 1
	print(dico["data"]["extras"]["altitude"], "-)" ,file=out_file)


resource = [0]*5
objectif = [0]*5
avancement = [0]*5


# main --------------------------
in_file = open(sys.argv[1], "r")
#out_file = sys.stdout
out_file = open(sys.argv[2], "w")

json_dict = json.load(in_file)

for info in json_dict:
	#init
	if "data" in info and "objective" in info["data"]:
		i = 0
		while i < len(info["data"]["objective"]):
			if i == 0:
				resource[0] = info["data"]["objective"][i]["resource"]
				objectif[0] = info["data"]["objective"][i]["amount"]
				i = i + 1
			elif i == 1:
				resource[1] = info["data"]["objective"][i]["resource"]
				objectif[1] = info["data"]["objective"][i]["amount"]
				i = i + 1
			elif i == 2:
				resource[2] = info["data"]["objective"][i]["resource"]
				objectif[2] = info["data"]["objective"][i]["amount"]
				i = i + 1
			elif i == 3:
				resource[3] = info["data"]["objective"][i]["resource"]
				objectif[3] = info["data"]["objective"][i]["amount"]
				i = i + 1
			elif i == 4:
				resource[4] = info["data"]["objective"][i]["resource"]
				objectif[4] = info["data"]["objective"][i]["amount"]
				i = i + 1
			

	# part: EXPLORER
	if "data" in info and "action" in info["data"]: 
		#action : LAND
		if info["data"]["action"] == "land":
			handleLand(info)
			line = line + 1
		#action : GLIMPSE
		if info["data"]["action"] == "glimpse":
			handleGlimpse_Explorer(info)
			line = line + 1
		#action : EXPLORE
		if info["data"]["action"] == "explore":
			handleExplore_Explorer(info)
			line = line + 1
		#action : MOVE_TO
		if info["data"]["action"] == "move_to":
			handleMove_to(info)
			line = line + 1
		#action : EXPLOIT
		if info["data"]["action"] == "exploit":
			handleExploit_Explorer(info)
			line = line + 1
			exploitRess	= info["data"]["parameters"]["resource"]
		#action : SCOUT
		if info["data"]["action"] == "scout":
			handleScout_Explorer(info)
			line = line + 1
		#action : TRANSFORM
		if info["data"]["action"] == "transform":
			handleTransform_Explorer(info)
			line = line + 1

	# part: EXPLORE_EXPLOIT
	if ("data" in info and "extras" in info["data"] and "amount" in info["data"]["extras"]):
		handleExploit_Engine(info)
	# part: EXPLORE_ENGINE
	if ("data" in info and "extras" in info["data"] and "resources" in info["data"]["extras"] and not("altitude" in info["data"]["extras"])):
		handleExplore_Engine(info)
	# part: SCOUT_ENGINE
	if ("data" in info and "extras" in info["data"] and "resources" in info["data"]["extras"] and "altitude" in info["data"]["extras"]):
		handleScout_Engine(info)
	# part: GLIMPSE_ENGINE
	if ("data" in info and "extras" in info["data"] and "report" in info["data"]["extras"]):
		handleGlimpse_Engine(info)
	# part: TRANSFORM_ENGINE
	if ("data" in info and "extras" in info["data"] and "production" in info["data"]["extras"]):
		handleTransform_Engine(info)

print(resource[0], avancement[0], "/", objectif[0], "---", resource[1], avancement[1], "/", objectif[1], "---", resource[2], avancement[2], "/", objectif[2], "---", resource[3], avancement[3], "/", objectif[3], "---", resource[4], avancement[4], "/", objectif[4], "---", file=out_file)

