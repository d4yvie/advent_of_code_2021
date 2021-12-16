from print_aoc import print_task1, print_task2
from math import prod
from file_util import read_first_line


class Decoder:

    def __init__(self, file_data: str):
        rawdata = bytes.fromhex(file_data)
        self.bits = ''.join(map('{:08b}'.format, rawdata))
        self.pos = 0

    def decode_int(self, nbits: int) -> int:
        res = int(self.bits[self.pos:self.pos + nbits], 2)
        self.pos += nbits
        return res

    def decode_n_packets(self, n: int) -> list[tuple[int, int, int]]:
        return [self.decode_one_packet() for _ in range(n)]

    def decode_len_packets(self, length: int) -> list[tuple[int, int, int]]:
        end = self.pos + length
        while self.pos < end:
            yield self.decode_one_packet()

    def decode_value_data(self) -> int:
        value = 0
        group = 0b10000
        while group & 0b10000:
            group = self.decode_int(5)
            value = (value << 4) + (group & 0b1111)
        return value

    def decode_operator_data(self) -> int | list[tuple[int, int, int]]:
        return self.decode_n_packets(self.decode_int(11)) if \
            self.decode_int(1) else \
            [i for i in self.decode_len_packets(self.decode_int(15))]

    def decode_packet_data(self, tid: int) -> int | list[tuple[int, int, int]]:
        if tid == 4:
            return self.decode_value_data()
        return self.decode_operator_data()

    def decode_one_packet(self) -> tuple[int, int, int]:
        version = self.decode_int(3)
        tid = self.decode_int(3)
        data = self.decode_packet_data(tid)
        return version, tid, data


VALUE_OPERATION_DICT = {
    0: sum,
    1: prod,
    2: min,
    3: max,
    4: lambda x: x,
}

TUPLE_OPERATION_DICT = {
    5: lambda a, b: int(a > b),
    6: lambda a, b: int(a < b),
    7: lambda a, b: int(a == b),
}


def evaluate(packet) -> int:
    _, tid, data = packet
    if tid == 4:
        return data
    values = map(evaluate, data)
    try:
        return VALUE_OPERATION_DICT[tid](values)
    except KeyError:
        pass
    a, b = values
    try:
        return TUPLE_OPERATION_DICT[tid](a, b)
    except KeyError:
        raise NotImplementedError(f'Unimplemented tid={tid}')


def sum_versions(packet: tuple[int, int, int]) -> int:
    v, tid, data = packet
    return v if tid == 4 else v + sum(map(sum_versions, data))


if __name__ == "__main__":
    decoder = Decoder(read_first_line())
    packet = decoder.decode_one_packet()
    print_task1(16, sum_versions(packet))
    print_task2(16, evaluate(packet))
