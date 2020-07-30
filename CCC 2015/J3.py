vowels = 'aeiou'
word = input()
newWord = []
for w in word:
    newWord.append(w)
    if w not in vowels:
        i = ord(w)
        while i > ord('a') and chr(i) not in vowels:
            i -= 1
        j = ord(w)
        while j < ord('z') and chr(j) not in vowels:
            j += 1
        if j == ord('z') or ord(w) - i <= j - ord(w):
            newWord.append(chr(i))
        else:
            newWord.append(chr(j))
        k = ord(w)
        if k != ord('z'):
            k += 1
            while k < ord('z') and chr(k) in vowels:
                k += 1
        newWord.append(chr(k))
print(''.join(newWord))
