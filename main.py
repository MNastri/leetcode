import typing as t

from os import listdir
from os.path import (
    isdir,
    join,
)

BASE_FOLDER = "problems"
DIFFICULTIES = {0, 1, 2}


def get_problem_number(filename: str) -> int:
    """Returns the problem number from a directory name."""
    return int(filename[1:5])


def get_problem_difficulty(filename: str) -> int:
    """Returns the problem difficulty from a directory name."""
    return int(filename[6:7])


def get_problems_by_difficulty() -> t.List[t.List[int]]:
    """Returns the list of problems by difficulty."""
    files = listdir(BASE_FOLDER)
    files = [ff for ff in files if isdir(join(BASE_FOLDER, ff)) and ff.startswith("p")]
    all_problems = [
        (get_problem_number(filename=ff), get_problem_difficulty(filename=ff))
        for ff in files
    ]
    solved_problems = []
    for difficulty in DIFFICULTIES:
        problems_by_difficulty = [nn for nn, dd in all_problems if dd == difficulty]
        solved_problems += (problems_by_difficulty,)
    return solved_problems


if __name__ == "__main__":
    solved = get_problems_by_difficulty()
    for idx, diff in enumerate(solved):
        print(f"Dificuldade {idx} - Problemas ({len(diff):^4}): {diff}")
