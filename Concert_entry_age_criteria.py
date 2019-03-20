print ("a ticket to Led Zeppelin concert please?")
print ("Yes, what is your age?")
a = int(input())
if a <=1:
    print("free entry but we recommend not to take babies inside")
elif a >=2 and a <=18:
    print ("Please pay $2")
elif a >= 65 and a<=130:
    print ("Please pay $5")
else:
    print ("Please pay $10")