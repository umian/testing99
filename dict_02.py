def average(*numbers):
    result= sum(numbers)/len(numbers)
    return result

numbers=(2,3,4,5,6,88,77,44)
x=average(*numbers)
print(x)