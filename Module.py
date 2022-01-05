loginList = ["Da"]
passwordList = ["Net"]


def CheckOut(a:str,b:str):
    '''It allows you to check out the type of an 'input' variable and call input again if variable type isn't string
    :param string b: output
    :param string a: 'input' variable
    :rtype:string
    '''
    while type(a)!=str():
        try:
            print(b)
            a = input("-->")
            return a
        except: ValueError


def Authorization():
    '''It allows you to input your login and password to enter on your 'account'
    :rtype:int
    '''
    login=0
    password=0

    login=CheckOut(login,"Login: ")
    if login in loginList:
        print()
    
    password=CheckOut(password,"Password: ")
    if password in passwordList:
        if loginList.index(login)==passwordList.index(password):
            ans = "one"
    else:
        ans = "zero"
    return ans


def Registration():
    '''It allows you to create new login and password which will be added to login and password lists
    :rtype:int
    '''
    newLogin=0
    while True:
        while type(newLogin)!=str():
            try:
                input("Please write new login: ")
                
            except: ValueError


