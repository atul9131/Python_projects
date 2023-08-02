# Speed of typing using python and time fuction (in word/min )

from time import *
import random as r

def mistake(partest , usertest):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error = error + 1
        except :
            error = error + 1
    return error

def speed_time(time_s, time_e, userinput):
    time_delay = time_e - time_s
    time_R = round(time_delay,2)
    speed = len(userinput)/time_R
    return round(speed)

if __name__ == '__main__':

    while True:
        ck = input('Ready to Type : Yes/NO :: ')
        if ck == 'Yes' :   
            test = ['Being able to match varying sets of characters is the first thing regular expressions can do that isnt already possible with the methods available on strings.' ,'However, if that was the only additional capability of regexes, they would not be much of an advance.' ,'Another capability is that you can specify that portions of the RE must be repeated a certain number of times.']
            test1 = r.choice(test)
            print('                           ****** Typing Speed ****** ')
            print(test1)
            print(len(test1))
            print()
            print()
            time_1 = time()/60
            testinput = input('Enter : ')
            time_2 = time()/60

            print('Speed : ',speed_time(time_1,time_2,testinput), "word/min")
            print('Error : ', mistake(test1,testinput))
            print(len(testinput))

        elif ck == 'No' :
            print('Thank You')
            break
        else:
            print('Wrong Input')



