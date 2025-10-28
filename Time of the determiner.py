time = int(input("Enter the time of day"))

if time < 0 or time > 24:
    print("Invalid, Insert a number only between (0 - 24)")
else: 
    if 5 <= time <= 11:
        print("Morning")
    elif 12<= time <= 16:
        print("Afternoon")
    elif 17<= time <=20:
        print("Evening")
    elif time >= 21 or time <= 4:
        print("Night")
