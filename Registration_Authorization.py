from Module import*

way = ""
while True:
    while type(way)!=int():
        try: 
            way = int(input("Type number action you want to do\nRegistration - 1\nAuthorization - 2\nEnd Task - 3\n"))
            if way==1:
                if Registration()=="zero":
                    print("\nUser alredy exist\n")
                else:
                    print("\nYou successfully created new account\n")
            elif way==2:
                if Authorization()=="zero":
                    print("\nLogin or password are wrong\n")
                else:
                    print("\nYou are Welcome!\n")
            elif way==3:
                break
        except: ValueError
    break 