def add_time(start, duration, day=None):
    ''' Takes in a start time, a duration time, and, optionally, a starting
        day of the week, and returns the sum of the duration and start times.
    
    @param start: a string in the form of a start time in the 12-hour format
    @param duration: a string in the form hh:mm that is to be added to start
    @param day: an optional starting day of the week
    @return: the final time with, if applicable, how many days later it is
    '''
    
    return new_time