import random


inputs = {"hallo" : "hello", "katze" : "cat"}

def recover():
	with open("words", "r") as f:
		for line in f:
			(key, value) = line.split()
			inputs[key] = value

def safe():
	file = open("words", "w")
	for keys in inputs:
		file.write("\n" + keys + " " + inputs[keys])

def newwords():
    while True:
        german = input("German word: ")
        if german == "#finish":
            return
        english = input ("English word: ")
        if english == "#finish":
            return
        inputs[german] = english

def query():
    while True:
        rk = random.choice(list(inputs))
        english = input("English translation from " + rk + ": ")
        if english == "#finish":
            return
        if inputs[rk] == english:
            print("Correct!")
        else:
            print("False! Right answer: " + inputs[rk])

def printall():
    for keys in inputs:
        print("{0} - {1}".format( keys, inputs[keys]))



recover()

while True:

    command = input("Command> ")
    if command == "newwords":
        newwords()
    elif command == "query":
        query()
    elif command == "output":
        printall()
    elif command == "#finish":
        safe()
        break

