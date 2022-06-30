def swap( ch):
    return 'B' if (ch == 'G') else 'G'
def swapStartChar(word, exp):
    swapCount = 0
    for i in range(len(word)):
        # if current character is not exp,
        # increase flip count
        if (word[i] != exp):
            swapCount += 1
        # flip exp character each time
        exp = swap(exp)
    return swapCount-1
# method return minimum flip to make binary
# string alternate
def seatingArrange(word):
    # return minimum of following two
    # 1) flips when alternate string starts with 0
    # 2) flips when alternate string starts with 1
    return min(swapStartChar(word, 'G'),
            swapStartChar(word, 'B'))

print(seatingArrange(input()),end='')