# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 21:29:46 2020

@author: clem7

This script will try to guess the mysterious number prepared
by guess_my_number.GuessMachine

It's strategy is to try random numbers between min and max.
It'll adapt min and max values to match GuessMachine answers'

"""

from guess_my_number import MIN,MAX,GuessMachine

if __name__=='__main_':
    min = MIN
    max = MAX
    guess_machine= GuessMachine()
    while True:
        attempt= int((min +max)/2)
        result = guess_machine.guess(attempt)
        print('tried %d : %s' % (attempt,result))
        if result == 'found' :
            
            print('Finished in %d attempts.' % guess_machine.number_of_attempt)
            break
        elif result == 'too low':
            min = attempt + 1
        else:
            max = attempt - 1

