def part1():
    with open('inputs/day_1') as file:
        max_cal = 0
        cur_cal = 0
        
        for line in file:
            if line == '\n':
                max_cal = max(cur_cal, max_cal)
                cur_cal = 0
            else:
                val = int(line)
                cur_cal += val
        
        return max_cal

print("Part 1 answer:\n", part1()) 

import heapq

def part2():
    with open('inputs/day_1') as file:
        # This is a min heap but we only push to it cur is larger than smallest
        # So it will always be in reverse order, [third, second, first]
        top_three = []
        heapq.heapify(top_three)

        cur_cal = 0
        
        for line in file:
            if line == '\n':
                if len(top_three) < 3:
                    heapq.heappush(top_three, cur_cal)
                else:
                    if cur_cal > top_three[0]:
                        heapq.heappop(top_three)
                        heapq.heappush(top_three, cur_cal)
                cur_cal = 0
            else:
                val = int(line)
                cur_cal += val
        
        return sum(top_three)

print("Part 2 answer:\n", part2())
