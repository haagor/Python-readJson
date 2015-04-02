#! /usr/bin/python3.4


# ./refactor.py isldb.json | wc -l
# ./refactor.py isldb.json | cat -n
# ./refactor.py isldb.json result.txt | sort | uniq -c

  
import json
import sys

def handleToto(dico):
    print("TOTO", dico, file=out_file)

def handleTutu(dico):
    print("tutu", dico, file=out_file)

# main --------------------------
in_file = open(sys.argv[1], "r")
out_file = sys.stdout
#out_file = open(sys.argv[2], "w")

json_dict = json.load(in_file)

for info in json_dict:
	if "data" in info and "action" in info["data"]:
		print(info["data"]["action"])
	if "toto" in info:
	    handleToto(info["toto"])

