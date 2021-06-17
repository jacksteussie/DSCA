############################
# @author Jack Steussie    #
# @email jsteussi@ucsd.edu #
############################

def add_time(start, duration, start_day=''):
    ''' Takes in a start time, a duration time, and, optionally, a 
        starting day of the week, and returns the sum of the duration 
        and start times and the day of the week if specified.
    
    @param start: a string in the form of a start time in the 12-hour format
    @param duration: a string in the form hh:mm that is to be added to start
    @param start_day: an optional starting day of the week
    @return: the final time with, if applicable, how many days later it is
    '''
    # Constants for ease of use 
    CONST_AM = 'AM'
    CONST_PM = 'PM'

    # First separate the start and duration into hours, minutes, and AM/PM (a.k.a. offset)
    start_hours, start_minutes, start_offset = int(start.partition(':')[0]), \
        int(start.partition(':')[2].partition(' ')[0]), \
        start.partition(':')[2].partition(' ')[2]
    duration_hours, duration_minutes = int(duration.partition(':')[0]), \
        int(duration.partition(':')[2])

    # Calculate the 24-hour format for easier calculations
    if start_offset == "PM" :
        start_hours = start_hours + 12

    # Add together the hours and the minutes
    new_hours = start_hours + duration_hours
    new_minutes = start_minutes + duration_minutes

    # Check if minutes added went over 60 minutes
    if new_minutes > 60:
        add_hours = new_minutes // 60
        new_minutes -= add_hours * 60 
        new_hours += add_hours

    # Check to see if new day
    add_days = 0
    if new_hours > 24:
        add_days = new_hours // 24
        new_hours -= add_days * 24

    # Calculate whether new_time is in AM or PM and convert back to 12-hour
    if new_hours > 0 and new_hours < 12:
        new_offset = CONST_AM
    elif new_hours == 12:
        new_offset = CONST_PM
    elif new_hours > 12:
        new_offset = CONST_PM
        new_hours -= 12
    else:
        new_offset = CONST_AM
        new_hours += 12

    if add_days > 0:
        if add_days == 1:
            days_later = ' (next day)'
        else:
            days_later = ' (' + str(add_days) + ' days later)'
    else:
        days_later = ''
    
    # Now, if the user specified it, we will calculate the day of the week it is
    weekday_list = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", \
        "Saturday", "Sunday")
    
    if start_day:
        weeks = add_days // 7
        index = weekday_list.index(start_day.lower().capitalize()) + \
            (add_days - 7 * weeks)
        if index > 6:
            index -= 7
        day = ", " + weekday_list[index]
    else :
        day = ""
    
    # Now we format the final, calculated time!
    new_time= str(new_hours) + ":" + \
        (str(new_minutes) if new_minutes > 9 else ("0" + str(new_minutes))) + \
        " " + new_offset + day + days_later

    return new_time