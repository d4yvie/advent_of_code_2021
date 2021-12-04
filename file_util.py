def read_lines(file_name="measurements") -> list[str]:
    with open(file_name) as f:
        return [line.strip() for line in f]


def read_line_seperated_data_sets(file_name="measurements") -> list[str]:
    with open(file_name) as f:
        return f.read().rstrip().split('\n\n')
