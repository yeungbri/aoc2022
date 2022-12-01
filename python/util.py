import requests
import datetime
import subprocess
import os
import textwrap

session_token = os.environ.get("AOC_SESSION")


if __name__ == '__main__':
    cur_day = int(datetime.datetime.now().strftime("%d"))
    if cur_day <= 25:
        input_file = f'inputs/day_{cur_day}'
        solution_file = f'python/solutions/day_{cur_day}.py'

        def get_input():
            if not os.path.exists(input_file):
                resp = requests.get(f"https://adventofcode.com/2022/day/{cur_day}/input", cookies={"session": session_token})
                # print(resp.text)
                with open(input_file, 'w') as f:
                    f.write(resp.text)
        get_input()

        def create_solution_file():
            if not os.path.exists(solution_file):
                with open(solution_file, 'w+') as f:
                    f.write(textwrap.dedent(
                        f"""\
                        def part1():
                            with open('{input_file}') as file:
                                for line in file:
                                    pass\n
                        print("Part 1 answer:\\n", part1())\n
                        """
                    ))
        create_solution_file()

        def append_part2():
            if os.path.exists(solution_file):
                with open(solution_file) as f:
                    if 'part2' in f.read():
                        return

                with open(solution_file, 'a+') as f:
                    f.write(textwrap.dedent(
                        f"""\
                        def part2():
                            with open('{input_file}') as file:
                                for line in file:
                                    pass\n
                        print("Part 2 answer:\\n", part2())\n
                        """
                    ))
        append_part2()

        def run_solution():
            subprocess.call(f"python3 {solution_file}", shell=True)
        run_solution()