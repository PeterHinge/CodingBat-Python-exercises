# Warmup-2


"""Given a string and a non-negative int n, return a larger string that is n copies of the original string."""
def string_times(str, n):
    return str * n


"""Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, 
or whatever is there if the string is less than length 3. Return n copies of the front."""
def front_times(str, n):
    if len(str) >= 3:
        str = str[:3]
    return str * n


"""Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo"."""
def string_bits(str):
    new_str = ""
    for i in range(len(str)):
        if i % 2 == 0:
            new_str += str[i]
    return new_str

# can be returned as list with a comprehension:
def string_bits_alt(str):
    return [str[i] for i in range(len(str)) if i % 2 == 0]


"""Given a non-empty string like "Code" return a string like "CCoCodCode"."""
def string_splosion(str):
    new_str = ""
    for i in range(len(str)):
        new_str += str[:i + 1]
    return new_str

# can be returned as a recursive function:
def string_splosion_alt(str):
    if len(str) == 1:
        return str
    return string_splosion(str[:-1]) + str


"""Given a string, return the count of the number of times that a substring length 2 appears in the string 
and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring)."""
def last2(str):
    if len(str) <= 2:
        return 0
    substr_count = 0
    for i in range(len(str) - 2):
        if str[i:i + 2] == str[-2:]:
            substr_count += 1
    return substr_count

# perhaps the too-short string case isn't necessary, since the for-loop wouldn't be able to execute with len(str) <= 2
# and substr_count remains 0 anyways.


"""Given an array of ints, return the number of 9's in the array."""
def array_count9(nums):
    nine_count = 0
    for n in nums:
        if n == 9:
            nine_count += 1
    return nine_count


"""Given an array of ints, return True if one of the first 4 elements in the array is a 9. 
The array length may be less than 4."""
def array_front9(nums):
    if 9 in nums[0:4]:
        return True
    return False


"""Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere."""
def array123(nums):
    for n in range(len(nums) - 2):
        if nums[n:n + 3] == [1, 2, 3]:
            return True
    return False


"""Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. So 
"xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings."""
def string_match(a, b):
    matches = 0
    shortest_str = min(len(a), len(b))
    for i in range(shortest_str - 1):
        if a[i:i + 2] == b[i:i + 2]:
            matches += 1
    return matches
