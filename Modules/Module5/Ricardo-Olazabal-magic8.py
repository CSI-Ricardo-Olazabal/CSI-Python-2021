import random
answers = ["Whithout a doubt.","It is decidedly so.","Very doubtful","Ask again later","Better not tell you know.","Reply hazy, try again later","My sources say NO.","Outlook not so good","My sources say YES.","Maybe.","You should ask yourself that question."]
name = str(input("What is your name? = "))
print(f"Hello, {name}! Welcome to all of my 8 balls.")
def ask():
    random_n = random.randint(0,11)
    question = str(input("What would you like to ask me? = "))
    print(f"{name.capitalize()} asks: {question}")
    print(answers[random_n])
    ask()
ask()
