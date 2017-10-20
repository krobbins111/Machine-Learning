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

def PLalgo(x[], y[], c[]):
    threshold = 3
    pass = 0
    h = 0
    #formula = (rand*threshold) + (rand*x) + (rand*y) 
    while(pass < x.length()):
        i = 0
        while(i < x.length):
            #formula = (rand*threshold) + (rand*x[i]) + (rand*y[i])
            #if formula < 0: h = 0
            #if formula > 0: h = 1
            #if h == c[i}:
                #pass = pass + 1
                #continue
            #else:
                #change of all weights where
        
#a way to return the weights. divide from final formula and add to int array
#along with epoch counter at end of every inner loop
#return int array

#because x is always set to something, all weights change upon failure
    #FIXED ABOVE BY CHANGING T0 -5 : 5 SO THAT WINNOW NOT X PARTS CAN JUST BE THE
            #NEGATIVE OF X I.E. (weight * smart + weight times  * not smart) smart = -not smart
            


