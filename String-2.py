# String-2


"""Given a string, return a string where for every char in the original, there are two chars."""
def double_char(str):
    double_str = ""
    for i in str:
        double_str += i * 2
    return double_str


"""Return the number of times that the string "hi" appears anywhere in the given string."""
def count_hi(str):
    hi_count = 0
    for i in range(len(str) - 1):
        if str[i:i + 2] == "hi":
            hi_count += 1
    return hi_count


"""Return True if the string "cat" and "dog" appear the same number of times in the given string."""
def cat_dog(str):
    cat_count = 0
    dog_count = 0
    for i in range(len(str) - 2):
        if str[i:i + 3] == "cat":
            cat_count += 1
        if str[i:i + 3] == "dog":
            dog_count += 1
    return cat_count == dog_count

# A dictionary/hashtable solution:
def cat_dog(str):
    dic = {"cat": 0, "dog": 0}
    for categorie in dic:
        for i in range(len(str) - 2):
            if str[i:i + 3] == categorie:
                dic[categorie] += 1
    return dic["cat"] == dic["dog"]


"""Return the number of times that the string "code" appears anywhere in the given string, 
except we'll accept any letter for the 'd', so "cope" and "cooe" count."""
def count_code(str):
    code_count = 0
    for i in range(len(str) - 3):
        if str[i:i + 2] == "co" and str[i + 3] == "e":
            code_count += 1
    return code_count


"""Given two strings, return True if either of the strings appears at the very end of the other string, 
ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). 
Note: s.lower() returns the lowercase version of a string."""
def end_other(a, b):
    low_a = a.lower()
    low_b = b.lower()
    short_lst = min(len(a), len(b))
    if low_a == low_b[-short_lst:] or low_b == low_a[-short_lst:]:
        return True
    return False


"""Return True if the given string contains an appearance of "xyz" where the xyz is not directly 
preceded by a period (.). So "xxyz" counts but "x.xyz" does not."""
def xyz_there(str):
    for i in range(len(str) - 2):
        if str[i:i + 3] == "xyz" and not str[i - 1] == ".":
            return True
    return False
