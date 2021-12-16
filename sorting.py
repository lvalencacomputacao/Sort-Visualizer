import random

def bubble_sort(vector):
    to_return = []
    for i in range(len(vector)):
        for j in range(len(vector)-1-i):
            if (vector[j] > vector[j+1]):
                to_return.append(vector.copy())
                vector[j], vector[j+1] = vector[j+1], vector[j]
    to_return.append(vector.copy())
    return to_return

def inversed_bubble_sort(vector):
    to_return = []
    for i in range(len(vector)):
        for j in range(len(vector)-1-i):
            if (vector[j] < vector[j+1]):
                to_return.append(vector.copy())
                vector[j], vector[j+1] = vector[j+1], vector[j]
    to_return.append(vector.copy())
    return to_return

def numbers_shuffle(vector):
    to_return = []
    for i in range(10):
        to_return.append(vector.copy())
        random.shuffle(vector)
    to_return.append(vector.copy())
    return to_return