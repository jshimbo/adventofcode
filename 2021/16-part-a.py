import sys


input_file = 'input/16-input'


with open(input_file if len(sys.argv) < 2 else sys.argv[1], encoding="utf-8") as f:
    data = list(f.read().strip())

input_hex = data
hexptr = 0
odometer = 0


def getbit():
    global input_hex, hexptr, odometer
    if hexptr == 0:
        getbit.bitptr = 4
    if getbit.bitptr > 3 or hexptr == 0:
        int_value = int(input_hex[hexptr], base=16)
        hexptr += 1
        getbit.bitpool = format(int_value, "04b")
        getbit.bitptr = 0
    res = getbit.bitpool[getbit.bitptr]
    getbit.bitptr += 1
    odometer += 1
    return res


getbit.bitpool = ''
getbit.bitptr = 99  # garbage value greater than sizeof(byte)


def get_bits(n):
    s = ""
    for i in range(n):
        s += getbit()
    return s


def get_packet_version():
    bits = get_bits(3)
    # print(bits)
    return(int(bits, 2))


def get_packet_type():
    bits = get_bits(3)
    # print(bits)
    return(int(bits, 2))


def get_literal_value():
    numbits = 0
    res = ""

    start_bit = getbit()
    while start_bit == '1':
        res += get_bits(4)
        start_bit = getbit()
        numbits += 5
    # one more time
    res += get_bits(4)
    numbits += 5

    return res, numbits


def get_operator_packet():
    num_bits = 0
    length_type_id = get_bits(1)
    if length_type_id == '0':
        # next 15 bits are a number that represents
        # the total length in bits of the sub-packets
        # contained by this packet
        s = get_bits(15)
        num_bits = 15
    else:
        s = get_bits(11)
        num_bits = 11

    return int(s, 2), num_bits


def process_packet():
    global odometer
    pkt_version = get_packet_version()
    result = pkt_version
    # print("NEW packet version", pkt_version)
    pkt_type = get_packet_type()
    if pkt_type == 4:
        # literal value
        literal_value, _ = get_literal_value()
        # print("    Type 4 literal value", int(literal_value, 2))
    else:
        # operator packet
        s, num = get_operator_packet()
        if num == 11:
            # get num packets
            num_packets = s
            # print("    Operator packet with",  num_packets, "subpackets")
            for _ in range(num_packets):
                result += process_packet()
        else:
            # get number of bits
            subpacket_bits = s
            # print("    Operator packet with", subpacket_bits, "subpacket bits")
            odo_start = odometer
            while subpacket_bits > (odometer - odo_start):
                # print(" ", subpacket_bits, "bits left")
                result += process_packet()
    # print("RTN")
    return result


answer1 = 0
answer1 += process_packet()

print("Answer 1 is", answer1)
print("Hex odometer reading", hexptr)
