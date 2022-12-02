def part1():
    with open('inputs/day_2') as file:
        score = 0
        for line in file:
            opp_choice, my_choice = line.split()
            """
            A / X - Rock
            B / Y - Paper
            C / Z - Scissors

            0 points if loss
            3 points if draw
            6 points if win
            """
            res = {
                "A": {
                    "X": 3,
                    "Y": 6,
                    "Z": 0
                },
                "B": {
                    "X": 0,
                    "Y": 3,
                    "Z": 6
                },
                "C": {
                    "X": 6,
                    "Y": 0,
                    "Z": 3
                }
            }

            if my_choice == 'X':
                score += 1
            elif my_choice == 'Y':
                score += 2
            elif my_choice == 'Z':
                score += 3

            score += res[opp_choice][my_choice]

            # if my_choice == 'X':
            #     score += 1
            #     if opp_choice == 'A':
            #         score += 3
            #     elif opp_choice == 'C':
            #         score += 6
            # elif my_choice == 'Y':
            #     score += 2
            #     if opp_choice == 'B':
            #         score += 3
            #     elif opp_choice == 'A':
            #         score += 6
            # elif my_choice == 'Z':
            #     score += 3
            #     if opp_choice == 'C':
            #         score += 3
            #     elif opp_choice == 'B':
            #         score += 6
            
        return score

print("Part 1 answer:\n", part1())

def part2():
    with open('inputs/day_2') as file:
        score = 0
        for line in file:
            opp_choice, outcome = line.split()
            """
            A - Rock
            B - Paper
            C - Scissors

            X - lose
            Y - draw
            Z - win

            0 points if loss
            3 points if draw
            6 points if win

            1 point if rock
            2 point if paper
            3 point if scissors
            """
            res = {
                "A": {
                    "X": 3,
                    "Y": 1,
                    "Z": 2
                },
                "B": {
                    "X": 1,
                    "Y": 2,
                    "Z": 3
                },
                "C": {
                    "X": 2,
                    "Y": 3,
                    "Z": 1
                }
            }

            if outcome == 'Y':
                score += 3
            elif outcome == 'Z':
                score += 6
            
            score += res[opp_choice][outcome]

        return score

print("Part 2 answer:\n", part2())

