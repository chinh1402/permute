
# Permutation Examples in Python

This code demonstrates three types of permutations using a simple Python function. The permutations are:

1.  **Straight Permutation**
2.  **Extend Permutation**
3.  **Compress Permutation**

Each permutation type is illustrated with a corresponding function that shows the state of the input before and after permutation, along with the lengths of the input and output.

## Functions

### `permute(k, arr)`

This function takes a string `k` and an array of indices `arr`, and returns a new string formed by permuting the characters in `k` according to the indices in `arr`.

**Parameters:**

-   `k` (str): The input string to be permuted.
-   `arr` (list of int): An array of indices indicating the order of characters in the resulting permutation.

**Returns:**

-   `str`: The permuted string.

### `straight_permutation()`

Demonstrates a straight permutation of the string `k` using a predefined set of indices.

### `extend_permutation()`

Demonstrates an extended permutation by repeating some elements of the string `k` using a predefined set of indices.

### `compress_permutation()`

Demonstrates a compressed permutation by using fewer elements of the string `k` using a predefined set of indices.

## Usage

Uncomment the desired function call at the bottom of the script to see the output of each permutation type.
