# this function filters an array by a numbered condition
def filterNumFunc(array, variable, number):
    filteredArray = []
    for element in array:
        if element[variable] == number:
            filteredArray.append(element)
    return filteredArray