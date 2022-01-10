loginList = ["Kevin"]
passwordList = ["Urm"]
str0 = ".,:;!_*-+()/#¤%&"
str1 = '0123456789'
str2 = 'qwertyuiopasdfghjklzxcvbnm'
str3 = str2.upper()

def Authorization():
    '''It allows you to input your login and password to enter on your 'account'
    :rtype:str
    '''
    login=0
    password=0

    while type(login)!=str:
        try:
            login = input("Login: \n-->")
        except: ValueError
    
    while type(password)!=str:
        try:
            password = input("Password: \n-->")
        except: ValueError
    if login in loginList and password in passwordList:
        if loginList.index(login)==passwordList.index(password):
            ans = "one"
    else:
        ans = "zero"
    return ans


def Registration():
    '''It allows you to create new login and password which will be added to login and password lists
    :rtype:str
    '''
    newLogin=0
    newPassword=0
    
    while type(newLogin)==int:
        try:
            newLogin = input("\nPlease write new login: \n-->")
        except: ValueError
    
    #while newLogin in loginList:
    #    try:
    #        newLogin = input("\nThis login is alredy exist\nPlease write new login: \n-->")
    #    except: ValueError
    
    while True:
        while type(newPassword)!=str:
            try:
                newPassword = input("Please create password: \n-->")
                break
            except: ValueError
        break

    if newLogin in loginList and newPassword in passwordList:
        if loginList.index(newLogin)==passwordList.index(newPassword):
            ans = "zero"
    else:
        loginList.append(newLogin)
        passwordList.append(newPassword)
        ans = "one"
    return ans
