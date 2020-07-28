'''
author = Tomas S
'''

text1 = ''' Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. '''

text2 = '''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.'''

text3 = '''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''


#| USER |   PASSWORD  |
#-----------------------
#| bob  |     123     |
#| ann  |    pass123  |
#| mike | password123 |
#| liz  |    pass123  |

login_db = {"bob": "123","ann": "pass123","mike": "password123","liz": "pass123"}
line = "="*20

while True:
    login = input("Enter user:")
    password = input("Enter password:")
    if login in login_db and login_db[login] == password:
        print("Thank you "+login+", you are now logged in.")
        break
    else:
        print("Incorrect user or password, try again.")
        continue

while True:
    print(line)
    print("We have 3 texts to be analyzed.")
    text_choice = input("Enter a number between 1 and 3 to select:")
    if not text_choice.isdigit():
        print("Not a number!")
        continue
    text_choice = int(text_choice)
    if text_choice in range(1,4):
        print(line)
        if (text_choice) == 1:
            print("There are",len(text1.split()),
                  "words in the selected text.")
            print("There are",sum(map(str.istitle, text1.split())),
                  "titlecase words.")
            print("There are",sum(map(str.isupper, text1.split())),
                  "uppercase words.")
            print("There are",sum(map(str.islower, text1.split())),
                  "lowercase words.")
            print("There are",sum(map(str.isdecimal, text1.split())),
                  "numeric strings.")
            chosen_text = text1
            break
        elif (text_choice) == 2:
            print("There are",len(text2.split()),
                  "words in the selected text.")
            print("There are",sum(map(str.istitle, text2.split())),
                  "titlecase words.")
            print("There are",sum(map(str.isupper, text2.split())),
                  "uppercase words.")
            print("There are",sum(map(str.islower, text2.split())),
                  "lowercase words.")
            print("There are",sum(map(str.isdecimal, text2.split())),
                  "numeric strings.")
            chosen_text = text2
            break
        elif (text_choice) == 3:
            print("There are",len(text3.split()),
                  "words in the selected text.")
            print("There are",sum(map(str.istitle, text3.split())),
                  "titlecase words.")
            print("There are",sum(map(str.isupper, text3.split())),
                  "uppercase words.")
            print("There are",sum(map(str.islower, text3.split())),
                  "lowercase words.")
            print("There are",sum(map(str.isdecimal, text3.split())),
                  "numeric strings.")
            chosen_text = text3
            break
    else:
        print("Make sure to select between values 1 to 3.")
        continue

print(line)

count = {}
words_in_text = chosen_text.split()
for i in words_in_text:
    if len(i) not in count:
      count[len(i)] = 1
    else:
      count[len(i)]+=1

for x in sorted(count):
    print(str(x)+"\t"+(int(count[x])*"*"), str(count[x]))
print(line)

words_in_text = chosen_text.split()
numerics = []

for num in words_in_text:
    if num.isnumeric():
        numerics.append(int(num))
print("If we summed all the numbers in the text we would get: "+ str(sum(numerics)))
print(line)