############################
# @author Jack Steussie    #
# @email jsteussi@ucsd.edu #
############################

import numpy as np

def calculate(lst):
    ''' Takes input of a list containing 9 digits, converts it to a 3 x 3 numpy
        array and returns a dictionary containing the mean, variance, standard
        deviation, max, min and sum along both axes and for the flattened
        matrix. 

    @param list: list of 9 digits
    @return: dictionary of lists containing the calculated statistics
    '''
    if len(lst) != 9:
        raise ValueError("List must contain nine numbers.")
    array = np.array(lst).reshape((3, 3))
    calculations = {
        "mean": [
            np.mean(array, axis = 0).tolist(),
            np.mean(array, axis = 1).tolist(),
            np.mean(array.tolist())
        ],
        "variance": [
            np.var(array, axis = 0).tolist(),
            np.var(array, axis = 1).tolist(),
            np.var(array) .tolist()    
        ],
        "standard deviation": [
            np.std(array, axis = 0).tolist(),
            np.std(array, axis = 1).tolist(),
            np.std(array).tolist()     
        ],   
        "max": [
            np.max(array, axis = 0).tolist(),
            np.max(array, axis = 1).tolist(),
            np.max(array).tolist()     
        ], 
        "min": [
            np.min(array, axis = 0).tolist(),
            np.min(array, axis = 1).tolist(),
            np.min(array).tolist()     
        ], 
        "sum": [
            np.sum(array, axis = 0).tolist(),
            np.sum(array, axis = 1).tolist(),
            np.sum(array).tolist()     
        ],  
    }
    
    return calculations