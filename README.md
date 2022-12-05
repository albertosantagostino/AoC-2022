# Advent of Code 2022 🎄

<div align="center">

| Day                                        | 1   | 2   | 📃                           | ⏲️   |
| ------------------------------------------ | :-: | :-: | :--------------------------: | :--: |
| [01](https://adventofcode.com/2022/day/1)  | ⭐  | ⭐  | [day01.py](src/day01.py)     | 🟢🟢 |
| [02](https://adventofcode.com/2022/day/2)  | ⭐  | ⭐  | [day02.py](src/day02.py)     | 🟢🟢 |
| [03](https://adventofcode.com/2022/day/3)  | ⭐  | ⭐  | [day03.py](src/day03.py)     | 🟢🟢 |
| [04](https://adventofcode.com/2022/day/4)  | ⭐  | ⭐  | [day04.py](src/day04.py)     | 🟢🟢 |
| [05](https://adventofcode.com/2022/day/5)  | ⭐  | ⭐  | [day05.py](src/day05.py)     | 🟢🟢 |

<sub>🟢 < 1 day | 🟡 1÷7 days | 🟠 = 7÷30 days | 💤 > 30 days</sub>

</div>

## Suggested Christmas songs 🔔

- [Chiron Beta Prime 🤖](https://www.youtube.com/watch?v=LUoDmRM2aJ0)
- [The Night Santa Went Crazy 🗡️](https://www.youtube.com/watch?v=0FJU4GrXztE)

## How to run

`Python 3.9` and `poetry` required. From the root folder:

````bash
# Prepare virtualenv (will be placed at .venv/). Only needed the first time
poetry install
# Activate the virtualenv
source .venv/bin/activate
# Run the solution
python3.9 src/day__.py
````

The script `src/day00_template.py` is a template  
Scripts are configured to automatically download puzzle inputs

### Setup (automatic puzzle input download)

To get and set your credentials: login into [AoC](https://adventofcode.com/), open the Web Developer Tools (`CTRL+SHIFT+I`). Go to the `Storage` tab (or `Application/Storage` in Chrome) and copy the value of your `session` cookie into the `aoc_cookie` entry of `config.json`

**Security note**: do not commit the `config.json` file as it contains your personal cookie. Run `git update-index --assume-unchanged config.json` to prevent git from tracking the file
