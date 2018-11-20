import random
correct = 0
incorrect = 0
while True:
    numQuestions = int(input('How many questions would you like to be asked?'))
    typeQuestion = input('what type or question would you like to be asked? (Addition, Multiplication or Mixed)').upper()
    for question in range(numQuestions):
        mixType = random.randint(0, 1)
        num1 = random.randint(1, 15)
        num2 = random.randint(1,15)
        
        if typeQuestion == ("ADDITION"):
            correctAnswer = num1 + num2
            answer = int( input("what is "+str(num1)+"+"+str(num2)))
            #answer = int(input((" " +num1 + "+" + num2 + "= ")))
            if answer == correctAnswer:
                correct += 1
            else:
                incorrect += 1
        
        elif typeQuestion == ("MULTIPLICATION"):
            correctAnswer = num1 * num2
            answer = int( input("what is "+str(num1)+"x"+str(num2)))
            if answer == correctAnswer:
                correct += 1
            else:
                incorrect += 1
        
        elif typeQuestion == ("MIXED"):
            if mixType == 0:
                correctAnswer = num1 + num2
                answer = int( input("what is "+str(num1)+"+"+str(num2)))
                if answer == correctAnswer:
                    correct += 1
                else:
                    incorrect += 1
                
            
            elif mixType == 1:
                correctAnswer = num1 * num2
                answer = int( input("what is "+str(num1)+"x"+str(num2)))
                if answer == correctAnswer:
                    correct += 1
                else:
                    incorrect += 1
        
            
    playAgain = input("Would you like to play Again? (Yes or No)").upper()
    
    
        
    if playAgain == ("NO"):
        break
        
print("Correct =", correct)
print("Incorrect =", incorrect)
    