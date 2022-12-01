# Usage
1. Export your AOC session token

You can find your AOC session token in the cookie of AOC.

`
echo \AOC_SESSION={your_token} >> .env
source .env
`

`export AOC_SESSION={your_token}`

2. From the root dir, run the script to generate files for the current day and run solutions

Each time it is run, it will try to fetch input, create template solution, add a part2, run
the solution as needed for the current day.

```
cd aoc2022
python3 util.py
```