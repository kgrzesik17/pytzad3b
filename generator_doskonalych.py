def perfect_numbers(min:int, max:int):
    '''
    This function generates perfect number for user specified range. 

    Input:
    min - minimum value
    max - maximum value

    Output:
    array - array of perfect numbers in user specified range.
    boolean value - False if failed
    '''

    output = []

    try:
        for i in range(min, max + 1):
            temp = []

            for j in range(1, i // 2 + 1):
                if i % j == 0:
                    temp.append(j)
            
            if sum(temp) == i:
                output.append(i)

    except TypeError:
        print("Niepoprawna wartość.")
        return False

    return output

print(perfect_numbers(1, 499))