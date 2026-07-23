# Implement, in your choice of language, a hash function that takes a String as a parameter.
# Utilize at least two of the methods discussed in the notes.  Use comments to indicate which methods you are using.

def hashing(key, table_size):
    # EXTRACTION METHOD
    # Use parts(s) of the key value to compute the hash - convert first, middle, and last characters to ASCII values.
    # ord() is a built- in python function that returns Unicode (ASCII) values
    first_char = ord(key[0])
    middle_char  = ord(key[len(key) // 2])
    last_char = ord(key[-1])

    # Combine the extracted values into a number
    ascii_val = first_char + middle_char + last_char

    # DIVISION METHOD
    # Return the hashed value by moding the table size (m)
    return ascii_val % table_size

# Division method works best with prime numbers
table_size = 31
words = ["apple", "banana", "computer", "python", "hashing"]

for word in words:
    print(f"{word:10} -> {hashing(word, table_size)}")