# part 2

def epsilon2dec(arr):
    """
    nor the binary number then convert to deciaml
    """
    decimal = 0
    num_bits = len(arr)
    # array was reversed in gamma2edec()
    # arr.reverse()
    print(arr)
    for i in range(num_bits):
        if arr[i] < 0:
            decimal += 2 ** i
            # print(i)
    return(decimal)


def gamma2dec(arr):
    """
    binary array to decimal
    """
    decimal = 0
    num_bits = len(arr)
    arr.reverse()
    print(arr)
    for i in range(num_bits):
        if arr[i] > 0:
            decimal += 2 ** i
            # print(i)
    return(decimal)


def binarystring2dec(str):
    decimal = 0
    num_bits = len(str)
    str = ''.join(reversed(str))
    for i in range(num_bits):
        if int(str[i]) > 0:
            decimal += 2 ** i
    return(decimal)


def next_bit(lines, index, oxygen):
    ones = []
    zeros = []
    for line in lines:
        if line[index] == "1":
            ones.append(line)
        else:
            zeros.append(line)

    if oxygen:
        if len(ones) < len(zeros):
            result = zeros
        else:
            result = ones
    else:  # CO2
        if len(ones) >= len(zeros):
            result = zeros
        else:
            result = ones

    return(result)


def main():

    ones = []
    zeros = []
    keep = []
    input_file = "03-input"

    """
    Oxygen rating
    """
    with open(input_file) as fp:
        for line in fp:
            line = line.strip()
            if line[0] == "1":
                ones.append(line)
            else:
                zeros.append(line)

    if len(ones) < len(zeros):
        keep = zeros
    else:
        keep = ones

    i = 0
    while(len(keep) > 1):
        i += 1
        keep = next_bit(keep, i, True)

    oxygen = binarystring2dec(keep[0])

    print("oxygen = ", oxygen)

    """
    CO2 rating
    """
    if len(ones) > len(zeros):
        keep = zeros
    else:
        keep = ones

    i = 0
    while(len(keep) > 1):
        i += 1
        keep = next_bit(keep, i, False)

    co2 = binarystring2dec(keep[0])

    print("co2 = ", co2)

    print("answer = ", oxygen * co2)


if __name__ == '__main__':
    main()
