from collections import Counter

def main():
    string = "i need some sleep"
    a = string[0:6]
    b = string[7:11]

    print("Main string: " + string)

    print("1) String reverse: " + string_reverse(string))

    print("2) To title: " + string.title())

    print("3) Find unique: " + find_unique(string))

    print("4) List genetator: ", [3*letter for letter in string])

    a, b = b, a
    print("5) Swap values: a-",a,"b-",b)

    print("6) Split on substrings: ", string.split())

    print("7) Join words by symbol: " + ",".join(string.split()))

    print("8) Is palindrome: ", is_palindrome("ababa"), "(ababa)")

    print("9) Count of element 's': ", сount_of_elements(string)["s"])

    print("10) Most common:", сount_of_elements(string).most_common(1))

    print("11) Is anagram? ('ababa', 'baaab'):", is_anagram("ababa", "baaab"))

    dict_1 = {'apple': 9, 'banana': 6}
    dict_2 = {'banana': 4, 'orange': 8}
    print("12) Concat two dicts ({'apple': 9, 'banana': 6}, {'banana': 4, 'orange': 8})", {**dict_1, **dict_2})

    print("13) Is unique? ('1345','1111'):", is_unique("1345"), is_unique("1111"))


def string_reverse(string):
    return string[::-1] 


def find_unique(string):
    uniq_set = set(string)
    return "".join(uniq_set)


def is_palindrome(string):
    if string == string[::-1]:
        return True
    return False

def сount_of_elements(string):
    return Counter(string)


def is_anagram(string_one, string_two):
    if Counter(string_one) == Counter(string_two):
        return True
    return False

def is_unique(string):
    if len(string) == len(set(string)):
        return True
    return False


if __name__ == "__main__":
    main()
