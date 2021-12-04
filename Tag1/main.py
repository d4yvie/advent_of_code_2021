from file_util import read_lines


def task1():
    f = open("measurements", "r")
    this_val = 0
    last_val = 0
    counted = 0
    lines = 0
    for x in f:
        if int(x) > 0:
            lines += 1
            this_val = int(x)
            if this_val > last_val:
                counted += 1
            last_val = int(x)
    counted -= 1
    print(f'The result is: {counted}')
    print(f'The number of lines are: {lines}')


def task2():
    lines = read_lines()
    counted = 0
    for third_line in range(3, len(lines)):
        if lines[third_line] + lines[third_line - 1] + lines[third_line - 2] > lines[third_line - 1] + lines[third_line - 2] + lines[third_line - 3]:
            counted += 1
    print(f'The result is: {counted}')
    print(f'The number of lines are: {len(lines)}')


if __name__ == '__main__':
    task1()
    task2()
