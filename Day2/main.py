from file_util import read_lines


def task1():
    lines = read_lines()
    x = 0
    y = 0
    for line in lines:
        line = line.split(" ")
        move = line[0]
        severity = int(line[1])
        if (move == "forward"):
            x += severity
        if (move == "up"):
            y -= severity
        if (move == "down"):
            y += severity
        print(x * y)


def task2():
    lines = read_lines()
    x = 0
    y = 0
    aim = 0
    for line in lines:
        line = line.split(" ")
        move = line[0]
        severity = int(line[1])
        if (move == "forward"):
            x += severity
            y += aim * severity
        if (move == "up"):
            aim -= severity
        if (move == "down"):
            aim += severity
        print(x * y)


if __name__ == '__main__':
    task1()
    task2()
