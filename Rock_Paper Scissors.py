from microbit import *
import random
import radio

rock = Image('00000:'
                '09990:'
                '09990:'
                '09990:'
                '00000:')
    
paper = Image('99999:'
            '90009:'
            '90009:'
            '90009:'
            '99999:')

scissors  = Image('90009:'
              '09090:'
              '00900:'
              '09090:'
              '90009:')
              
tie = Image('00000:'
              '00000:'
              '99999:'
              '00000:'
              '00000:')

win = Image('90009:'
              '90009:'
              '90909:'
              '99099:'
              '90009:')
              
lose = Image('90000:'
              '90000:'
              '90000:'
              '90000:'
              '99990:')



radio.on()

while True:
    
                    
    if pin0.is_touched():
        display.show(rock)
        choice1 = 'rock'

    if pin1.is_touched():
        display.show(paper)
        choice1 = 'paper'

    if pin2.is_touched():
        display.show(scissors)
        choice1 = 'scissors'
        
    if button_a.was_pressed():
        radio.send(choice1)

    incoming = radio.receive()
    
    if incoming == 'rock':
        if choice1 == 'rock':
            display.show(tie)
        elif choice1 == 'paper':
            display.show(win)
        else:
            display.show(lose)
    
    elif incoming == 'paper':
        if choice1 == 'rock':
            display.show(lose)
        elif choice1 == 'paper':
            display.show(tie)
        else:
            display.show(win)
    
    elif incoming == 'scissors':
        if choice1 == 'rock':
            display.show(win)
        elif choice1 == 'paper':
            display.show(lose)
        else:
            display.show(tie)
