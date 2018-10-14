#Aaron Alexander 101107249


	
instructions = input("would you like instructions? (yes or no) ").upper()
	
if instructions == ("YES"):
	print("\nPick a movie from the list below\n\nCHRISTMAS FILMS\nHome Alone 2\tThe Polar Express\tElf\tHow The Grinch Stole Christmas\tA Christmas Carol\nJingle All The Way\tFrosty The Snow Man\tA Charlie Brown Christmas\tThe Nightmare Before Christmas\tThe Santa Claus 2\n\nFAIRY TALES\nRapunzel\tBrave\tPrincess And The Frog\tSherk\tPuss In Boots\nAladdin\tBeauty And The Beast\tCinderella\tSnow White\tSleeping Beauty\n\nThen answer the following questions with yes and no answers, the expert system will then tell you the title of the movie.")

else:
	print()
		
run =("YES")


while run == ("YES"):

	print('\nWhat sub-genre are you selecting from? \n\nChristmas Films or Fairy Tales\n')
	movietype = input().upper()

		




#questions for christmas films
	if movietype == ("CHRISTMAS FILMS"):
		answer = input("Does the main character of the film stay in the plaza hotel? (yes or no) ").upper()

		if answer == ("YES"):
			print(""""Home Alone 2" is the film title""") 
		else:
			answer = input("Does most of the film take place on a train? (yes or no) ").upper()
			if answer == ("YES"):
				print(""""The Polar Express" is the film title""")
			else:
				answer = input("Does the film star Will Ferrel? (yes or no) ").upper()
				if answer == ("YES"):
					print(""""Elf" is the film title""")
				else:
					answer = input("Does the film star a green person? (yes or no) ").upper()
					if answer == ("YES"):
						print(""""How The Grinch Stole Christmas" is the film title""")
					else:
						answer = input("Is the main chracter stingy with his money? (yes or no) ").upper()
						if answer == ("YES"):
							print(""""A Christmas Carol" is the film title""")
						else:
							answer = input("Does the father in the film try to get an action figure? (yes or no) ").upper()
							if answer == ("YES"):
								print(""""Jingle All The Way" is the film title""")
							else:
								answer = input("Does the film star a talking snowman? (yes or no) ").upper()
								if answer == ("YES"):
									print(""""Frosty The Snow Man" is the film title""")
								else:
									answer = input("Does the film star a child name Charlie Brown? (yes or no) ").upper()
									if answer == ("YES"):
										print(""""A Charlie Brown Christmas" is the film title""")
									else:
										answer = input("Is it a Stop Motion Film? (yes or no)")
										if answer == ("YES"):
											print(""""The Nightmare Before Christmas" is the film title""")
										else:
											print(""""The Santa Clause 2" is the film title""")

	elif movietype == ("FAIRY TALES"):
		answer = input("Does the main character of the film have extremely long hair? (yes or no) ").upper()
	
		if answer == ("YES"):
			print(""""Rapunzel" is the film title""") 
		else:
			answer = input("Does the main chracter of the film have curly red hair? (yes or no) ").upper()
			if answer == ("YES"):
				print(""""Brave" is the film title""")
			else:
				answer = input("Does the film follow two frogs? (yes or no) ").upper()
				if answer == ("YES"):
					print(""""Princess And The Frog" is the film title""")
				else:
					answer = input("Does the film star an ogre? (yes or no) ").upper()
					if answer == ("YES"):
						print(""""Sherk " is the film title""")
					else:
						answer = input("Is the main chracter a cat? (yes or no) ").upper()
						if answer == ("YES"):
							print(""""Puss In Boots" is the film title""")
						else:
							answer = input("Does the movie have a genie? (yes or no) ").upper()
							if answer == ("YES"):
								print(""""Aladdin" is the film title""")
							else:
								answer = input("Is one of the main characters a beast? (yes or no) ").upper()
								if answer == ("YES"):
									print(""""Beauty And The Beast" is the film title""")
								else:
									answer = input("Does the main chracter lose a glass slipper? (yes or no) ").upper()
									if answer == ("YES"):
										print(""""Cinderella" is the film title""")
									else:
										answer = input("Is the main character poised by an apple? (yes or no)")
										if answer == ("YES"):
											print(""""Snow White" is the film title""")
										else:
											print(""""SLeeping Beauty" is the film title""")


	else:
		print("\nInvalid Input\n")
	run = input("Would you like to use this program again? (yes or no) ").upper()




