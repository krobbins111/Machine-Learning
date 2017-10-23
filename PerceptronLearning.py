#Perceptron Learning


#Noise level 1 (no noise), level 2, level 3
# Level 1 will represent the control and compared to other levels to see how they suffer

#CLASS LABEL NOISE: an example surrounded by examples of a different class or when an example is in the gray area between classes

#Perhaps use poor classes that will overlap easily in domain


#Need to make up examples for two classes with number integers (intelligence scale 1-10 and effort scale 1-10)
#Question would be to see if someone is an honor student

#make linear classifier for easy smart, hardworking to student in honor class

#low effort, low intelligence into not honor

#class label noise represents lazy geniuses and hardworking fails as well as close mix in the middle

#perceptron learn and winnow
#polynomials?

import random

x = {4.4, 2.8, -3, -1.1}
y = {4.5, 4, -4, -2.7}

def inc(x, y, t, rate):
    i = 0
    while(i < x.length()):
        i = i +1


def PLalgo(x, y, c):
    threshold = 10 *random()
    passed = 0
    h = 0
    learn = 0.5
    #formula = threshold) + (rand*x) + (rand*y) #nvm
    while(passed < x.length()):
        i = 0
        while(i < x.length()):
            formula = (threshold) + (x[i]) + (y[i])
            if formula < 0: h = 0
            if formula > 0: h = 1
            if h == c[i]:
                passed = passed + 1
            if h == 1 and c[i] == 0:
                #decrease of all weights additive by learn
                passed = 0
            if h == 0 and c[i] == 1:
                #increase of all weight additive by learn
                passed = 0
            i = i + 1
        
#a way to return the weights. divide from final formula and add to int array
#along with epoch counter at end of every inner loop
#return int array

#because x is always set to something, all weights change upon failure
    #FIXED ABOVE BY CHANGING T0 -5 : 5 SO THAT WINNOW NOT X PARTS CAN JUST BE THE
            #NEGATIVE OF X I.E. (weight * smart + weight times  * not smart) smart = -not smart
            


