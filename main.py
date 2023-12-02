import random as ran
import colorama as col

col.init(autoreset=True)
quiz = ["Food", "Animal", "Transport", "Verb", "Letter", "Programming Language"]
things = [
    ["Banana", "Cheery", "StrawBerry", "Pear"],
    ["Wolf", "Cheetah", "Giraffe", "Bear"],
    ["Airplane", "Jet", "Taxi", "Lolly"],
    ["Develop", "Learn", "Sing", "Killing"],
    ['F', "K", "Z", "T"],
    ["Ruby", "TypeScript", "Cobol", "C#"]
]

# start
print("Welcome To Hangman" + col.Style.BRIGHT + col.Fore.YELLOW)
i = 5  # Initialize i outside the loop
while i > 0:
    j = 4
    while j > 0:
        print(f"Name a {quiz[i - 1]}")
        user = input(col.Fore.GREEN + "ANS >> ").lower()
        if user == ran.choice(things[i - 1]).lower():
            print('Yes')
        else:
            print('No')
        j = j - 1
    i = i - 1

else:
    print("You Lose" + col.Fore.RED)
