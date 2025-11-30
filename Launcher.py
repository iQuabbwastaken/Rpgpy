import random
from calendar import error


def main():
	launch()


def launch():
	print("Hi there, Adventurer!")
	with open("Players.txt", "a") as file:
		lines = open("Players.txt", "r").read().split("\n")
		if lines == "":
			createPlayerFile()

		choice = input("[1] Continue / [2] New character \n")
		if choice == "2":
			createPlayerFile()

		if choice == "1":
			print("Available characters: \n")
			for i in range(len(lines)):
				print("[" + str(i) + "]" + " " +  str(lines[i]))
			choice = int(input("Which character would you like to choose? \n"))
			print("You chose: " + str(choice) + "\n" + "This is the character: " + lines[choice])



def createPlayerFile():
	playerName = input("What should i call you, adventurer? \n")
	with open(playerName + ".txt", "a") as pd:
		pd.write("playerName= "+playerName+ "DO NOT CHANGE, THIS WILL BREAK YOUR CHARACTER! \n")

	with open("Players.txt", "a") as plrs:
		plrs.write(playerName + "\n")

main()