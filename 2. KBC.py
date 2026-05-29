"""This is replica of KBC here we can ask question give option for ans 
   and there is money price system same as KBC"""

print("WELCOME TO KBC")

questions = [
    ["question1" , "option A" , "option B" , "option C" , "option D" , "correct option's index" , 4],
    ["question2" , "option A" , "option B" , "option C" , "option D" , "correct option's index" , 3],
    ["question3" , "option A" , "option B" , "option C" , "option D" , "correct option's index" , 2],
    ["question4" , "option A" , "option B" , "option C" , "option D" , "correct option's index" , 1],
    ["question5" , "option A" , "option B" , "option C" , "option D" , "correct option's index" , 4],
    ["question6" , "option A" , "option B" , "option C" , "option D" , "correct option's index" , 3],
    ["question7" , "option A" , "option B" , "option C" , "option D" , "correct option's index" , 2],
    ["question8" , "option A" , "option B" , "option C" , "option D" , "correct option's index"],
    ["question9" , "option A" , "option B" , "option C" , "option D" , "correct option's index"],
    ["question10" , "option A" , "option B" , "option C" , "option D" , "correct option's index"],
    ["question11" , "option A" , "option B" , "option C" , "option D" , "correct option's index"],
    ["question12" , "option A" , "option B" , "option C" , "option D" , "correct option's index"],
    ["question13" , "option A" , "option B" , "option C" , "option D" , "correct option's index"],
    ["question14" , "option A" , "option B" , "option C" , "option D" , "correct option's index"],
]
# make as much as questions u need
levels = [1000 , 2000 , 3000 , 5000 , 10000 , 20000 , 40000 , 80000 , 160000 , 320000 , 640000 , 1250000 , 2500000 , 5000000 , 10000000]
money = 0
for i in range(0 , len(questions)):
    question = questions[i]
    print(f"\n\nQuestion for Rs.{levels[i]}")
    print(question[0])
    print(f"a. {question[1]}                   b. {question[2]}")
    print(f"c. {question[3]}                   c. {question[4]}")
    reply = int(input("Enter your answer (1,4) or 0 to quit: "))
    if(reply == 0):
        money = levels[i-1]
        break
    if(reply == question[-1]):
        print(f"Correct answer , you have won Rs.{levels[i]}")
        if(i == 4):
            money = 10000
        elif(i == 9):
            money = 320000
        elif(i == 14):
            money = 10000000
    else:
         print("wrong answer!")
         break
print(f"Take home Rs.{money}")