def lucas(row:int, col:int, values=None):
    """ """
    two_d = [] * row
    for _ in two_d:
        two_d[_} = [] * col

# Exercise 3:
# Dynamically build a 2D data structure and initialize with values
def make_2d(rows:int, cols:int, value=None):
    '''Create a rows x cols 2D data structure
    initialized to _value_
    Example:
    >>> made_2d(3, 3)
    [[None, None, None], [None, None, None], [None, None, None]]
    '''
    list_2d = []
    for _ in range(rows):
        elems = []             # makes a empty list
        for _ in range(cols):  # then fills empty list
            elems.append(value)# with value
        list_2d.append(elems)  # puts this list into parent list 
    return list_2d
