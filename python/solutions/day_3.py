def priority(c):
    if c.islower():
        # 'a' is 97 in ascii, ord gives unicode code point of char
        priority = ord(c) - 96
    elif c.isupper():
        # 'A' is 65 in ascii, add back 26 for the lower case chars
        priority = ord(c) - 64 + 26
    return priority

def part1():
    with open('inputs/day_3') as file:
        res = 0
        for line in file:
            sz = len(line)
            seen = set()
            for i in range(sz//2):
                seen.add(line[i])
            # print('--')
            for i in range(sz//2,sz):
                if line[i] in seen:
                    appears_both = line[i]
                    res += priority(appears_both)
                    
                    # Forgot this break in here after finding the duped char
                    break
        return res

print("Part 1 answer:\n", part1())

def part2():
    with open('inputs/day_3') as file:
        common = None
        res = 0
        for idx, line in enumerate(file):
            line = line.strip()
            if idx % 3 == 0:
                common = set(line)
            new_common = set()
            for c in common:
                if c in line:
                    new_common.add(c)
            common = new_common
            if idx % 3 == 2:
                print(common)
                assert len(common) == 1
                res += priority(common.pop())
        return res

print("Part 2 answer:\n", part2())

