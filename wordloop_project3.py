import numpy as np

def num_letters(n_rows, n_cols): #n_rows, n_cols = data.shape
    return n_rows * n_cols - (n_rows - 2)*(n_cols - 2)

data = np.loadtxt("loop4.csv", delimiter=",", dtype=str, encoding = 'utf8')
words = [] #this will store the letters we extract from the data file
n_rows, n_col = data.shape  #this gives you the number of rows and number of columns in the data file
#collect all letters - fill in your code here

# First row: left to right
for c in range(n_col):
    words.append(str(data[0, c]))

# Last column: top to bottom
for r in range(1, n_rows):
    words.append(str(data[r, n_col - 1]))

# Last row: right to left
for c in range(n_col - 2, -1, -1):
    words.append(str(data[n_rows - 1, c]))

# First column: bottom to top
for r in range(n_rows - 2, 0, -1):
    words.append(str(data[r, 0]))

 
print(words) #check that you collected all the letters in your data file

#assert len(words) == num_letters(rows, columns) 



assert num_letters(3, 4) == 10     #3 is the num_rows and 4 is the num_columns
assert num_letters(13,4) ==30
assert num_letters(4,4) ==12
assert num_letters(6,4) ==16
assert num_letters(6,7) ==22
print("Checking assertions.")
