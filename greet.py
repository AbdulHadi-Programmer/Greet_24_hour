import time
h = int(time.strftime("%H"))
user = input("Enter Your Name: ")
print()
if (h >= 0 and h < 6):
    print("Good Afternoon", user)
elif (h >= 6 and h < 9):
    print("Good Evening", user)
elif (h >= 9 and h < 12):
    print("Good Night", user)
elif (h >= 12 and h <= 18):
    print("Good Mid-Night", user)
elif (h > 18 and h <=24):
    print("Good Morning", user)
