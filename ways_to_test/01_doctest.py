import doctest

def cubes(a,b):
    '''
    return all the cubes of values in ghe range a to b
    We write doctests within the documentation string
    >>> cubes(1,5)
    [1, 8, 27, 64]
    >>> cubes(1,101) # doctest:+ELLIPSIS +NORMALIZE_WHITESPACE
    [1, 8, ..., 1000000]
    '''
    answers = []
    for i in range(a, b):
        answers.append(i**3)
    return answers


if __name__ == '__main__':
    # print( cubes(1, 8) ) 
    doctest.testmod(verbose=True)