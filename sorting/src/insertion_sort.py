

def insertion_sort(A):
    for j in range(1, len(A)):
        A = insert(A, j)
    return A

def insert(A, j):
    if j <= 0 or j >= len(A):
        raise ValueError(f"Invalid index of {j} for {type(A)} of length {len(A)}")
    key = A[j]
    i = j - 1
    while i >= 0 and key < A[i]:
        A[i+1] = A[i]
        i -= 1
    A[i+1] = key
    return A
