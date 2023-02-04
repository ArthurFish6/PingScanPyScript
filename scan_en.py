'''START'''
#Importation of modules
from os import system
print('\nThis is simple tools using os and  ICMP protocol :)\n')
'''///'''
print('[1] scan 1 IP\n\n[2] scan an IP range\n')
s = input('select an option > ')
'''///'''
#IF
if s == '1':
    #1
    ip = input('select ur IP to scan > ')
    system('ping {}'.format(ip))


if s == '2':
    '''///'''
    #2
    rang = input("select ur range ip \nexemple(192.168.1) >  ")
    '''///'''
    a = input("start of the range > ")
    a = int(a)
    '''///'''
    b = input("last number of the range > ")
    b = int(b)
    '''///'''
    long = a
    for ping in range(a, b):
        system("ping {}.{}".format(rang, long))
        long = long + 1
'''END'''
