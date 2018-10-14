#aaronalexander_101107249





#input instructions here
print("\n\n\n6 Ingredient Recipe Specific Batch Calculator")
print("\nINSTRUCTIONS:To Calculate Your Specific Ingredient Amounts Answers the Following Questions")




#input name and quanity of each ingredient

nameIng1 = input("\n\n\nWhat is the name of the first ingredient? ")
unitIng1 = input("What is the unit of measurement? ")
quanIng1 = float(input("What is the quantity? "))

nameIng2 = input("\nWhat is the name of the second ingredient? ")
unitIng2 = input("What is the unit of measurement? ")
quanIng2 = float(input("What is the quantity? "))

nameIng3 = input("\nWhat is the name of the third ingredient? ")
unitIng3 = input("What is the unit of measurement? ")
quanIng3 = float(input("What is the quantity? "))

nameIng4 = input("\nWhat is the name of the fourth ingredient? ")
unitIng4 = input("What is the unit of measurement? ")
quanIng4 = float(input("What is the quantity? "))

nameIng5 = input("\nWhat is the name of the fifth ingredient? ")
unitIng5 = input("What is the unit of measurement? ")
quanIng5 = float(input("What is the quantity? "))

nameIng6 = input("\nWhat is the name of the sixth ingredient? ")
unitIng6 = input("What is the unit of measurement? ")
quanIng6 = float(input("What is the quantity? "))

#about recipe
nameOfRecipe = input("\nWhat is the name of this recipe? ")
servingsPerBatch = float(input("\nHow many individual servings does this recipe make per batch? "))


requestedIndividualServings = float(input("How many individual servings would you like to make? "))

ratioReq = requestedIndividualServings/servingsPerBatch

#new quantities 
newQuanIng1 = ratioReq*quanIng1
newQuanIng2 = ratioReq*quanIng2
newQuanIng3 = ratioReq*quanIng3
newQuanIng4 = ratioReq*quanIng4
newQuanIng5 = ratioReq*quanIng5
newQuanIng6 = ratioReq*quanIng6


#calorie info
calPerBatch = int(input("\nHow many calories per batch? "))
calBatchRequested = (calPerBatch/servingsPerBatch)*requestedIndividualServings


#how much to put for requested individual servings
print("\nFor",requestedIndividualServings,"induvidual servings you need\n")







#new amounts printed
print(nameIng1,"{:.2f}".format(newQuanIng1),unitIng1)
print(nameIng2,"{:.2f}".format(newQuanIng2),unitIng2)
print(nameIng3,"{:.2f}".format(newQuanIng3),unitIng3)
print(nameIng4,"{:.2f}".format(newQuanIng4),unitIng4)
print(nameIng5,"{:.2f}".format(newQuanIng5),unitIng5)
print(nameIng6,"{:.2f}".format(newQuanIng6),unitIng6)

import math

calPerIndividual = calPerBatch/servingsPerBatch
minServingsRequired = math.ceil((2000/calPerIndividual))


print("\nFor a minimun of 2000 calories you need to eat",minServingsRequired,"individual servings\n\n")




