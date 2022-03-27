import os
import typing as t

from os import listdir
from os.path import (
    isdir,
    join,
)

BASE_FOLDER = "problems"
DIFFICULTIES = {0, 1, 2, 3, 4}


def get_problem_number(filename: str) -> str:
    """Returns the problem number from a directory name."""
    return filename[1:5]


def get_problem_difficulty(filename: str) -> int:
    """Returns the problem difficulty from a directory name."""
    return int(filename[6:7])


def get_problem_name(filename: str) -> str:
    """Returns the problem name from a directory name."""
    return filename[8:]


def offset_problem_difficulty(offset: int) -> None:
    """Renames all problem packages adding offset to their difficulty. Offset
    can be negative.
    """
    files = listdir(BASE_FOLDER)
    files = [ff for ff in files if isdir(join(BASE_FOLDER, ff)) and ff.startswith("p")]
    numbers = [get_problem_number(ff) for ff in files]
    difficulties = []
    for ff in files:
        diff = get_problem_difficulty(ff) + offset
        assert (
            diff in DIFFICULTIES
        ), f"A nova dificuldade {diff} para {ff} não está prevista"
        difficulties += (diff,)
    names = [get_problem_name(ff) for ff in files]
    new_file_str = "p{number}_{difficulty}_{name}"
    new_files = [
        new_file_str.format(number=num, difficulty=dd, name=name)
        for num, dd, name in zip(numbers, difficulties, names)
    ]
    assert len(files) == len(new_files)
    for src, dst in zip(files, new_files):
        os.rename(os.path.join(BASE_FOLDER, src), os.path.join(BASE_FOLDER, dst))


# if __name__ == "__main__":
#     offset_problem_difficulty(1)


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
        problems_by_difficulty = [
            int(nn) for nn, dd in all_problems if int(dd) == difficulty
        ]
        solved_problems += (problems_by_difficulty,)
    return solved_problems


def count_problems() -> t.List[int]:
    """Returns the count of problems in each difficulty."""
    solved_problems = get_problems_by_difficulty()
    counts = [ll for ll in map(len, solved_problems)]
    return counts


def get_easiness_ratios() -> t.List[float]:
    """In relation to the hardest difficulty."""
    counts = count_problems()
    ratios = []
    end = len(counts)-1
    while end >= 0 and counts[end] == 0:
        end -= 1
    for diff in counts:
        if diff != 0:
            ratios += (diff / counts[end],)
        elif diff == 0:
            ratios += (0,)
    return ratios


if __name__ == "__main__":
    solved = get_problems_by_difficulty()
    biggest_count = max(count_problems())
    charact_of_count = len(str(biggest_count))
    whitespace = " " * charact_of_count
    for idx, diff in enumerate(solved):
        len_of_diff = (whitespace + str(len(diff)))[-charact_of_count:]
        print(f"Dificuldade {idx} - Problemas ({len_of_diff}): {diff}")
    diff_ratios = get_easiness_ratios()
    print(f"Proporção de facilidade: {diff_ratios}")
