############################
# @author Jack Steussie    #
# @email jsteussi@ucsd.edu #
############################

import copy
import random

class Hat:
    def __init__(self, **kwargs):
        ''' Constructor for class Hat. Takes an unspecified number of 
            non-keyword arguments (colors) with a dictionary. 
        
        @param self: Hat class instance self-reference
        @param **kwargs: dictionary of non-keyword arguments (colors)
        @return: None
        '''
        self.contents = list()
        for key, val in kwargs.items():
            for _ in range(val):
                self.contents.append(key)
         
    def draw(self, number):
        ''' Removes balls from the Hat object at random from contents and 
            returns those balls as a list of strings. If the number of balls
            to draw exceeds the available quantity, returns the contents of 
            the hat.
        
        @param self: Hat class instance self-reference
        @param number: number of balls to draw from the hat
        @return: list of balls removed from hat or list of the contents of hat
        '''
        if number > len(self.contents):
            return self.contents
        
        balls = []
        for _ in range(number):
            choice = random.randrange(len(self.contents))
            balls.append(self.contents.pop(choice))
        
        return balls
    
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    ''' Returns the probability of drawing the contents in expected_balls arg.
        Calculated by performing 'num_experiments' (N) experiments while 
        counting how many times we get the expected_balls (call this M) for 
        each experiment, and estimate the probability as M/N.
    
    @param hat: hat object containing balls (should be copied inside function)
    @param expected_balls: list of balls we are calculating the drawing chance
    @param num_balls_drawn: the number of balls to draw out of hat each time
    @param num_experiments: the number of experiments to perform
    @return: the probability of drawing the input list of expected_balls
    '''
    expected_balls_num = []
    for key in expected_balls:
        expected_balls_num.append(expected_balls[key])

    num_success = 0

    for _ in range(num_experiments):
        new_hat = copy.deepcopy(hat)
        balls = new_hat.draw(num_balls_drawn)

        num_balls = []
        for key in expected_balls:
            num_balls.append(balls.count(key))
        
        if num_balls >= expected_balls_num:
            num_success += 1
    
    return num_success / num_experiments # M/N
