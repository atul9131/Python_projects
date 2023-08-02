# Email Validation (Using Regex Functions)
'''
a-z
0-9
. _  one time
@  one time
. at II OR III postion from back
'''

import re
email_condition = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
user_email = input('Enter your email : ')

if re.search(email_condition , user_email):
    print('Right Email')
else:
    print('Wrong email')


