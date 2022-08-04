#!/usr/bin/env python3

import netifaces

print(netifaces.interfaces())

for i in netifaces.interfaces(): #loops through interfaces
    print('\n**********Details of Interface - ' + i + '**********') #displays interfaces
    
    try:
        print('MAC: ', end='')
        print(netifaces.ifaddresses(i)[netifaces.AF_LINK][0]['addr']) #displays interface addresses

        print('IP: ', end='')
        print(netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr'])

    except:
        print('Could not collect adapter information')
