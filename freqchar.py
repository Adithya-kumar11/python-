def char_frequence(text):
    freq = {}
    for ch in text:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
    return freq
s="adithya kumar"
print(char_frequence(s))