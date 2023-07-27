import time
h = int(time.strftime("%H"))
user = input("Enter Your Name: ")
print()
# if (int(h) >= 0 and int(h) <= 6):
#     print("Good Afternoon", user)
# elif (int(h) > 6 and int(h) < 12):
#     print("Good Night", user) 
# elif (int(h) >= 12 and int(h) <= 18):
#     print("Good Mid-Night", user)  
# elif (int(h) > 18 and int(h) <=24):
#     print("Good Morning", user)
##################################################
#if (int(h) >= 0 and int(h) <= 6):
#    print("Good Afternoon", user)
#elif (int(h) > 6 and int(h) < 9):
#    print("Good Evening", user)
#elif (int(h) >= 9 and int(h) < 12):
#    print("Good Night", user)
#elif (int(h) >= 12 and int(h) <= 18):
#    print("Good Mid-Night", user)
#elif (int(h) > 18 and int(h) <=24):
#    print("Good Morning", user)
#################################################
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
