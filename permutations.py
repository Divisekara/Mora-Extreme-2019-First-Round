def permutations_with_repetition(s):
    base = len(s)
    for n in range(base**base):
        yield "".join(s[n // base**(base-d-1) % base] for d in range(base))

number="1234123412341234123412341234123412341234123412341234123412341234123412341234123412341234123412341234123412341234123412341234123412341234123412341234123412341234123412341234"
number_=number[:5]
for p in permutations_with_repetition(number):
    print(p)
