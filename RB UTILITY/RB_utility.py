# -*- coding: utf-8 -*-
"""
Created on Thu May 12 16:32:03 2016

@author: ALCZ11511047
"""

import argparse
from RESET_BUDDY_lib import RBUDDY

# argparse cause pzthon script to be run with parameters.
# this script has 3 parameters  - operation (set, get, reset...)
#                               - pin 
#                               - state (low/high - 0/1)
#                               - optional - time (reset speed)

# resulting script run syntax:
# python RB_utility.py operation pin state (time)  


parser = argparse.ArgumentParser()
parser.add_argument("operation", help="Choose action (set,reset,clear all",
                    type = str, choices = ["set","get","reset","rev_reset","clearall",
                    "test","s","g","r","rev","c","t",'crazy!'])
parser.add_argument("pin", choices = ['x','a','all','1','2','3','4','5','6','7','8','9'],
                    help = "choose pin")
parser.add_argument("state", choices = ['x','0','1'],
                    help = "choose state")  
parser.add_argument("-t","--time", type = float, help = "reset time in seconds") 
            
args = parser.parse_args()            



UTILITY = RBUDDY()

#sets or clears 1 pin or all pins
if args.operation == "set" or args.operation == "s":
    if (args.pin == 'x') or (args.state == 'x') :
        print('invalid input!!!')
    elif args.pin == 'a':
        for i in range (9):
            UTILITY.set_pin((i+1),int(args.state))
    elif args.pin == 'all':
        for i in range (9):
            UTILITY.set_pin((i+1),int(args.state))        
    else:  
        UTILITY.set_pin(int(args.pin),int(args.state))      

        
if args.operation == "get" or args.operation == "g":
    if args.pin == 'x':
        print('invalid input!!!')
    elif args.pin == 'a':
        for i in range (9):   
            UTILITY.get_pin(i+1)
    elif args.pin == 'all':
        for i in range (9):   
            UTILITY.get_pin(i+1)        
    else:
        UTILITY.get_pin(int(args.pin))
            
if args.operation == "reset" or args.operation == "r":
    if args.time == None:
        args.time = 1
    if args.pin == 'x':
        print('invalid input!!!')
    elif args.pin == 'a':
        for i in range (9): 
            UTILITY.reset_pin(i+1, args.time)
    elif args.pin == 'all':
        for i in range (9):   
            UTILITY.reset_pin(i+1, args.time)        
    else:         
        UTILITY.reset_pin(int(args.pin), args.time)
    
if args.operation == "rev_reset" or args.operation == "rev":
    if args.time == None:
        args.time = 1
    if args.pin == 'x':
        print('invalid input!!!')
    elif args.pin == 'a':
        for i in range (9): 
            UTILITY.reverse_reset_pin(i+1, args.time)
    elif args.pin == 'all':
        for i in range (9):   
            UTILITY.reverse_reset_pin(i+1, args.time)        
    else:         
        UTILITY.reverse_reset_pin(int(args.pin), args.time)
    
        
if args.operation == "crazy!":
    UTILITY.crazy()      

if args.operation == "test"or args.operation == "t":
    UTILITY.test()         
    
               
