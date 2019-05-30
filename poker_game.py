#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 30 10:40:50 2019

@author: Vydeepthi
"""
#%%
import random
#%%
number_of_card=52
number_of_players=int(input("Enter the number of players:"))
names=[]
for i in range(number_of_players):
    new_name=input("Enter the name of player: ")
    names.append(new_name)
print(names)
#%%
"""
1. The script will deal 5 cards to each player (you can use random.choice to select at random from a list). The different cards, sorted from lowest to highest are 2,3,4,5,6,7,8,9,10,J,Q,K,A. 
There are four suits, clubs, spades, hearts, diamonds.
2. The script will print out each one of the players' hand, find out which one of the players have a winning hand and will print out the name of the winner
3. Easy version, where we just compare the hands and the hand with the highest cards wins.
 For example, if Player 1 has the hand 2,3,K,Q,7 and Player 2 has the hand 8,10, ACE,J,2 
 Player 2 would win because 1 ACE beats a K. 
 If Player 1 has the hand 2,3,K,Q,7, and 
 Player 2 has the hand J,J,K,7,3 then Player 1 would win (since K,Q beats K,J)."""
#%%
suit = ['s', 'c', 'd', 'h']
rank = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K','A',]
class Cards:
    def _init_(self, rank, suits):
        self.suit=suit
        self.rank=rank
    def _str_(self):
        return self.rank + "of" +self.suit
    