from operator import itemgetter

def selection_sort(A):
    for j in range(len(A)-1):
        i, _ = min(enumerate(A[j:]), key=itemgetter(1))
        A[j], A[i+j] = A[i+j], A[j]
    return A
