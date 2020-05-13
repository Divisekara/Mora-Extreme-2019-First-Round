
def get_longest_palindromes(strng):
    N = len(strng)
    ans = []

    for l in range(N, 0, -1):   # 1.
        found = False
        for s in range(N-l+1):  # 2.
            target = strng[s:s+l]
        if target == target[::-1]:  # 3.
                ans.append(strng[s:s+l])
                found = True
        if found:
            break

    return ans if strng else ['']


print get_longest_palindromes("raceofcar")
