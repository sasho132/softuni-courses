words = input().split(" ")
palindrome_word = input()
palindromes_list = []

for palindrome in words:
    if palindrome[::-1] == palindrome:
        palindromes_list.append(palindrome)

palindrome_word_count = words.count(palindrome_word)
print(palindromes_list)
print(f"Found palindrome {palindrome_word_count} times")
