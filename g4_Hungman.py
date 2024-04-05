import random

def switch_case(argument):
    switcher = {
        1: print(
        """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                """),
        2: """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                """,
        3: """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                """,
        4: """ --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                """,
        5: """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                """,
    }
    return switcher.get(argument, "Invalid case")

list = ["apple", "banana", "carrot", "dog", "elephant", "frog", "giraffe", "horse", "iguana", "jellyfish"]
chosen_word=random.choice(list)
print(chosen_word)
b=len(chosen_word)
le=b
old_le=le
chances=0
print(b)
word=[]
for i in chosen_word:
    word += "-"
print(word)
while le>0:
    a = input("choose a letter : ")
    for i in range(b):
        if chosen_word[i] == a:
            word[i] = a
            le -= 1
        else:
            continue
    print(word)

    if le == old_le:
        chances += 1
        print(switch_case(chances))
    if chances == 5:
        print("YOU LOST")
        break
    if le == 0:
        print("YOU WON")
        break
    old_le=le

