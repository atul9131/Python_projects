# Email validation (Using String Functions)

email = input('Enter Your Email: ')  # g@g.in , atulmeena310@gmail.com

j,k,d = 0,0,0
if len(email) >= 6:
    if email[0].isalpha():
        if ("@" in email) and (email.count('@')==1):
            if (email[-4]=='.') or (email[-3]=='.'):
                for i in email:
                    if i==i.isspace():
                        j = 1
                    elif i.isalpha():
                        if i==i.upper():
                            k = 1
                    elif i.isdigit():
                        continue
                    elif i=='_' or i=='.' or i=='@':
                        continue
                    else:
                        d = 1
                    
                if j==1 or k==1 or d==1 :
                    print('Wrong Email 5') 
                else:
                    print("Right Email") 
            else :
                print ("Wrong Email due to . 4")
        else :
            print("Wrong Email due to @ 3")
    else :
        print("Wrong Email due to First character is not alphabet 2")
else :
    print('Wrong Email due to less than 6 character 1')














