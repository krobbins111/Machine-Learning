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

#training set 1: No Noise
smart1 = [4.4, 2.8, 3.5, 3.2, -3, -1.1, -4, -2.4]
effort1 = [4.5, 4, 4.1, 4.9, -4, -2.7, -2.1, -2.5]
classifier1 = [1, 1, 1, 1, 0, 0, 0, 0]

#training set 2: Boundary cases
smart2 = [4.4, 2.8, 3.5, 3.2, -3, -1.1, -0.4, 1]
effort2 = [4.5, 4, 4.1, 4.9, -4, -2.7, 1.3, -1]
classifier2 = [1, 1, 1, 1, 0, 0, 0, 1]

#training set3: Severe class label noise
smart3 = [4.4, 2.8, 3.5, -3.2, -3, -1.1, 4.5, -1.5, -3, 4.1]
effort3 = [4.5, 4, 4.1, -4.9, -4, -2.7, -2, 4.6, -3.5, 4.3]
classifier3 = [1, 1, 1, 0, 0, 0, 1, 1, 1, 0]

#def inc(x, y, t, rate):
 #   i = 0
 #   t += 1
  #  while(i < len(x)):
   #     x[i] += 1
    #    y[i] += 1
     #   i += 1

#def dec(w0, w1, w2):
 #   i = 0
  #  t -= rate
   # while(i < len(x)):
    #    x[i] -= rate
     #   y[i] -= rate
      #  i += 1

#above functions changed due to use of weights rather than adjusting the vector while testing

def PLalgo(x, y, c):
    threshold = random.randint(-5, 5)
    passed = 0
    h = 0
    learn = 0.1
    epochcount = 0
    w0 = random.random() * 100
    w1 = random.random() * 100
    w2 = random.random() * 100
    print(w0, w1, w2)
    #formula = threshold) + (rand*x) + (rand*y) #nvm
    while(passed < len(x)):
        i = 0
        if epochcount > 10000:
            print('Not Linearly Separable')
            break
        while(i < len(x)):
            formula = (w0 * threshold) + (w1 * x[i]) + (w2 * y[i])
            print('formula: ')
            print(formula)
            print('\n')
            if formula <= 0: h = 0
            if formula > 0: h = 1
            print('h and c: ')
            print(h, c[i])
            print('\n')
            if h == c[i]:
                passed = passed + 1
            elif h == 1 and c[i] == 0:
                #decrease of all weights additive by learn
                if x[i] != 0: w1 -= learn
                if y[i] != 0: w2 -= learn
                print('Decreased\n')
                passed = 0
            elif h == 0 and c[i] == 1:
                #increase of all weight additive by learn
                if x[i] != 0: w1 += learn
                if y[i] != 0: w2 += learn
                print('Increased\n')
                passed = 0
            else: print('Error')
            i = i + 1
            print('Passed: ')
            print(passed)
            print('\n')
        epochcount += 1
    print('Epochs: ')
    print(epochcount)
    print('\n')
    print(w0, w1, w2)
    return epochcount


PLalgo(smart2, effort2, classifier2)

#a way to return the weights. divide from final formula and add to int array
#along with epoch counter at end of every inner loop
#return int array

#because x is always set to something, all weights change upon failure
    #FIXED ABOVE BY CHANGING T0 -5 : 5 SO THAT WINNOW NOT X PARTS CAN JUST BE THE
            #NEGATIVE OF X I.E. (weight * smart + weight times  * not smart) smart = -not smart
            


