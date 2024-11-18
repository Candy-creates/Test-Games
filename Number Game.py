import random

Name = input("What is your name?\n")#Used to call user's name
print("-Tell me the answer to get a point!\n"
      "-If you get one wrong you will lose")

#---Variable---
quests = int(input("How many questions do you want to do?"))#Number of questions
prog = quests#How many questions has been done so far
pts = 0#Points earned
bad = 0#Questions wrong


keep_going = True#Main loop
while keep_going == True:
    for i in range(0, 1):
        dub = random.randint(1,2)#Picks addition or subtraction question


        if dub == (1):
            for i in range(0, 1):  # this is for add +
                tel = random.randint(1, 50)
                lar = random.randint(1, 50)
            loop = True #If the input from user is nothing this loop will turn on
            while loop == True:

                word = (str(lar) + " + " + str(tel))

                print(word)#prints question
                user = input("Answer: ")

                if user == (""):#No answer
                    print("Please enter something. X")
                    loop = True

                elif int(user) == (tel + lar):#Right answer
                    print("Good job! " + "\U0001f600")
                    prog -= 1#Substact progress meaning how much is left
                    print("You have " + str(prog) + " more questions left." )
                    pts += 1#Adds points/ right answer counter
                    keep_going = True
                    loop = False

                else:#Wrong answer
                    print(Name + "'s got it wrong. " + "\U0001F612")
                    Add = lar + tel
                    print("The correct answer was " + str(Add) + "✅")
                    print("You have " + str(prog) + " more questions left.")
                    bad += 1#Add wrong answer counter
                    keep_going = True
                    loop = False


        elif dub == 2:
            keep_going2 = True
            while keep_going2 == True:
                for i in range(0, 1):  # this is for subtract -
                    sub = random.randint(1, 50)
                    min = random.randint(1, 50)
                    if sub < min:#To prevent negative numbers
                        keep_going2 = True
                    elif sub > min:
                        keep_going2 = False

                    num = (str(sub) + " - " + str(min))

            loop2 = True
            while loop2 == True:
                print(num)
                suber = input("Answer: ")

                if suber == (""):  # No answer
                    print("Please enter something. X")
                    loop2 = True

                elif int(suber) == (sub - min):
                    print("Good job! " + "\U0001f600")
                    prog -= 1
                    print("You have " + str(prog) + " more questions left.")
                    pts += 1
                    keep_going = True
                    loop2 = False

                else:
                    print(Name + "'s got it wrong. " + "\U0001F612")
                    print("The correct answer was " + str(int(sub)-int(min)) + ".")
                    print("You have " + str(prog) + " more questions left.")
                    bad += 1
                    keep_going = True
                    loop2 = False


    if pts >= (quests):#stops loop
        keep_going = False
        print("Congrats!!!" + Name + " has gotten " + str(pts) +
              " point!!!Way to go!!! =D")
        print(Name + " got " + str(bad) + " wrong.")


# ---------------------------------------END---------------------------------------