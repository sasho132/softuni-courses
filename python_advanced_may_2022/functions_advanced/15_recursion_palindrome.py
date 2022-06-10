def palindrome(word, index):
    if index == len(word) // 2:
        return f"{word} is a palindrome"
    first_ch = word[index]
    second_ch = word[len(word) - 1 - index]
    if first_ch != second_ch:
        return f"{word} is not a palindrome"
    return palindrome(word, index + 1)


# print(palindrome("abcba", 0))
print(palindrome("peter", 0))

'''
def recursive_power(number, power):
    result = 1
    if power == 0:
        return result
    result = number * recursive_power(number, power - 1)
    return result
'''