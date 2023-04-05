test= str(input("What course is it?    "))
max_score = int(input("what is the maximum score to get?    "))
score= int(input("what did you score?    "))
percentage = round(float(score/max_score), 2) * 100
print("Your score is", percentage, "%")

if percentage > 89 and percentage <= 100  :
    print("You got an A+!")
elif percentage > 79 and percentage <= 90 :
    print("You got an A!")
elif percentage > 69 and percentage <= 80 :
    print ("You got a B!")
elif percentage > 59 and percentage <= 70 :
    print("You got a C!")
elif percentage > 49 and percentage <= 60 :
    print("You got a D!")
else:
    print ("You got a U :(")
