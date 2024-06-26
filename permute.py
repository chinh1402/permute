def permute(k, arr):
    n = len(arr)
    permutation = ""
    for i in range(0, n):
        permutation = permutation + k[arr[i] - 1]
    return permutation

def straight_permutation():
    k = "ABCDEFGH"
    arr = [3, 1, 4, 7, 6, 2, 5, 8]
    print("Straight Permutation:")
    print("Before permutation:", k)
    print("arr:", arr)
    result = permute(k, arr)
    print("After permutation:", result)
    print("Input Length:", len(k), "Output Length:", len(result))
    print()

def extend_permutation():
    k = "ABCDEFGH"
    arr = [3, 1, 4, 7, 6, 2, 5, 8, 3, 1]
    print("Extend Permutation:")
    print("Before permutation:", k)
    print("arr:", arr)
    result = permute(k, arr)
    print("After permutation:", result)
    print("Input Length:", len(k), "Output Length:", len(result))
    print()

def compress_permutation():
    k = "ABCDEFGH"
    arr = [3, 1, 4, 7]
    print("Compress Permutation:")
    print("Before permutation:", k)
    print("arr:", arr)
    result = permute(k, arr)
    print("After permutation:", result)
    print("Input Length:", len(k), "Output Length:", len(result))
    print()

# straight_permutation()
# extend_permutation()
# compress_permutation()
