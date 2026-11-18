


def num_letters(n_rows, n_cols): #n_rows, n_cols = data.shape
    return n_rows * n_cols - ((n_rows - 2)*(n_cols - 2))

assert num_letters(3, 4) == 10     #3 is the num_rows and 4 is the num_columns
assert num_letters(13,4) ==30
assert num_letters(4,4) ==12
assert num_letters(6,4) ==16
assert num_letters(6,7) ==22
print("Checking assertions.")
