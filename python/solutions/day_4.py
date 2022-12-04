# Interval problem
def part1():
    with open('inputs/day_4') as file:
        res = 0
        for line in file:
            line = line.strip()
            pair_str = line.split(',')
            
            first = pair_str[0].split('-')
            first = list(map(lambda str: int(str), first))

            second = pair_str[1].split('-')
            second = list(map(lambda str: int(str), second))
            # print(first, second)

            # Is first inside of second?
            if first[0] >= second[0] and first[1] <= second[1]:
                res += 1
                # print(first, second)
            # Is second inside of first?
            elif second[0] >= first[0] and second[1] <= first[1]:
                res += 1
                # print(first, second)
        return res
                

print("Part 1 answer:\n", part1())

def part2():
    with open('inputs/day_4') as file:
        res = 0
        cnt = 0
        for line in file:
            line = line.strip()
            pair_str = line.split(',')
            
            first = pair_str[0].split('-')
            first = list(map(lambda str: int(str), first))

            second = pair_str[1].split('-')
            second = list(map(lambda str: int(str), second))

            # Is first completely in front of second?
            if first[1] < second[0]:
                res += 1
                print(first, second)
            # Is second completely in front of first?
            elif second[1] < first[0]:
                res += 1
                print(first, second)
            cnt += 1
        return cnt - res

print("Part 2 answer:\n", part2())

