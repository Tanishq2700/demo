import time
from tabulate import tabulate

print("\n\n\n\n\t\t\t\t\t\t\tWELCOME TO COMPUTER QUIZ !")
playing = input("Do you want to play? (Yes/No): ")
if playing.upper() != "YES":
    print("KHELNA HI NAHI THA TO LAPTOP KYU LIYA ???")
    quit()
if playing.upper() == 'YES':
    print('''                   
>                                    RULES OF THE GAME\n''') 
print('''        1) You are being provided with some questions.\n''')
time.sleep(1)
print('''        2) 5 Points will be awarded for each correct answer.\n''')
time.sleep(1)
print('''        3) For every Incorrect answer 2 marks will be deducted from your score.\n''')
time.sleep(1)
print('''        4) If you submit more than 3 Incorrect answers, your game will quit automatically.\n''')
time.sleep(1)
print('''        5) You can press 'q' If you want to quit at any time\n''')
time.sleep(1)
print('''        6) If you score full marks then you will be rewarded with cash prize.💲💰 💲\n''')
time.sleep(5)

print('''> SELECT QUIZ TOPIC: \n
    1. PYTHON\n
    2. GENERAL KNOWLEDGE\n
    3. INDIA\n
    4. SCIENCE\n
    5. CURRENT AFFAIRS (HARD LEVEL)\n
    6. PICK ODD ONE OUT (BASIC LEVEL)\n''')
time.sleep(1)
a = input('Select An Option : ')

if a == '1':
        
    score = 0
    incorrect = 0
    correct = 0
    for i in range(1, 100):
        a = input('\n\nAre You Ready ? (Yes/No): ')
        if a.upper() == 'YES':
            print('\n\n\t\t\t\t\t"PYTHON QUIZ" is About To Begin in: ')
            time.sleep(1)
            print('3')
            time.sleep(1)
            print('2')
            time.sleep(1)
            print('1\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
            break 
        else:
            print('Enter "Yes" when ready')
    # # 1. ______________________________________________________________________________________________________________________________________________________________________
    table = [[ '1. What is the maximum possible length of an identifier?'],['a) 31'],['b) 63'],['c) 78'],['d) Any length']]
    print(tabulate(table, headers = 'firstrow', tablefmt = 'mixed_grid'))
    
    answer = input('Type your answer(A/B/C/D): ')
    if answer.upper() == 'D':
        print('\t\t\t\t\t\t\t\tCorrect!\n\n')
        score += 5
        correct += 1
    elif answer.lower() == 'q':
        print('Thanks for playing 😄')
        quit()
    else:
        print("\t\t\t\t\t\t\t\tIncorrect!\n\n")
        score -= 2
        incorrect += 1
    # 2. __________________________________________________________________________________________________________________________________________________________________________
    time.sleep(1)
    table = [['2. What does pip stand for python?'],['a) Pip Installs Python'],['b) Pip Installs Packages'],['c) Preferred Installer Program'],['d) All of the mentioned']]
    print(tabulate(table, headers = 'firstrow', tablefmt = 'mixed_grid'))

    answer = input('Type your answer(A/B/C/D): ')
    if answer.upper() == 'C':
        print('\t\t\t\t\t\t\t\tCorrect!\n\n')
        score += 5
        correct += 1
    elif answer.lower() == 'q':
        print('Thanks for playing 😄')
        quit()
    else:
        print("\t\t\t\t\t\t\t\tIncorrect!\n\n")
        score -= 2
        incorrect  += 1
    # 3. ________________________________________________________________________________________________________________  
    time.sleep(1)
    table = [['''3. for i in [1, 2, 3, 4][::-1]:
        print (i)''' ],['a) 4 3 2 1'],['b) Error'],['c) 1 2 3 4'], ['d) 4321']]
    print(tabulate(table, headers = 'firstrow', tablefmt = 'mixed_grid'))

    answer = input('Type your answer(A/B/C/D): ')
    if answer.upper() == 'A':
        print('\t\t\t\t\t\t\t\tCorrect!\n\n')
        score += 5
        correct += 1
    elif answer.lower() == 'q':
        print('Thanks for playing 😄')
        quit()
    else:
        print("\t\t\t\t\t\t\t\tIncorrect!\n\n")
        score -= 2
        incorrect  += 1
    if incorrect >= 3:
        print('You have given 3 incorrect answers!!')
        print("You didn't complete the quiz",',You Lose!!!')
        print('Your score is :',score)
        print("You submiited ", correct, "answers correctly")
        quit()
    #4. _______________________________________________________________________________________________________________________  
    time.sleep(1)
    table = [['4. print("abc. DEF".capitalize())'], ['a) Abc.def'],['b) abc.def'],['c) Abc.Def'],['d) ABC.DEF']]
    print(tabulate(table, headers = 'firstrow', tablefmt = 'mixed_grid'))

    answer = input('Type your answer(A/B/C/D): ')
    if answer.upper() == 'A':
        print('\t\t\t\t\t\t\t\tCorrect!\n\n')
        score += 5
        correct += 1
    elif answer.lower() == 'q':
        print('Thanks for playing 😄')
        quit()
    else:
        print("\t\t\t\t\t\t\t\tIncorrect!\n\n")
        score -= 2
        incorrect += 1
    if incorrect >= 3:
        print('You have given 3 incorrect answers!!')
        print("You didn't complete the quiz",',You Lose!!!')
        print('Your score is :',score)
        print("You submiited ", correct, "answers correctly")
        quit()
    #5. ____________________________________________________________________________________________________________________________ 
    time.sleep(1)
    table = [['''5.Which of the following Python statements will result in the output: 6? 
    A = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]'''],['a) A[2][1]'],['b) A[3][2]'],['c) A[1][2]'],['d) A[2][3]']]
    print(tabulate(table, headers = 'firstrow', tablefmt = 'mixed_grid'))

    answer = input('Type your answer(A/B/C/D): ')
    if answer.upper() == 'C':
        print('\t\t\t\t\t\t\t\tCorrect!\n\n')
        score += 5
        correct += 1
    elif answer.lower() == 'q':
        print('Thanks for playing 😄')
        quit()
    else:
        print("\t\t\t\t\t\t\t\tIncorrect!\n\n")
        score -= 2
        incorrect += 1
    if incorrect >= 3:
        print('You have given 3 incorrect answers!!')
        print("You didn't complete the quiz",',You Lose!!!')
        print('Your score is :',score)
        print("You submiited ", correct, "answers correctly")
        quit()
    #6. ____________________________________________________________________________________________________________________________
    time.sleep(1)
    table = [['''6. x = 'abcd'
    for i in range(len(x)):
        print(i)'''],['a) Error'],['b) 1 2 3 4'],['c) a b c d'],['d) 0 1 2 3']]    
    print(tabulate(table, headers = 'firstrow', tablefmt = 'mixed_grid'))
    answer = input('Type your answer(A/B/C/D): ')
    if answer.upper() == 'D':
        print('\t\t\t\t\t\t\t\tCorrect!\n\n')
        score += 5
        correct += 1
    elif answer.lower() == 'q':
        print('Thanks for playing 😄')
        quit()
    else:
        print("\t\t\t\t\t\t\t\tIncorrect!\n\n")
        score -= 2
        incorrect += 1
    if incorrect >= 3:
        print('You have given 3 incorrect answers!!')
        print("You didn't complete the quiz",',You Lose!!!')
        print('Your score is :',score)
        print("You submiited ", correct, "answers correctly")
        quit()
    #7. _____________________________________________________________________________________________________________________________
    time.sleep(1)
    table = [['7. To add a new element to a list we use which Python command?'],['a) list1.addEnd(5)'],['b) list1.addLast(5)'],['c) list1.append(5)'],['d) list1.add(5)']]
    print(tabulate(table, headers = 'firstrow', tablefmt = 'mixed_grid'))
    answer = input('Type your answer(A/B/C/D): ')
    if answer.upper() == 'C':
        print('\t\t\t\t\t\t\t\tCorrect!\n\n')
        score += 5
        correct += 1
    elif answer.lower() == 'q':
        print('Thanks for playing 😄')
        quit()
    else:
        print("\t\t\t\t\t\t\t\tIncorrect!\n\n")
        score -= 2
        incorrect += 1
    if incorrect >= 3:
        print('You have given 3 incorrect answers!!')
        print("You didn't complete the quiz",',You Lose!!!')
        print('Your score is :',score)
        print("You submiited ", correct, "answers correctly")
        quit()
#8. ______________________________________________________________________________________________________________________________
    time.sleep(1)
    table = [['8. What is the Syntax of List Comprehension ?'],['a) [item for expression in iterable if condition == True]'],['b) [expression for item in iterable if condition == True]'],['c) [for i in range(len(x))]'],['d) [print(output)]']]
    print(tabulate(table, headers = 'firstrow', tablefmt = 'mixed_grid'))
    answer = input('Type your answer(A/B/C/D): ')
    if answer.upper() == 'B':
        print('\t\t\t\t\t\t\t\tCorrect!\n\n')
        score += 5
        correct += 1
    elif answer.lower() == 'q':
        print('Thanks for playing 😄')
        quit()
    else:
        print("\t\t\t\t\t\t\t\tIncorrect!\n\n")
        score -= 2
        incorrect += 1
    if incorrect >= 3:
        print('You have given 3 incorrect answers!!')
        print("You didn't complete the quiz",',You Lose!!!')
        print('Your score is :',score)
        print("You submiited ", correct, "answers correctly")
        quit()
#9. __________________________________________________________________________________________________________
    time.sleep(1)
    table = [['9.  print(2**(3**2), (2**3)**2, 2**3**2)'],['a) 512 64 512'],['b) 512 512 512'],['c) 64 512 64'],['D) 64 64 64']]
    print(tabulate(table, headers = 'firstrow', tablefmt = 'mixed_grid'))
    answer = input('Type your answer(A/B/C/D): ')
    if answer.upper() == 'A':
        print('\t\t\t\t\t\t\t\tCorrect!\n\n')
        score += 5
        correct += 1
    elif answer.lower() == 'q':
        print('Thanks for playing 😄')
        quit()
    else:
        print("\t\t\t\t\t\t\t\tIncorrect!\n\n")
        score -= 2
        incorrect += 1
    if incorrect >= 3:
        print('You have given 3 incorrect answers!!')
        print("You didn't complete the quiz",',You Lose!!!')
        print('Your score is :',score)
        print("You submiited ", correct, "answers correctly")
        quit()
#10. __________________________________________________________________________________________________________
    time.sleep(1)
    table = [['8. Which of the following represents the bitwise XOR operator?'],['a) &'],['b) ^'],['c) |'],['d) !']]
    print(tabulate(table, headers = 'firstrow', tablefmt = 'mixed_grid'))
    answer = input('Type your answer(A/B/C/D): ')
    if answer.upper() == 'B':
        print('\t\t\t\t\t\t\t\tCorrect!\n\n')
        score += 5
        correct += 1
    elif answer.lower() == 'q':
        print('Thanks for playing 😄')
        quit()
    else:
        print("\t\t\t\t\t\t\t\tIncorrect!\n\n")
        score -= 2
        incorrect += 1
    if incorrect >= 3:
        print('You have given 3 incorrect answers!!')
        print("You didn't complete the quiz",',You Lose!!!')
        print('Your score is :',score)
        print("You submiited ", correct, "answers correctly")
        quit()

    print('''
    YOUR SCORE IS: ''', score,'/50')

    print("You submiited ", correct, "answers correctly")

    if score == 50:
        input('''
    Enter your account number for prize money: ''')
        print('''
                                                                NAHI MILENGE PAISE     
                                                        🤣 🤣 KAISA LAGA MERA MAZAK 🤣 🤣''')
if a == '2':
    score = 0
    incorrect = 0
    correct = 0
    for i in range(1, 100):
        a = input('\n\nAre You Ready ? (Yes/No): ')
        if a.upper() == 'YES':
            print('\n\n\t\t\t\t\t"GENERAL KNOWLEDGE QUIZ" is About To Begin in: ')
            time.sleep(1)
            print('3')
            time.sleep(1)
            print('2')
            time.sleep(1)
            print('1\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
            time.sleep(1)
            break 
        else:
            print('Enter "Yes" when ready')
# 1. ______________________________________________________________________________________________________________________________________________________________________

    time.sleep(1)
    table = [['1. What is the name of the biggest technology company in South Korea?'],['a) SSANGYOUNG'],['b) SAMSUNG'],['c) HYUNDAI MOTORS'],['d) KIA MOTORS']]
    print(tabulate(table, headers = 'firstrow', tablefmt = 'mixed_grid'))
    
    answer = input('Type your answer(A/B/C/D): ')
    if answer.upper() == 'B':
        print('\t\t\t\t\t\t\t\tCorrect!\n\n')
        score += 5
        correct += 1
    elif answer.lower() == 'q':
        print('Thanks for playing 😄')
        quit()
    else:
        print("\t\t\t\t\t\t\t\tIncorrect!\n\n")
        score -= 2
        incorrect += 1
#2. _______________________________________________________________________________________________________________________________________________________________________    
    time.sleep(1)
    table = [['2. What is the capital of Portugal?'],['a) RONALDO'],['b) PEPE'],['c) MBAPPE'],['d) LISBON']]
    print(tabulate(table, headers = 'firstrow', tablefmt = 'mixed_grid'))
    
    answer = input('Type your answer(A/B/C/D): ')
    if answer.upper() == 'D':
        print('\t\t\t\t\t\t\t\tCorrect!\n\n')
        score += 5
        correct += 1
    elif answer.lower() == 'q':
        print('Thanks for playing 😄')
        quit()
    else:
        print("\t\t\t\t\t\t\t\tIncorrect!\n\n")
        score -= 2
        incorrect += 1
#3. ___________________________________________________________________________________________________________        
    time.sleep(1)
    table = [['3. How many hearts does an Octopus Have?'],['a) THREE'],['b) TWO'],['c) ONE'],['d) EIGHT']]
    print(tabulate(table, headers = 'firstrow', tablefmt = 'mixed_grid'))
    
    answer = input('Type your answer(A/B/C/D): ')
    if answer.upper() == 'A':
        print('\t\t\t\t\t\t\t\tCorrect!\n\n')
        score += 5
        correct += 1
    elif answer.lower() == 'q':
        print('Thanks for playing 😄')
        quit()
    else:
        print("\t\t\t\t\t\t\t\tIncorrect!\n\n")
        score -= 2
        incorrect += 1
    if incorrect >= 3:
        print('You have given 3 incorrect answers!!')
        print("You didn't complete the quiz",',You Lose!!!')
        print('Your score is :',score)
        print("You submiited ", correct, "answers correctly")
        quit()
#4. ____________________________________________________________________________________________________________            
    time.sleep(1)
    table = [['4. Who is the Prime Minister of United Kingdom?'],['a) Queen Elizabeth'],['b) Justin Trudeau'],['c) Rishi Sunak'],['d) Joe Biden']]
    print(tabulate(table, headers = 'firstrow', tablefmt = 'mixed_grid'))
    
    answer = input('Type your answer(A/B/C/D): ')
    if answer.upper() == 'C':
        print('\t\t\t\t\t\t\t\tCorrect!\n\n')
        score += 5
        correct += 1
    elif answer.lower() == 'q':
        print('Thanks for playing 😄')
        quit()
    else:
        print("\t\t\t\t\t\t\t\tIncorrect!\n\n")
        score -= 2
        incorrect += 1
    if incorrect >= 3:
        print('You have given 3 incorrect answers!!')
        print("You didn't complete the quiz",',You Lose!!!')
        print('Your score is :',score)
        print("You submiited ", correct, "answers correctly")
        quit()
#5. ____________________________________________________________________________________________________________
    time.sleep(1)
    table = [['5. Who was the first Indian to go to space?'],['a) Rakesh Sharma'],['b) Sunita Williams '],['c) Kalpana Chawla'],['d) Neil Armstrong']]
    print(tabulate(table, headers = 'firstrow', tablefmt = 'mixed_grid'))
    
    answer = input('Type your answer(A/B/C/D): ')
    if answer.upper() == 'A':
        print('\t\t\t\t\t\t\t\tCorrect!\n\n')
        score += 5
        correct += 1
    elif answer.lower() == 'q':
        print('Thanks for playing 😄')
        quit()
    else:
        print("\t\t\t\t\t\t\t\tIncorrect!\n\n")
        score -= 2
        incorrect += 1
    if incorrect >= 3:
        print('You have given 3 incorrect answers!!')
        print("You didn't complete the quiz",',You Lose!!!')
        print('Your score is :',score)
        print("You submiited ", correct, "answers correctly")
        quit()
#6. _______________________________________________________________________________________________________________
    time.sleep(1)
    table = [['6. How many sides are there in a Dodecagon?'],['a) 10'],['b) 12'],['c) 21'],['d) No Such Polygon']]
    print(tabulate(table, headers = 'firstrow', tablefmt = 'mixed_grid'))
    
    answer = input('Type your answer(A/B/C/D): ')
    if answer.upper() == 'B':
        print('\t\t\t\t\t\t\t\tCorrect!\n\n')
        score += 5
        correct += 1
    elif answer.lower() == 'q':
        print('Thanks for playing 😄')
        quit()
    else:
        print("\t\t\t\t\t\t\t\tIncorrect!\n\n")
        score -= 2
        incorrect += 1
    if incorrect >= 3:
        print('You have given 3 incorrect answers!!')
        print("You didn't complete the quiz",',You Lose!!!')
        print('Your score is :',score)
        print("You submiited ", correct, "answers correctly")
        quit()
#7. _______________________________________________________________________________________________________________
    time.sleep(1)
    table = [['7. Name the river bank on which TAJ MAHAL is situated ?'],['a) Ganga'],['b) Yamuna'],['c) Godaveri'],['d) Indus']]
    print(tabulate(table, headers = 'firstrow', tablefmt = 'mixed_grid'))
    
    answer = input('Type your answer(A/B/C/D): ')
    if answer.upper() == 'B':
        print('\t\t\t\t\t\t\t\tCorrect!\n\n')
        score += 5
        correct += 1
    elif answer.lower() == 'q':
        print('Thanks for playing 😄')
        quit()
    else:
        print("\t\t\t\t\t\t\t\tIncorrect!\n\n")
        score -= 2
        incorrect += 1
    if incorrect >= 3:
        print('You have given 3 incorrect answers!!')
        print("You didn't complete the quiz",',You Lose!!!')
        print('Your score is :',score)
        print("You submiited ", correct, "answers correctly")
        quit()
#8. _______________________________________________________________________________________________________________
    time.sleep(1)
    table = [['8. What is the National Song of INDIA?'],['a) Vande Mataram'],['b) Jana Gana Mana'],['c) Saare Jahan Se Accha'],['d) Mere Desh Ki Dharti']]
    print(tabulate(table, headers = 'firstrow', tablefmt = 'mixed_grid'))
    
    answer = input('Type your answer(A/B/C/D): ')
    if answer.upper() == 'A':
        print('\t\t\t\t\t\t\t\tCorrect!\n\n')
        score += 5
        correct += 1
    elif answer.lower() == 'q':
        print('Thanks for playing 😄')
        quit()
    else:
        print("\t\t\t\t\t\t\t\tIncorrect!\n\n")
        score -= 2
        incorrect += 1
    if incorrect >= 3:
        print('You have given 3 incorrect answers!!')
        print("You didn't complete the quiz",',You Lose!!!')
        print('Your score is :',score)
        print("You submiited ", correct, "answers correctly")
        quit()
#9. _______________________________________________________________________________________________________________
    time.sleep(1)
    table = [['9. Which is the Largest Animal On Earth ?'],['a) African Elephant'],['b) Asian Elephant'],['c) Blue Whale'],['d) Humpback Whale']]
    print(tabulate(table, headers = 'firstrow', tablefmt = 'mixed_grid'))
    answer = input('Type your answer(A/B/C/D): ')
    if answer.upper() == 'C':
        print('\t\t\t\t\t\t\t\tCorrect!\n\n')
        score += 5
        correct += 1
    elif answer.lower() == 'q':
        print('Thanks for playing 😄')
        quit()
    else:
        print("\t\t\t\t\t\t\t\tIncorrect!\n\n")
        score -= 2
        incorrect += 1
    if incorrect >= 3:
        print('You have given 3 incorrect answers!!')
        print("You didn't complete the quiz",',You Lose!!!')
        print('Your score is :',score)
        print("You submiited ", correct, "answers correctly")
        quit()
#10. _______________________________________________________________________________________________________________
    time.sleep(1)
    table = [['10. Which Of the following is not a type of Whale?'],['a) Humpback Whale'],['b) Sperm Whale'],['c) Beluga Whale'],['d) Killer Whale']]
    print(tabulate(table, headers = 'firstrow', tablefmt = 'mixed_grid'))
    
    answer = input('Type your answer(A/B/C/D): ')
    if answer.upper() == 'D':
        print('\t\t\t\t\t\t\t\tCorrect!\n\n')
        score += 5
        correct += 1
    elif answer.lower() == 'q':
        print('Thanks for playing 😄')
        quit()
    else:
        print("\t\t\t\t\t\t\t\tIncorrect!\n\n")
        score -= 2
        incorrect += 1
    if incorrect >= 3:
        print('You have given 3 incorrect answers!!')
        print("You didn't complete the quiz",',You Lose!!!')
        print('Your score is :',score)
        print("You submiited ", correct, "answers correctly")
        quit()
    print('''
    YOUR SCORE IS: ''', score,'/50')

    print("You submiited ", correct, "answers correctly")

    if score == 50:
        input('''
    Enter your account number for prize money: ''')
        print('''
                                                                NAHI MILENGE PAISE     
                                                        🤣 🤣 KAISA LAGA MERA MAZAK 🤣 🤣''')
if a == '3':
    score = 0
    incorrect = 0
    correct = 0
    for i in range(1, 100):
        a = input('\n\nAre You Ready ? (Yes/No): ')
        if a.upper() == 'YES':
            print('\n\n\t\t\t\t\t"QUIZ on INDIA" is About To Begin in: ')
            time.sleep(1)
            print('3')
            time.sleep(1)
            print('2')
            time.sleep(1)
            print('1\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
            time.sleep(1)
            break 
        else:
            print('Enter "Yes" when ready')
# 1. ______________________________________________________________________________________________________________________________________________________________________

    time.sleep(1)
    table = [['1. Which was the first satellite of INDIA?'],['a) Bhaskara'],['b) Aryabhatta'],['c) Rohini'],['d) Kalpana']]
    print(tabulate(table, headers = 'firstrow', tablefmt = 'mixed_grid'))
    
    answer = input('Type your answer(A/B/C/D): ')
    if answer.upper() == 'B':
        print('\t\t\t\t\t\t\t\tCorrect!\n\n')
        score += 5
        correct += 1
    elif answer.lower() == 'q':
        print('Thanks for playing 😄')
        quit()
    else:
        print("\t\t\t\t\t\t\t\tIncorrect!\n\n")
        score -= 2
        incorrect += 1
# 2. ______________________________________________________________________________________________________________________________________________________________________

    time.sleep(1)
    table = [['2. Who was the first Prime Minister of INDIA?'],['a) Mahatma Gandhi'],['b) Indira Gandhi'],['c) Jawaharlal Nehru'],['d) Dr.Rajendra Prasad']]
    print(tabulate(table, headers = 'firstrow', tablefmt = 'mixed_grid'))
    
    answer = input('Type your answer(A/B/C/D): ')
    if answer.upper() == 'C':
        print('\t\t\t\t\t\t\t\tCorrect!\n\n')
        score += 5
        correct += 1
    elif answer.lower() == 'q':
        print('Thanks for playing 😄')
        quit()
    else:
        print("\t\t\t\t\t\t\t\tIncorrect!\n\n")
        score -= 2
        incorrect += 1
# 3. ______________________________________________________________________________________________________________________________________________________________________

    time.sleep(1)
    table = [['3. Who was the first Indian Governor-General of Independant INDIA?'],['a) Dr.Rajendra Prasad'],['b) Dadabhai Nairoji'],['c) Vallabhbhai Patel'],['d) C.Rajagopalachari']]
    print(tabulate(table, headers = 'firstrow', tablefmt = 'mixed_grid'))
    
    answer = input('Type your answer(A/B/C/D): ')
    if answer.upper() == 'D':
        print('\t\t\t\t\t\t\t\tCorrect!\n\n')
        score += 5
        correct += 1
    elif answer.lower() == 'q':
        print('Thanks for playing 😄')
        quit()
    else:
        print("\t\t\t\t\t\t\t\tIncorrect!\n\n")
        score -= 2
        incorrect += 1
    if incorrect >= 3:
        print('You have given 3 incorrect answers!!')
        print("You didn't complete the quiz",',You Lose!!!')
        print('Your score is :',score)
        print("You submiited ", correct, "answers correctly")
        quit()
# 4. ______________________________________________________________________________________________________________________________________________________________________

    time.sleep(1)
    table = [["4. When is National Voters' Day celebrated ?"],['a) 5 January'],['b) 5 December'],['c) 25 January'],['d) 25 December']]
    print(tabulate(table, headers = 'firstrow', tablefmt = 'mixed_grid'))
    
    answer = input('Type your answer(A/B/C/D): ')
    if answer.upper() == 'C':
        print('\t\t\t\t\t\t\t\tCorrect!\n\n')
        score += 5
        correct += 1
    elif answer.lower() == 'q':
        print('Thanks for playing 😄')
        quit()
    else:
        print("\t\t\t\t\t\t\t\tIncorrect!\n\n")
        score -= 2
        incorrect += 1
    if incorrect >= 3:
        print('You have given 3 incorrect answers!!')
        print("You didn't complete the quiz",',You Lose!!!')
        print('Your score is :',score)
        print("You submiited ", correct, "answers correctly")
        quit()
# 5. ______________________________________________________________________________________________________________________________________________________________________

    time.sleep(1)
    table = [["5. Which is the longest river flowing in INDIA ?"],['a) Indus'],['b) Godavari'],['c) Brahmaputra'],['d) Ganga']]
    print(tabulate(table, headers = 'firstrow', tablefmt = 'mixed_grid'))

    answer = input('Type your answer(A/B/C/D): ')
    if answer.upper() == 'D':
        print('\t\t\t\t\t\t\t\tCorrect!\n\n')
        score += 5
        correct += 1
    elif answer.lower() == 'q':
        print('Thanks for playing 😄')
        quit()
    else:
        print("\t\t\t\t\t\t\t\tIncorrect!\n\n")
        score -= 2
        incorrect += 1
    if incorrect >= 3:
        print('You have given 3 incorrect answers!!')
        print("You didn't complete the quiz",',You Lose!!!')
        print('Your score is :',score)
        print("You submiited ", correct, "answers correctly")
        quit()
# 6. ______________________________________________________________________________________________________________________________________________________________________

    time.sleep(1)
    table = [["6. Which state shares a boundary with only one Indian state ?"],['a) Sikkim'],['b) Nagaland'],['c) Assam'],['d) Manipur']]
    print(tabulate(table, headers = 'firstrow', tablefmt = 'mixed_grid'))
    
    answer = input('Type your answer(A/B/C/D): ')
    if answer.upper() == 'A':
        print('\t\t\t\t\t\t\t\tCorrect!\n\n')
        score += 5
        correct += 1
    elif answer.lower() == 'q':
        print('Thanks for playing 😄')
        quit()
    else:
        print("\t\t\t\t\t\t\t\tIncorrect!\n\n")
        score -= 2
        incorrect += 1
    if incorrect >= 3:
        print('You have given 3 incorrect answers!!')
        print("You didn't complete the quiz",',You Lose!!!')
        print('Your score is :',score)
        print("You submiited ", correct, "answers correctly")
        quit()
# 7. ______________________________________________________________________________________________________________________________________________________________________

    time.sleep(1)
    table = [["7. Identify the state which is not landlocked ?"],['a) Haryana'],['b) Andhra Pradesh'],['c) Telangana'],['d) Madhya Pradesh']]
    print(tabulate(table, headers = 'firstrow', tablefmt = 'mixed_grid'))
    
    answer = input('Type your answer(A/B/C/D): ')
    if answer.upper() == 'B':
        print('\t\t\t\t\t\t\t\tCorrect!\n\n')
        score += 5
        correct += 1
    elif answer.lower() == 'q':
        print('Thanks for playing 😄')
        quit()
    else:
        print("\t\t\t\t\t\t\t\tIncorrect!\n\n")
        score -= 2
        incorrect += 1
    if incorrect >= 3:
        print('You have given 3 incorrect answers!!')
        print("You didn't complete the quiz",',You Lose!!!')
        print('Your score is :',score)
        print("You submiited ", correct, "answers correctly")
        quit()
# 8. ______________________________________________________________________________________________________________________________________________________________________

    time.sleep(1)
    table = [["8. Who was the first Mughal Emperor of INDIA?"],['a) Babur'],['b) Humayun'],['c) Aurangzeb'],['d) Akbar']]
    print(tabulate(table, headers = 'firstrow', tablefmt = 'mixed_grid'))
    
    answer = input('Type your answer(A/B/C/D): ')
    if answer.upper() == 'A':
        print('\t\t\t\t\t\t\t\tCorrect!\n\n')
        score += 5
        correct += 1
    elif answer.lower() == 'q':
        print('Thanks for playing 😄')
        quit()
    else:
        print("\t\t\t\t\t\t\t\tIncorrect!\n\n")
        score -= 2
        incorrect += 1
    if incorrect >= 3:
        print('You have given 3 incorrect answers!!')
        print("You didn't complete the quiz",',You Lose!!!')
        print('Your score is :',score)
        print("You submiited ", correct, "answers correctly")
        quit()
# 9. ______________________________________________________________________________________________________________________________________________________________________

    time.sleep(1)
    table = [["9. Who is the President of INDIA?"],['a) Dr.Manmohan Singh'],['b) Rahul Gandhi'],['c) Draupadi Murmu'],['d) Rajnath Kovind']]
    print(tabulate(table, headers = 'firstrow', tablefmt = 'mixed_grid'))
    
    answer = input('Type your answer(A/B/C/D): ')
    if answer.upper() == 'C':
        print('\t\t\t\t\t\t\t\tCorrect!\n\n')
        score += 5
        correct += 1
    elif answer.lower() == 'q':
        print('Thanks for playing 😄')
        quit()
    else:
        print("\t\t\t\t\t\t\t\tIncorrect!\n\n")
        score -= 2
        incorrect += 1
    if incorrect >= 3:
        print('You have given 3 incorrect answers!!')
        print("You didn't complete the quiz",',You Lose!!!')
        print('Your score is :',score)
        print("You submiited ", correct, "answers correctly")
        quit()
# 10. ______________________________________________________________________________________________________________________________________________________________________

    time.sleep(1)
    table = [["10. Which is the most popular tourist destination amongst college students ?"],['a) Goa'],['b) Gujarat'],['c) Haryana'],['d) Home']]
    print(tabulate(table, headers = 'firstrow', tablefmt = 'mixed_grid'))
    
    answer = input('Type your answer(A/B/C/D): ')
    if answer.upper() == 'A':
        print('\t\t\t\t\t\t\t\tCorrect!\n\n')
        score += 5
        correct += 1
    elif answer.lower() == 'q':
        print('Thanks for playing 😄')
        quit()
    else:
        print("\t\t\t\t\t\t\t\tIncorrect!\n\n")
        score -= 2
        incorrect += 1
    if incorrect >= 3:
        print('You have given 3 incorrect answers!!')
        print("You didn't complete the quiz",',You Lose!!!')
        print('Your score is :',score)
        print("You submiited ", correct, "answers correctly")
        quit()
    print('''
    YOUR SCORE IS: ''', score,'/50')
    print("You submiited ", correct, "answers correctly")
    if score == 50:
        input('''
    Enter your account number for prize money: ''')
        print('''
                                                                NAHI MILENGE PAISE     
                                                        🤣 🤣 KAISA LAGA MERA MAZAK 🤣 🤣''')
if a == '4':
    score = 0
    incorrect = 0
    correct = 0
    for i in range(1, 100):
        a = input('\n\nAre You Ready ? (Yes/No): ')
        if a.upper() == 'YES':
            print('\n\n\t\t\t\t\t"SCIENCE QUIZ" is About To Begin in: ')
            time.sleep(1)
            print('3')
            time.sleep(1)
            print('2')
            time.sleep(1)
            print('1\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
            time.sleep(1)
            break 
        else:
            print('Enter "Yes" when ready')
# 1. ______________________________________________________________________________________________________________________________________________________________________

    time.sleep(1)
    table = [['1. Which of the following is a non metal that remains liquid at room temperature?'],['a) Phosphorous'],['b) Bromine'],['c) Chlorine'],['d) Mercury']]
    print(tabulate(table, headers = 'firstrow', tablefmt = 'mixed_grid'))
    
    answer = input('Type your answer(A/B/C/D): ')
    if answer.upper() == 'B':
        print('\t\t\t\t\t\t\t\tCorrect!\n\n')
        score += 5
        correct += 1
    elif answer.lower() == 'q':
        print('Thanks for playing 😄')
        quit()
    else:
        print("\t\t\t\t\t\t\t\tIncorrect!\n\n")
        score -= 2
        incorrect += 1
# 2. ______________________________________________________________________________________________________________________________________________________________________

    time.sleep(1)
    table = [['2. Which of the following metals forms an amalgam with other metals?'],['a) Tin'],['b) Mercury'],['c) Lead'],['d) Zinc']]
    print(tabulate(table, headers = 'firstrow', tablefmt = 'mixed_grid'))
    
    answer = input('Type your answer(A/B/C/D): ')
    if answer.upper() == 'B':
        print('\t\t\t\t\t\t\t\tCorrect!\n\n')
        score += 5
        correct += 1
    elif answer.lower() == 'q':
        print('Thanks for playing 😄')
        quit()
    else:
        print("\t\t\t\t\t\t\t\tIncorrect!\n\n")
        score -= 2
        incorrect += 1
# 3. ______________________________________________________________________________________________________________________________________________________________________

    time.sleep(1)
    table = [["3. The gas usually filled in electric bulb is ?"],['a) Nitrogen'],['b) Helium'],['c) Hydrogen'],['d) Oxygen']]
    print(tabulate(table, headers = 'firstrow', tablefmt = 'mixed_grid'))
    
    answer = input('Type your answer(A/B/C/D): ')
    if answer.upper() == 'A':
        print('\t\t\t\t\t\t\t\tCorrect!\n\n')
        score += 5
        correct += 1
    elif answer.lower() == 'q':
        print('Thanks for playing 😄')
        quit()
    else:
        print("\t\t\t\t\t\t\t\tIncorrect!\n\n")
        score -= 2
        incorrect += 1
    if incorrect >= 3:
        print('You have given 3 incorrect answers!!')
        print("You didn't complete the quiz",',You Lose!!!')
        print('Your score is :',score)
        print("You submiited ", correct, "answers correctly")
        quit()
# 4. ______________________________________________________________________________________________________________________________________________________________________

    time.sleep(1)
    table = [["4. Washing Soda is the common name for ?"],['a) Calcium Bicarbonate'],['b) Sodium Bicarbonate'],['c) Sodium Carbonate'],['d) Calcium Carbonate']]
    print(tabulate(table, headers = 'firstrow', tablefmt = 'mixed_grid'))
    
    answer = input('Type your answer(A/B/C/D): ')
    if answer.upper() == 'C':
        print('\t\t\t\t\t\t\t\tCorrect!\n\n')
        score += 5
        correct += 1
    elif answer.lower() == 'q':
        print('Thanks for playing 😄')
        quit()
    else:
        print("\t\t\t\t\t\t\t\tIncorrect!\n\n")
        score -= 2
        incorrect += 1
    if incorrect >= 3:
        print('You have given 3 incorrect answers!!')
        print("You didn't complete the quiz",',You Lose!!!')
        print('Your score is :',score)
        print("You submiited ", correct, "answers correctly")
        quit()
# 5. ______________________________________________________________________________________________________________________________________________________________________

    time.sleep(1)
    table = [["5. Tetraethyl Lead is used as ?"],['a) Pain killer'],['b) Fire extinguisher'],['c) Mosquito repellent'],['d) Petrol additive']]
    print(tabulate(table, headers = 'firstrow', tablefmt = 'mixed_grid'))
    
    answer = input('Type your answer(A/B/C/D): ')
    if answer.upper() == 'D':
        print('\t\t\t\t\t\t\t\tCorrect!\n\n')
        score += 5
        correct += 1
    elif answer.lower() == 'q':
        print('Thanks for playing 😄')
        quit()
    else:
        print("\t\t\t\t\t\t\t\tIncorrect!\n\n")
        score -= 2
        incorrect += 1
    if incorrect >= 3:
        print('You have given 3 incorrect answers!!')
        print("You didn't complete the quiz",',You Lose!!!')
        print('Your score is :',score)
        print("You submiited ", correct, "answers correctly")
        quit()
# 6. ______________________________________________________________________________________________________________________________________________________________________

    time.sleep(1)
    table = [["6. Which of the following is used as a lubricant?"],['a) Graphite'],['b) Silica'],['c) Water'],['d) Silicon dioxide']]
    print(tabulate(table, headers = 'firstrow', tablefmt = 'mixed_grid'))
    
    answer = input('Type your answer(A/B/C/D): ')
    if answer.upper() == 'A':
        print('\t\t\t\t\t\t\t\tCorrect!\n\n')
        score += 5
        correct += 1
    elif answer.lower() == 'q':
        print('Thanks for playing 😄')
        quit()
    else:
        print("\t\t\t\t\t\t\t\tIncorrect!\n\n")
        score -= 2
        incorrect += 1
    if incorrect >= 3:
        print('You have given 3 incorrect answers!!')
        print("You didn't complete the quiz",',You Lose!!!')
        print('Your score is :',score)
        print("You submiited ", correct, "answers correctly")
        quit()
# 7. ______________________________________________________________________________________________________________________________________________________________________

    time.sleep(1)
    table = [["7. The gases used in different types of welding would include ?"],['a) oxygen and hydrogen'],['b) oxygen, hydrogen, acetylene and nitrogen'],['c) oxygen, acetylene and argon'],['d) oxygen and acetylene']]
    print(tabulate(table, headers = 'firstrow', tablefmt = 'mixed_grid'))
    
    answer = input('Type your answer(A/B/C/D): ')
    if answer.upper() == 'D':
        print('\t\t\t\t\t\t\t\tCorrect!\n\n')
        score += 5
        correct += 1
    elif answer.lower() == 'q':
        print('Thanks for playing 😄')
        quit()
    else:
        print("\t\t\t\t\t\t\t\tIncorrect!\n\n")
        score -= 2
        incorrect += 1
    if incorrect >= 3:
        print('You have given 3 incorrect answers!!')
        print("You didn't complete the quiz",',You Lose!!!')
        print('Your score is :',score)
        print("You submiited ", correct, "answers correctly")
        quit()
# 8. ______________________________________________________________________________________________________________________________________________________________________

    time.sleep(1)
    table = [["8. The property of a substance to absorb moisture from the air on exposure is called ?"],['a) Osmosis'],['b) efflorescence'],['c) deliquescence'],['d) Absorption']]
    print(tabulate(table, headers = 'firstrow', tablefmt = 'mixed_grid'))
    
    answer = input('Type your answer(A/B/C/D): ')
    if answer.upper() == 'C':
        print('\t\t\t\t\t\t\t\tCorrect!\n\n')
        score += 5
        correct += 1
    elif answer.lower() == 'q':
        print('Thanks for playing 😄')
        quit()
    else:
        print("\t\t\t\t\t\t\t\tIncorrect!\n\n")
        score -= 2
        incorrect += 1
    if incorrect >= 3:
        print('You have given 3 incorrect answers!!')
        print("You didn't complete the quiz",',You Lose!!!')
        print('Your score is :',score)
        print("You submiited ", correct, "answers correctly")
        quit()
# 9. ______________________________________________________________________________________________________________________________________________________________________

    time.sleep(1)
    table = [["9. The average salinity of Sea water is ?"],['a) 3%'],['b) 3.5%'],['c) 4%'],['d) 4.5%']]
    print(tabulate(table, headers = 'firstrow', tablefmt = 'mixed_grid'))
    
    answer = input('Type your answer(A/B/C/D): ')
    if answer.upper() == 'B':
        print('\t\t\t\t\t\t\t\tCorrect!\n\n')
        score += 5
        correct += 1
    elif answer.lower() == 'q':
        print('Thanks for playing 😄')
        quit()
    else:
        print("\t\t\t\t\t\t\t\tIncorrect!\n\n")
        score -= 2
        incorrect += 1
    if incorrect >= 3:
        print('You have given 3 incorrect answers!!')
        print("You didn't complete the quiz",',You Lose!!!')
        print('Your score is :',score)
        print("You submiited ", correct, "answers correctly")
        quit()
# 10. ______________________________________________________________________________________________________________________________________________________________________

    time.sleep(1)
    table = [["10. The group of metals Fe, Co, Ni may best called as ?"],['a) Transition Elements'],['b) Alkali Metals'],['c) Semiconductors'],['d) p-block Elements']]
    print(tabulate(table, headers = 'firstrow', tablefmt = 'mixed_grid'))
    
    answer = input('Type your answer(A/B/C/D): ')
    if answer.upper() == 'A':
        print('\t\t\t\t\t\t\t\tCorrect!\n\n')
        score += 5
        correct += 1
    elif answer.lower() == 'q':
        print('Thanks for playing 😄')
        quit()
    else:
        print("\t\t\t\t\t\t\t\tIncorrect!\n\n")
        score -= 2
        incorrect += 1
    if incorrect >= 3:
        print('You have given 3 incorrect answers!!')
        print("You didn't complete the quiz",',You Lose!!!')
        print('Your score is :',score)
        print("You submiited ", correct, "answers correctly")
        quit()
    print('''
    YOUR SCORE IS: ''', score,'/50')
    print("You submiited ", correct, "answers correctly")
    if score == 50:
        input('''
    Enter your account number for prize money: ''')
        print('''
                                                                NAHI MILENGE PAISE     
                                                        🤣 🤣 KAISA LAGA MERA MAZAK 🤣 🤣''')
if a == '5':
    score = 0
    incorrect = 0
    correct = 0
    for i in range(1, 100):
        a = input('\n\nAre You Ready ? (Yes/No): ')
        if a.upper() == 'YES':
            print('\n\n\t\t\t\t\t"CURRENT AFFAIRS QUIZ" is About To Begin in: ')
            time.sleep(1)
            print('3')
            time.sleep(1)
            print('2')
            time.sleep(1)
            print('1\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
            time.sleep(1)
            break 
        else:
            print('Enter "Yes" when ready')
# 1. ______________________________________________________________________________________________________________________________________________________________________

    time.sleep(1)
    table = [["1. As per the World Bank's Migration and Development Brief, what is the expected Remittance flows to India in 2022-23?"],['a) USD 50 billion'],['b) USD 100 billion'],['c) USD 150 billion'],['d) USD 200 billion']]
    print(tabulate(table, headers = 'firstrow', tablefmt = 'mixed_grid'))
    
    answer = input('Type your answer(A/B/C/D): ')
    if answer.upper() == 'B':
        print('\t\t\t\t\t\t\t\tCorrect!\n\n')
        score += 5
        correct += 1
    elif answer.lower() == 'q':
        print('Thanks for playing 😄')
        quit()
    else:
        print("\t\t\t\t\t\t\t\tIncorrect!\n\n")
        score -= 2
        incorrect += 1
# 2. ______________________________________________________________________________________________________________________________________________________________________

    time.sleep(1)
    table = [['2. Economic Cooperation and Trade Agreement (ECTA) between India and which country is set to enter into force from December 2022??'],['a) Australia'],['b) UAE'],['c) France'],['d) India']]
    print(tabulate(table, headers = 'firstrow', tablefmt = 'mixed_grid'))
    
    answer = input('Type your answer(A/B/C/D): ')
    if answer.upper() == 'A':
        print('\t\t\t\t\t\t\t\tCorrect!\n\n')
        score += 5
        correct += 1
    elif answer.lower() == 'q':
        print('Thanks for playing 😄')
        quit()
    else:
        print("\t\t\t\t\t\t\t\tIncorrect!\n\n")
        score -= 2
        incorrect += 1
# 3. ______________________________________________________________________________________________________________________________________________________________________

    time.sleep(1)
    table = [["3. Which is the first country to gather six of its astronauts in space?"],['a) USA'],['b) Russia'],['c) Israel'],['d) China']]
    print(tabulate(table, headers = 'firstrow', tablefmt = 'mixed_grid'))
    
    answer = input('Type your answer(A/B/C/D): ')
    if answer.upper() == 'D':
        print('\t\t\t\t\t\t\t\tCorrect!\n\n')
        score += 5
        correct += 1
    elif answer.lower() == 'q':
        print('Thanks for playing 😄')
        quit()
    else:
        print("\t\t\t\t\t\t\t\tIncorrect!\n\n")
        score -= 2
        incorrect += 1
    if incorrect >= 3:
        print('You have given 3 incorrect answers!!')
        print("You didn't complete the quiz",',You Lose!!!')
        print('Your score is :',score)
        print("You submiited ", correct, "answers correctly")
        quit()
# 4. ______________________________________________________________________________________________________________________________________________________________________

    time.sleep(1)
    table = [["4. Paubrasilia echinata is the national tree species of which country?"],['a) Argentina'],['b) Japan'],['c) Brazil'],['d) Portugal']]
    print(tabulate(table, headers = 'firstrow', tablefmt = 'mixed_grid'))
    
    answer = input('Type your answer(A/B/C/D): ')
    if answer.upper() == 'C':
        print('\t\t\t\t\t\t\t\tCorrect!\n\n')
        score += 5
        correct += 1
    elif answer.lower() == 'q':
        print('Thanks for playing 😄')
        quit()
    else:
        print("\t\t\t\t\t\t\t\tIncorrect!\n\n")
        score -= 2
        incorrect += 1
    if incorrect >= 3:
        print('You have given 3 incorrect answers!!')
        print("You didn't complete the quiz",',You Lose!!!')
        print('Your score is :',score)
        print("You submiited ", correct, "answers correctly")
        quit()
# 5. ______________________________________________________________________________________________________________________________________________________________________

    time.sleep(1)
    table = [["5. Agni Warrior is a bilateral defence exercise held between India and which country?"],['a) USA'],['b) Sri Lanka'],['c) Singapore'],['d) India']]
    print(tabulate(table, headers = 'firstrow', tablefmt = 'mixed_grid'))
    
    answer = input('Type your answer(A/B/C/D): ')
    if answer.upper() == 'C':
        print('\t\t\t\t\t\t\t\tCorrect!\n\n')
        score += 5
        correct += 1
    elif answer.lower() == 'q':
        print('Thanks for playing 😄')
        quit()
    else:
        print("\t\t\t\t\t\t\t\tIncorrect!\n\n")
        score -= 2
        incorrect += 1
    if incorrect >= 3:
        print('You have given 3 incorrect answers!!')
        print("You didn't complete the quiz",',You Lose!!!')
        print('Your score is :',score)
        print("You submiited ", correct, "answers correctly")
        quit()
#6. _____________________________________________________________________________________________________________________________________________________________
    time.sleep(1)
    table = [["6. IIT-Madras has partnered with which country to launch “Centre for Energy” to work on UN-SDGs?"],['a) USA'],['b) Australia'],['c) Singapore'],['d) Germany']]
    print(tabulate(table, headers = 'firstrow', tablefmt = 'mixed_grid'))
    
    answer = input('Type your answer(A/B/C/D): ')
    if answer.upper() == 'B':
        print('\t\t\t\t\t\t\t\tCorrect!\n\n')
        score += 5
        correct += 1
    elif answer.lower() == 'q':
        print('Thanks for playing 😄')
        quit()
    else:
        print("\t\t\t\t\t\t\t\tIncorrect!\n\n")
        score -= 2
        incorrect += 1
    if incorrect >= 3:
        print('You have given 3 incorrect answers!!')
        print("You didn't complete the quiz",',You Lose!!!')
        print('Your score is :',score)
        print("You submiited ", correct, "answers correctly")
        quit()
#7. _____________________________________________________________________________________________________________________________________________________________
    time.sleep(1)
    table = [["7. Which Indian city is placed at 22nd rank in the 'Prime Global Cities Index Q3 2022' ?"],['a) Mumbai'],['b) Surat'],['c) New Delhi'],['d) Kolkata']]
    print(tabulate(table, headers = 'firstrow', tablefmt = 'mixed_grid'))
    
    answer = input('Type your answer(A/B/C/D): ')
    if answer.upper() == 'A':
        print('\t\t\t\t\t\t\t\tCorrect!\n\n')
        score += 5
        correct += 1
    elif answer.lower() == 'q':
        print('Thanks for playing 😄')
        quit()
    else:
        print("\t\t\t\t\t\t\t\tIncorrect!\n\n")
        score -= 2
        incorrect += 1
    if incorrect >= 3:
        print('You have given 3 incorrect answers!!')
        print("You didn't complete the quiz",',You Lose!!!')
        print('Your score is :',score)
        print("You submiited ", correct, "answers correctly")
        quit()
#8. _____________________________________________________________________________________________________________________________________________________________
    time.sleep(1)
    table = [["8. Which Indian state has named 'Prasoon Joshi' as its brand ambassador?"],['a) Gujarat'],['b) Assam'],['c) Uttarakhand'],['d) Bihar']]
    print(tabulate(table, headers = 'firstrow', tablefmt = 'mixed_grid'))
    
    answer = input('Type your answer(A/B/C/D): ')
    if answer.upper() == 'C':
        print('\t\t\t\t\t\t\t\tCorrect!\n\n')
        score += 5
        correct += 1
    elif answer.lower() == 'q':
        print('Thanks for playing 😄')
        quit()
    else:
        print("\t\t\t\t\t\t\t\tIncorrect!\n\n")
        score -= 2
        incorrect += 1
    if incorrect >= 3:
        print('You have given 3 incorrect answers!!')
        print("You didn't complete the quiz",',You Lose!!!')
        print('Your score is :',score)
        print("You submiited ", correct, "answers correctly")
        quit()
#8. _____________________________________________________________________________________________________________________________________________________________
    time.sleep(1)
    table = [["7. Which country has recently enacted a new penal code, which has triggered protests across the country?"],['a) China'],['b) Cuba'],['c) New Zealand'],['d) Brazil']]
    print(tabulate(table, headers = 'firstrow', tablefmt = 'mixed_grid'))
    
    answer = input('Type your answer(A/B/C/D): ')
    if answer.upper() == 'B':
        print('\t\t\t\t\t\t\t\tCorrect!\n\n')
        score += 5
        correct += 1
    elif answer.lower() == 'q':
        print('Thanks for playing 😄')
        quit()
    else:
        print("\t\t\t\t\t\t\t\tIncorrect!\n\n")
        score -= 2
        incorrect += 1
    if incorrect >= 3:
        print('You have given 3 incorrect answers!!')
        print("You didn't complete the quiz",',You Lose!!!')
        print('Your score is :',score)
        print("You submiited ", correct, "answers correctly")
        quit()
#9. _____________________________________________________________________________________________________________________________________________________________
    time.sleep(1)
    table = [["9. Which space agency installed Roll-Out Solar Array on the International Space Station?"],['a) ISRO'],['b) NASA'],['c) JAXA'],['d) ESA']]
    print(tabulate(table, headers = 'firstrow', tablefmt = 'mixed_grid'))
    
    answer = input('Type your answer(A/B/C/D): ')
    if answer.upper() == 'B':
        print('\t\t\t\t\t\t\t\tCorrect!\n\n')
        score += 5
        correct += 1
    elif answer.lower() == 'q':
        print('Thanks for playing 😄')
        quit()
    else:
        print("\t\t\t\t\t\t\t\tIncorrect!\n\n")
        score -= 2
        incorrect += 1
    if incorrect >= 3:
        print('You have given 3 incorrect answers!!')
        print("You didn't complete the quiz",',You Lose!!!')
        print('Your score is :',score)
        print("You submiited ", correct, "answers correctly")
        quit()
#10. _____________________________________________________________________________________________________________________________________________________________
    time.sleep(1)
    table = [["10. Which country launched its latest nuclear stealth bomber named 'B-21'?"],['a) Israel'],['b) Russia'],['c) Ukraine'],['d) USA']]
    print(tabulate(table, headers = 'firstrow', tablefmt = 'mixed_grid'))
    
    answer = input('Type your answer(A/B/C/D): ')
    if answer.upper() == 'D':
        print('\t\t\t\t\t\t\t\tCorrect!\n\n')
        score += 5
        correct += 1
    elif answer.lower() == 'q':
        print('Thanks for playing 😄')
        quit()
    else:
        print("\t\t\t\t\t\t\t\tIncorrect!\n\n")
        score -= 2
        incorrect += 1
    if incorrect >= 3:
        print('You have given 3 incorrect answers!!')
        print("You didn't complete the quiz",',You Lose!!!')
        print('Your score is :',score)
        print("You submiited ", correct, "answers correctly")
        quit()
    print('''
    YOUR SCORE IS: ''', score,'/50')
    print("You submiited ", correct, "answers correctly")
    if score == 50:
        input('''
    Enter your account number for prize money: ''')
        print('''
                                                                NAHI MILENGE PAISE     
                                                        🤣 🤣 KAISA LAGA MERA MAZAK 🤣 🤣''')
if a == '6':
    score = 0
    incorrect = 0
    correct = 0
    for i in range(1, 100):
        a = input('\n\nAre You Ready ? (Yes/No): ')
        if a.upper() == 'YES':
            print('\n\n\t\t\t\t\t"ODD ONE OUT QUIZ" is About To Begin in: ')
            time.sleep(1)
            print('3')
            time.sleep(1)
            print('2')
            time.sleep(1)
            print('1\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
            time.sleep(1)
            break 
        else:
            print('Enter "Yes" when ready')
# 1. ______________________________________________________________________________________________________________________________________________________________________

    time.sleep(1)
    table = [["1. PICK ODD ONE OUT?"],['a) PYTHON'],['b) JAVA'],['c) C++'],['d) SWIFT']]
    print(tabulate(table, headers = 'firstrow', tablefmt = 'mixed_grid'))
    
    answer = input('Type your answer(A/B/C/D): ')
    if answer.upper() == 'D':
        print('\t\t\t\t\t\t\t\tCorrect!\n\n')
        score += 5
        correct += 1
    elif answer.lower() == 'q':
        print('Thanks for playing 😄')
        quit()
    else:
        print("\t\t\t\t\t\t\t\tIncorrect!\n\n")
        score -= 2
        incorrect += 1
# 2. ______________________________________________________________________________________________________________________________________________________________________

    time.sleep(1)
    table = [["2. PICK ODD ONE OUT?"],['a) Dollar'],['b) Ounce'],['c) Peso'],['d) Euro']]
    print(tabulate(table, headers = 'firstrow', tablefmt = 'mixed_grid'))
    
    answer = input('Type your answer(A/B/C/D): ')
    if answer.upper() == 'B':
        print('\t\t\t\t\t\t\t\tCorrect!\n\n')
        score += 5
        correct += 1
    elif answer.lower() == 'q':
        print('Thanks for playing 😄')
        quit()
    else:
        print("\t\t\t\t\t\t\t\tIncorrect!\n\n")
        score -= 2
        incorrect += 1
# 3. ______________________________________________________________________________________________________________________________________________________________________

    time.sleep(1)
    table = [["3. PICK ODD ONE OUT?"],['a) Square'],['b) Triangle'],['c) Rectangle'],['d) Cuboid']]
    print(tabulate(table, headers = 'firstrow', tablefmt = 'mixed_grid'))
    
    answer = input('Type your answer(A/B/C/D): ')
    if answer.upper() == 'D':
        print('\t\t\t\t\t\t\t\tCorrect!\n\n')
        score += 5
        correct += 1
    elif answer.lower() == 'q':
        print('Thanks for playing 😄')
        quit()
    else:
        print("\t\t\t\t\t\t\t\tIncorrect!\n\n")
        score -= 2
        incorrect += 1
    if incorrect >= 3:
        print('You have given 3 incorrect answers!!')
        print("You didn't complete the quiz",',You Lose!!!')
        print('Your score is :',score)
        print("You submiited ", correct, "answers correctly")
        quit()
# 4. ______________________________________________________________________________________________________________________________________________________________________

    time.sleep(1)
    table = [["4. PICK ODD ONE OUT?"],['a) Amber Heard'],['b) Tushar'],['c) Tanishq'],['d) Tanish']]
    print(tabulate(table, headers = 'firstrow', tablefmt = 'mixed_grid'))
    
    answer = input('Type your answer(A/B/C/D): ')
    if answer.upper() == 'A':
        print('\t\t\t\t\t\t\t\tCorrect!\n\n')
        score += 5
        correct += 1
    elif answer.lower() == 'q':
        print('Thanks for playing 😄')
        quit()
    else:
        print("\t\t\t\t\t\t\t\tIncorrect!\n\n")
        score -= 2
        incorrect += 1
    if incorrect >= 3:
        print('You have given 3 incorrect answers!!')
        print("You didn't complete the quiz",',You Lose!!!')
        print('Your score is :',score)
        print("You submiited ", correct, "answers correctly")
        quit()
# 5. ______________________________________________________________________________________________________________________________________________________________________

    time.sleep(1)
    table = [["5. PICK ODD ONE OUT?(Related to CHITKARA)"],['a) Armstrong'],['b) MarcoPolo'],['c) Vasco Da Gama'],['d) Tesla']]
    print(tabulate(table, headers = 'firstrow', tablefmt = 'mixed_grid'))
    
    answer = input('Type your answer(A/B/C/D): ')
    if answer.upper() == 'D':
        print('\t\t\t\t\t\t\t\tCorrect!\n\n')
        score += 5
        correct += 1
    elif answer.lower() == 'q':
        print('Thanks for playing 😄')
        quit()
    else:
        print("\t\t\t\t\t\t\t\tIncorrect!\n\n")
        score -= 2
        incorrect += 1
    if incorrect >= 3:
        print('You have given 3 incorrect answers!!')
        print("You didn't complete the quiz",',You Lose!!!')
        print('Your score is :',score)
        print("You submiited ", correct, "answers correctly")
        quit()
# 6. ______________________________________________________________________________________________________________________________________________________________________

    time.sleep(1)
    table = [["6. PICK ODD ONE OUT?"],['a) IDLI'],['b) DOSA'],['c) CHHOLE BHATURE'],['d) SAMBHAR']]
    print(tabulate(table, headers = 'firstrow', tablefmt = 'mixed_grid'))
    
    answer = input('Type your answer(A/B/C/D): ')
    if answer.upper() == 'C':
        print('\t\t\t\t\t\t\t\tCorrect!\n\n')
        score += 5
        correct += 1
    elif answer.lower() == 'q':
        print('Thanks for playing 😄')
        quit()
    else:
        print("\t\t\t\t\t\t\t\tIncorrect!\n\n")
        score -= 2
        incorrect += 1
    if incorrect >= 3:
        print('You have given 3 incorrect answers!!')
        print("You didn't complete the quiz",',You Lose!!!')
        print('Your score is :',score)
        print("You submiited ", correct, "answers correctly")
        quit()
# 7. ______________________________________________________________________________________________________________________________________________________________________

    time.sleep(1)
    table = [["7. PICK ODD ONE OUT?"],['a) ASSAM'],['b) SIKKIM'],['c) ARRUNACHAL PRADESH'],['d) NAGALAND']]
    print(tabulate(table, headers = 'firstrow', tablefmt = 'mixed_grid'))
    
    answer = input('Type your answer(A/B/C/D): ')
    if answer.upper() == 'B':
        print('\t\t\t\t\t\t\t\tCorrect!\n\n')
        score += 5
        correct += 1
    elif answer.lower() == 'q':
        print('Thanks for playing 😄')
        quit()
    else:
        print("\t\t\t\t\t\t\t\tIncorrect!\n\n")
        score -= 2
        incorrect += 1
    if incorrect >= 3:
        print('You have given 3 incorrect answers!!')
        print("You didn't complete the quiz",',You Lose!!!')
        print('Your score is :',score)
        print("You submiited ", correct, "answers correctly")
        quit()
# 8. ______________________________________________________________________________________________________________________________________________________________________

    time.sleep(1)
    table = [["8. PICK ODD ONE OUT?"],['a) REALME'],['b) XIAOMI'],['c) SAMSUNG'],['d) HUAWEI']]
    print(tabulate(table, headers = 'firstrow', tablefmt = 'mixed_grid'))
    
    answer = input('Type your answer(A/B/C/D): ')
    if answer.upper() == 'C':
        print('\t\t\t\t\t\t\t\tCorrect!\n\n')
        score += 5
        correct += 1
    elif answer.lower() == 'q':
        print('Thanks for playing 😄')
        quit()
    else:
        print("\t\t\t\t\t\t\t\tIncorrect!\n\n")
        score -= 2
        incorrect += 1
    if incorrect >= 3:
        print('You have given 3 incorrect answers!!')
        print("You didn't complete the quiz",',You Lose!!!')
        print('Your score is :',score)
        print("You submiited ", correct, "answers correctly")
        quit()
# 9. ______________________________________________________________________________________________________________________________________________________________________

    time.sleep(1)
    table = [["9. PICK ODD ONE OUT?"],['a) BMW'],['b) AUDI'],['c) FERRARI'],['d) MERCEDES']]
    print(tabulate(table, headers = 'firstrow', tablefmt = 'mixed_grid'))
    
    answer = input('Type your answer(A/B/C/D): ')
    if answer.upper() == 'C':
        print('\t\t\t\t\t\t\t\tCorrect!\n\n')
        score += 5
        correct += 1
    elif answer.lower() == 'q':
        print('Thanks for playing 😄')
        quit()
    else:
        print("\t\t\t\t\t\t\t\tIncorrect!\n\n")
        score -= 2
        incorrect += 1
    if incorrect >= 3:
        print('You have given 3 incorrect answers!!')
        print("You didn't complete the quiz",',You Lose!!!')
        print('Your score is :',score)
        print("You submiited ", correct, "answers correctly")
        quit()
# 10. ______________________________________________________________________________________________________________________________________________________________________

    time.sleep(1)
    table = [["10. PICK ODD ONE OUT?"],['a) RANJI TROPHY'],['b) VIJAY HAZARE TROPHY'],['c) DHYANCHAND TROPHY'],['d) MUSHTAQ ALI TROPHY']]
    print(tabulate(table, headers = 'firstrow', tablefmt = 'mixed_grid'))
    
    answer = input('Type your answer(A/B/C/D): ')
    if answer.upper() == 'C':
        print('\t\t\t\t\t\t\t\tCorrect!\n\n')
        score += 5
        correct += 1
    elif answer.lower() == 'q':
        print('Thanks for playing 😄')
        quit()
    else:
        print("\t\t\t\t\t\t\t\tIncorrect!\n\n")
        score -= 2
        incorrect += 1
    if incorrect >= 3:
        print('You have given 3 incorrect answers!!')
        print("You didn't complete the quiz",',You Lose!!!')
        print('Your score is :',score)
        print("You submiited ", correct, "answers correctly")
        quit()
    print('''
    YOUR SCORE IS: ''', score,'/50')
    print("You submiited ", correct, "answers correctly")
    if score == 50:
        input('''
    Enter your account number for prize money: ''')
        print('''
                                                                NAHI MILENGE PAISE     
                                                        🤣 🤣 KAISA LAGA MERA MAZAK 🤣 🤣''')
