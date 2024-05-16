import random as rd

#● ┌ ─ ┐ │ └ ┘

"┌──────────┐"
"│          │"
"│          │"
"│          │"
"└──────────┘"
dice_art ={
    1:("┌───────────┐",
       "│           │",
       "│     ●     │",
       "│           │",
       "└───────────┘"),
    2:("┌───────────┐",
       "│   ●       │",
       "│           │",
       "│        ●  │",
       "└───────────┘"),
    3:("┌───────────┐",
       "│   ●       │",
       "│      ●    │",
       "│        ●  │",
       "└───────────┘"),
    4:("┌───────────┐",
       "│   ●    ●  │",
       "│           │",
       "│   ●    ●  │",
       "└───────────┘"),
    5:("┌───────────┐",
       "│   ●    ●  │",
       "│      ●    │",
       "│   ●    ●  │",
       "└───────────┘"),
    6:("┌───────────┐",
       "│   ●    ●  │",
       "│   ●    ●  │",
       "│   ●    ●  │",
       "└───────────┘")
    
}

dice=[]
total=0
number_of_dice=int(input("how many dice?"))

for die in range(number_of_dice):
    dice.append(rd.randint(1,6))

#for column
#for die in range(number_of_dice):
#    for line in dice_art.get(dice[die]):
#        print(line)

#for row
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end=" ")
    print()  # This prints a newline character after printing all the lines of a single row of dice

for die in dice:
    total+= die
print("total=", total)

