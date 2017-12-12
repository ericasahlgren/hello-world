fruit_basket=['apple','banana','strawberry','melon','pineapple']

Guess = raw_input("Guess a fruit!")

if Guess in fruit_basket:
    print("you found a " + Guess)
else:
    print("There is no " + Guess + " in the fruit basket")

