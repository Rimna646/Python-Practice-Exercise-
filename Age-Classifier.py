age= int(input("how old are you?"))

def classify_person(age):
    if age <= 12:
       print("child")
    elif age <= 17:
    	print("teenager")
    elif age <= 64:
        print ("adult")
    elif age >= 65:
        print ("senior")
        

classify_person(age) 
