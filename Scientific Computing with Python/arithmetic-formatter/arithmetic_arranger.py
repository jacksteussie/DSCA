############################
# @author Jack Steussie    #
# @email jsteussi@ucsd.edu #
############################

def arithmetic_arranger(input, show_answers=False):
    ''' Receives a list of strings that are arithmetic problems and returns the 
        problems arranged vertically and side-by-side.

    @param input: list of strings that contains arithmetic problems
    @param show_answers: by default is False; True will display answers
    @return: a string of the formatted problems
    '''
    if len(input) > 5:
        return 'Error: Too many problems.'
    
    output: str
    first_nums = list()
    second_nums = list()
    operators = list()
    cur_index = 0

    # First row loop
    for elem in input:
        if '+' not in elem and '-' not in elem:
            return 'Error: Operator must be \'+\' or \'-\'.'
        elif '+' in elem:
            op = '+'
            operators.append(op)

        elif '-' in elem:
            op = '-'
            operators.append(op)
        
        elem = elem.replace(' ', '')
        num_1 = elem.split(op)[0]
        num_2 = elem.split(op)[1]
        first_nums.append(num_1)
        second_nums.append(num_2)

        if(len(num_1) > 4 or len(num_2) > 4):
            return 'Error: Numbers cannot be more than four digits.'
        elif not num_1.isdecimal() or not num_2.isdecimal():
            return 'Error: Numbers must only contain digits.'

        output += num_1.rjust(max([len(num_1), len(num_2)]) + 2, ' ')

        if cur_index == len(input) - 1:
            break
        else:
            output += ' ' * 4

        cur_index += 1

    output += '\n'
    
    # Second row loop
    cur_index = 0
    for i in range(0, len(input)):
        num_1 = first_nums[i]
        num_2 = second_nums[i]
        op = operators[i]
        output += op + num_2.rjust(max([len(num_1), len(num_2)]) + 1, ' ')

        if cur_index == len(input) - 1:
            break
        else:
            output += ' ' * 4

        cur_index += 1
    
    output += '\n'

    # Third row loop
    cur_index = 0
    for i in range(0, len(input)):
        num_1 = first_nums[i]
        num_2 = second_nums[i]
        op = operators[i]

        for i in range(0, max([len(num_1), len(num_2)]) + 2):
            output += '-'
        
        if cur_index == len(input) - 1:
            break
        else:
            output += ' ' * 4

        cur_index += 1

    # Answer calculations and fourth row if the user specifies it
    if show_answers == True:
        output += '\n'

        cur_index = 0
        for i in range(0, len(input)):
            num_1 = first_nums[i]
            num_2 = second_nums[i]
            op = operators[i]
            if(operators[i] == '+'):
                answer = int(num_1) + int(num_2)
            elif(operators[i] == '-'):
                answer = int(num_1) - int(num_2)

            output += str(answer).rjust(max([len(num_1), len(num_2)]) + 2, ' ')

            if cur_index == len(input) - 1:
                break
            else:
                output += ' ' * 4
            
            cur_index += 1

    return output
