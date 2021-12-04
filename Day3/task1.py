from file_util import read_lines


def gamma_rate(lines: list[str], number_len=12) -> str:
    gamma_bin = ""
    for i in range(number_len):
        gamma_bin += '1' if is_gamma_bit(i, lines) else '0'
    return gamma_bin


def is_gamma_bit(i: int, lines: list[str]) -> bool:
    ones = 0
    zeroes = 0
    for bit in lines:
        if bit[i] == '1':
            ones += 1
        else:
            zeroes += 1
    return ones > zeroes


def epsilon_rate(gamma_bin: str) -> str:
    epsilon_bin = ""
    for num in gamma_bin:
        epsilon_bin += '0' if num == '1' else '1'
    return epsilon_bin


def to_decimal(num: str) -> int:
    return int(num, 2)


if __name__ == '__main__':
    lines = read_lines()
    gamma_bin = gamma_rate(lines)
    epsilon_bin = epsilon_rate(gamma_bin)
    print(to_decimal(gamma_bin) * to_decimal(epsilon_bin))
