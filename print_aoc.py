def print_answer(day: int, task: int, answer: int | str) -> None:
    print(f"Answer of day {day} task {task} is {answer}")


def print_task1(day: int, answer: int | str) -> None:
    print_answer(day, 1, answer)


def print_task2(day: int, answer: int | str) -> None:
    print_answer(day, 2, answer)


def finish_task1(day: int, answer: int | str, expected: int | str = "") -> int | str:
    print_task1(day, answer)
    return check_expected(answer, expected)


def finish_task2(day: int, answer: int | str, expected: int | str = "") -> int | str:
    print_task2(day, answer)
    return check_expected(answer, expected)


def check_expected(answer: int | str, expected: int | str = "") -> int | str:
    if expected and asserter_active():
        assert answer == expected
    return answer


def asserter_active() -> bool:
    return True
