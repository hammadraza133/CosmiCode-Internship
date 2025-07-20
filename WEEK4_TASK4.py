def char_frequency(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq

# Example to run code
s = "hello world"
print(char_frequency(s))
