def bubble_sort(vector):
    to_return = []
    for i in range(len(vector)):
        for j in range(len(vector)-1-i):
            if (vector[j] > vector[j+1]):
                to_return.append(vector.copy())
                vector[j], vector[j+1] = vector[j+1], vector[j]
    to_return.append(vector.copy())
    return to_return

def insertion_sort():
    pass

def inversed_bubble_sort():
    pass