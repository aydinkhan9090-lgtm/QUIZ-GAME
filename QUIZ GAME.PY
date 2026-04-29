questions={
    "WHAT IS THE CAPITAL OF FRANCE?": "PARIS",
    "WHAT IS THE LARGEST PLANET IN OUR SOLAR SYSTEM?": "JUPITER",
    "WHO WROTE THE PLAY 'ROMEO AND JULIET'?": "WILLIAM SHAKESPEARE",
    "WHAT IS THE CAPITAL OF JAPAN?": "TOKYO",
    "WHO INVENTED PYTHON": "GUIDO VAN ROSSUM",
}
score=0
print("Welcome to the QUIZ GAME^_^")

for question in questions:
    answer=input(question + " : " ).upper()
    if answer==questions[question]:
        score= score + 1
    else:
        print("WRONG ANSWER,TRY AGAIN 😊")

print("your score is:", score, "/5")
