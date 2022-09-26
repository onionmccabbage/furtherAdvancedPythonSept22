# here is a filter function to filter data by 'starts with'
def filterNames(x, l):
    '''
    For a data structure x return only if 'name' starts with letter l
    '''
    if x['name'].startswith(l):
        return x['name'] # we have a match, so return this item
    else:
        return '' # no match