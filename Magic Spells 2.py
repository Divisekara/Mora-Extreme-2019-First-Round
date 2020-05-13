n = int(input())
s = int(input())
red = list(map(int, input().strip().split()))[:-1]
yellow = list(map(int, input().strip().split()))[:-1]

x = [1]*n

def get_spell(spell_index):
    if spell_index == 0:
        return lambda x: True
    if spell_index == 1:
        return lambda x: (x % 2 == 1)
    if spell_index == 2:
        return lambda x: (x % 2 == 0)
    if spell_index == 3:
        return lambda x: (x % 3 == 1)

def swap_all(spell_index):
    for i in range(n):
        x[i] = swap(i, x[i], get_spell(spell_index))

def swap(index, value, spell):
    if spell(index + 1) == True:
        return (value + 1) % 2
    return value

def get_group(index):
    if index % 6 == 4:
        return 0
    if index % 2 == 0:
        return 1
    if index % 6 == 1:
        return 2
    if index % 2 == 1:
        return 3

answers = set()
for spell_1 in range(2):
    for spell_2 in range(2):
        for spell_3 in range(2):
            for spell_4 in range(2):
                x = [1]*n
                if spell_1 == 1:
                    swap_all(0)
                if spell_2 == 1:
                    swap_all(1)
                if spell_3 == 1:
                    swap_all(2)
                if spell_4 == 1:
                    swap_all(3)

                for i in range(n):
                    if x[i] == 1 and i + 1 in yellow:
                        break
                    if x[i] == 0 and i + 1 in red:
                        break
                else:
                    min_spells = spell_1 + spell_2 + spell_3 + spell_4
                    if s < min_spells:
                        continue
                    if s % 2 != min_spells % 2:
                        continue
                    answers.add(tuple(x))

answers = sorted(answers)
for answer in answers:
    print("".join(map(str, answer)))

if len(answers) == 0:
    print("IMPOSSIBLE")