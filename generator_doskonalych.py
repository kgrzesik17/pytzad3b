def perfect_numbers(min:int, max:int):
    """
    This generator generates perfect numbers for user specified range.


    Input:
    min - minimum value
    max - maximum value

    Output:
    yield - perfect numbers in user specified range
    boolean value - False if failed
    """

    try:
        for i in range(min, max + 1):
            temp = []

            for j in range(1, i // 2 + 1):
                if i % j == 0:
                    temp.append(j)

            if sum(temp) == i:
                yield i

    except TypeError:
        print("Niepoprawna wartość.")
        return False
    except:
        print("Nieznany błąd.")
        return False