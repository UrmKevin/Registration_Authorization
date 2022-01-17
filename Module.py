#str0 = ".,:;!_*-+()/#¤%&"
#str1 = '0123456789'
#str2 = 'qwertyuiopasdfghjklzxcvbnm'
#str3 = str2.upper()

def Authorization(ll,pl):
    '''It allows you to input your login and password to enter on your 'account'
    :param list ll: List of logins
    :param list pl: List of password
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
    if login in ll and password in pl:
        if ll.index(login)==pl.index(password):
            ans = "one"
    else:
        ans = "zero"
    return ans


def Registration(ll,pl):
    '''It allows you to create new login and password which will be added to login and password lists
    :param list ll: List of logins
    :param list pl: List of password
    :rtype:str
    '''
    newLogin=0
    newPassword=0
    
    while type(newLogin)==int:
        try:
            newLogin = input("\nPlease write new login: \n-->")
        except: ValueError
    
    while True:
        while type(newPassword)!=str:
            try:
                newPassword = input("Please create password: \n-->")
                break
            except: ValueError
        break

    if newLogin in ll and newPassword in pl:
        if ll.index(newLogin)==pl.index(newPassword):
            ans = "zero"
        else:
            ans = "one"
            rida_salvestamine('Logins.txt',newLogin)
            rida_salvestamine('Passwords.txt',newPassword)
            ll.append(newLogin)
            pl.append(newPassword)
    else:
        rida_salvestamine('Logins.txt',newLogin)
        rida_salvestamine('Passwords.txt',newPassword)
        ll.append(newLogin)
        pl.append(newPassword)
        ans = "one"
    return ans


def Failist_Lugemine(f:str,l:list):
    '''
    :param file f: 
    :param list l: 
    :rtype:list
    '''
    file=open(f,'r')
    for rida in file:
        l.append(rida.strip())
    file.close()
    return l


def failisse_salvestamine(f:str,l:list):
    '''Loetelu salvestame failisse
    '''
    file=open(f,'w')
    for e in l:
        file.write(e+'\n')
    file.close()


def rida_salvestamine(f:str,rida:str):
    '''Üks sõna või lause(rida) salvestamine filisse
    '''
    file=open(f,'a')
    file.write(rida+'\n')
    file.close()
