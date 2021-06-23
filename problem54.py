"""
High Card: 2 - 14 points (2-10-J-Q-K-A)
One Pair: 
Two Pairs: 
Three of a Kind: 
Straight: 
Flush: 
Full House: 
Four of a Kind: 
Straight Flush: 
Royal Flush: 

The file, poker.txt, contains one-thousand random hands dealt to two players. 
Each line of the file contains ten cards (separated by a single space): 
the first five are Player 1's cards and the last five are Player 2's cards. 
You can assume that all hands are valid 
(no invalid characters or repeated cards), 
each player's hand is in no specific order, 
and in each hand there is a clear winner.

How many hands does Player 1 win?
"""
#%%
import numpy as np
import pandas as pd
import os as os

raw = pd.read_csv('poker.txt', header = None)

#%%

both_hands = raw.loc[0].item().split(' ')
print(both_hands)
P1 = both_hands[:5]
P2 = both_hands[5:]

class hand:
    def __init__(self, lis):
        self.suits = [list(card)[1] for card in lis]
        self.nums = self.get_nums(lis)
        self.nums.sort()
        self.flush = self.is_flush()
        self.straight = self.is_straight()
        self.num_dict()
        
        
    def is_flush(self):
        if len(set(self.suits)) > 1:
            return False
        else: return True
    
    
    def get_nums(self,lis):
        nums = [list(card)[0] for card in lis]
        nums = np.array(nums).astype('<U2')
        
        nums[nums=='T'] = '10'
        nums[nums=='J'] = '11'
        nums[nums=='Q'] = '12'
        nums[nums=='K'] = '13'
        nums[nums=='A'] = '14'
        nums = nums.astype('int')
        return nums
    
    
    def is_straight(self):
        if (len(set(self.nums)) == 5) and (np.max(self.nums)-np.min(self.nums) == 4):
            return True
        else:
            return False
    
    def num_dict(self):
        self.dict = {}
        for i in self.nums:
            if i in self.dict: 
                self.dict[i]+=1
            else: 
                self.dict[i] = 1
    
    def four_of_a_kind(self):
        if max(self.dict.values()) == 4:
            return True
        else:
            return False
    
    def full_house(self):
        if (max(self.dict.values()) == 3) and (min(self.dict.values()) == 2):
            return True
        else:
            return False
    
    def three_of_a_kind(self):
        if (max(self.dict.values()) == 3):
            return True
        else:
            return False
    
    def two_pair(self):
        if (max(self.dict.values()) == 2) and (len(self.dict.values()) == 3):
            return True
        else:
            return False
    
    def one_pair(self):
        if (max(self.dict.values()) == 2) and (len(self.dict.values()) == 4):
            return True
        else:
            return False
    
    def high_card(self):
        return max(self.nums)
    
    def get_score(self):
        if self.is_flush() and self.is_straight():
            return 10
        elif self.four_of_a_kind():
            return 9
        elif self.full_house():
            return 8
        elif self.is_flush():
            return 7
        elif self.is_straight():
            return 6
        elif self.three_of_a_kind():
            return 5
        elif self.two_pair():
            return 4
        elif self.one_pair():
            return 3
        else:
            return 2
    
    def tie_break(self,score):
        if score == 2:
            return max (self.nums)
        elif score == 3:
            pass
"""     
One Pair: 
Two Pairs: 
Three of a Kind: 
Straight: 
Flush: 
Full House: 
Four of a Kind: 
Straight Flush: 
Royal Flush: 
"""   
    
H1 = hand(P1)
print(H1.nums)

class winner:
    def __init__(self):
        self.winner = 0
    
    def set(self, n):
        if self.winner == 0:
            self.winner = n
    
    def get(self):
        return self.winner
        

#%% 
Wins1, Wins2 = 0, 0
ties = []
for i in range(1000):
    W = winner()
    both_hands = raw.loc[i].item().split(' ')
    Hand1 = hand(both_hands[:5])
    Hand2 = hand(both_hands[5:])
    S1 = Hand1.get_score()
    S2 = Hand2.get_score()
    
    if S1 == S2:
        #for this set, the only ties are high card and 1 pair
        #compare highest number
        if S1==2:
            i=1
            while W.get() ==0:            
                if Hand1.nums[-i] > Hand2.nums[-i]:
                    W.set(1)
                elif Hand1.nums[-i] < Hand2.nums[-i]:
                    W.set(2)
                i+=1
    
        if S1 == 3:
            pair1, pair2 = 0, 0
            
            keys1 = list(Hand1.dict.keys())
            vals1 = list(Hand1.dict.values())
            pair1 = keys1[vals1.index(2)]
            
            keys2 = list(Hand2.dict.keys())
            vals2 = list(Hand2.dict.values())
            pair2 = keys2[vals2.index(2)]
            
            if pair1>pair2:
                W.set(1)
            elif pair1<pair2:
                W.set(2)
            else:
                i=1
                while W.get() ==0:            
                    if Hand1.nums[-i] > Hand2.nums[-i]:
                        W.set(1)
                    elif Hand1.nums[-i] < Hand2.nums[-i]:
                        W.set(2)
                    i+=1
        
    elif S1 > S2:
        
        W.set(1)
    else:
        W.set(2)
        
    if W.get() == 1: 
        Wins1 += 1
    elif W.get() == 2:
        Wins2 += 1

#Final Answer:
#376
    
    
        

    
    
    
    
        
    
        
        















    