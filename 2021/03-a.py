def epsilon2dec(arr):
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
    decimal = 0
    num_bits = len(arr)
    arr.reverse()
    print(arr)
    for i in range(num_bits):
        if arr[i] > 0:
            decimal += 2 ** i
            # print(i)
    return(decimal)


def main():

    gamma = []
    first_line = True
    num_lines = 0

    with open("03-input") as fp:
        for line in fp:
            line = line.strip()
            num_bits = len(line)
            if first_line:
                first_line = False
                for x in range(num_bits):
                    if line[x] == "1":
                        gamma.append(1)
                    else:
                        gamma.append(-1)
            else:
                for x in range(num_bits):
                    if line[x] == "1":
                        gamma[x] += 1
                    else:
                        gamma[x] -= 1

    print(gamma)
    gamma_decimal = gamma2dec(gamma)
    print(gamma_decimal)
    epsilon_decimal = epsilon2dec(gamma)
    print(epsilon_decimal)
    print("answer")
    print(epsilon_decimal * gamma_decimal)


if __name__ == '__main__':
    main()
