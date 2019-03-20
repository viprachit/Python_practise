d = int(input("Enter your grade: "))

if d >= 35:
	if d >= 35 and d < 50:
		print("Second Class")
	elif d >= 50 and d < 60:
		print("Higher Second Class")
	elif d >= 60 and d < 75:
		print("First Class")
	else:
		print("Distinction..!!")
else:
	print("Failed")