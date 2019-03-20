print("what is your age?")

a = int(input("I am "))
if a <= 17:
    print("you are too young - no entry")
elif a >= 18 and a <= 20:
            print ("you are allowed to enter but No drink - get a white tag")
elif a >= 21 and a <= 25:
            print ("you can drink only bear - get an orange tag")
else:
    print("you can drink - get a green tag")
