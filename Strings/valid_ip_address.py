# import requests
# import mysql.connector
# import pandas as pd

def valid_ip_number(number):
    n = None
    try:
        if number != str(int(number)):
            return False
        n = int(number)
    except:
        return False
    if n > 0 and n <= 255:
        return True
    else:
        return False

# s = input()
s = '25525511135'

# 255(r1)255(r2)11(r3)135

for r1 in range(0,4):
   for r2 in range(r1+1,r1+4):
       for r3 in range(r2+1,r2+4):
           s1 = s[:r1]
           s2 = s[r1:r2]
           s3 = s[r2:r3]
           s4 = s[r3:]
           first = valid_ip_number(s1)
           second = valid_ip_number(s2)
           third = valid_ip_number(s3)
           fourth = valid_ip_number(s4)
           if first and second and third and fourth:
               print('--------')
               print("{}.{}.{}.{}".format(s1,s2,s3,s4))
              

