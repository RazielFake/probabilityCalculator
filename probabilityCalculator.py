# -*- coding: utf-8 -*-
"""
Created on Wed May 26 15:29:06 2021

@author: Raziel
"""


import copy
import random
# Consider using the modules imported above.

class Hat:
    
    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            for n in range(int(value)):
                self.contents.append(str(key))
        
        
    def draw(self, num_drawns):
        picked = list()
        if(num_drawns >= len(self.contents)):
            return sorted(self.contents)
        else:
            for n in range(num_drawns):
                ran = random.randint(0, len(self.contents)-1)
                picked.append(self.contents.pop(ran))
            return sorted(picked)
        


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    
    positives = 0
    
    for n in range(num_experiments):
        
        #THIS IS TO PREVENT A LOGICAL ERROR WITH THE DRAWN BALLS
        aux = copy.deepcopy(hat)
        drawn_balls = aux.draw(num_balls_drawn)
        
        
        #CREATE A NEW DICTIONARY AND FILL WITH THE DRAWN BALLS AND THE TIMES 
        #THEY WERE DRAWN
        count_hat = dict.fromkeys(drawn_balls, 0)
        for value_drawn in(drawn_balls):
            for key, value in(count_hat.items()):
                if(value_drawn == key):
                    count_hat[key] +=1
        
        
        #CHECK IF THE DRAWN BALLS CONTAINS THE AMOUNT OF EXPECTED BALLS
        had_all = 0
        for key_exp, value_exp in(expected_balls.items()):
            
            for key_drawn, value_drawn in(count_hat.items()):
                #IF EXPECTED BALLS ARE IN THE DRAWN ONES
                if(key_exp == key_drawn):
                    if((int(count_hat[key_drawn]) > 0 ) 
                       and  (count_hat[key_drawn] >= expected_balls[key_exp])):
                        had_all += 1
                        break;
            
            if(had_all == len(expected_balls)):
                positives +=1

            
    return positives/num_experiments





''' hat = Hat(yellow=5,red=1,green=3,blue=9,test=1)
print(hat.drawn(5))
probability = experiment(hat=hat, expected_balls={"yellow":2,"blue":3,"test":1}, num_balls_drawn=5, num_experiments=200)
print(probability)


hat = Hat(blue=3,red=2,green=6)
probability = experiment(hat=hat, expected_balls={"blue":2,"green":1}, num_balls_drawn=4, num_experiments=1000)
print(probability)
 '''