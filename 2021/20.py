import sys


def print_image(image, really=False):
    if really:
        for row in image:
            scanline = ''
            for pixel in row:
                scanline += pixel
            print(scanline)

    print(len(image[0]), "W x", len(image), "H")
    print("Brightness is", brightness(image))
    print('')
    return


def brightness(image):
    return sum([c == '#' for row in image for c in row])


def evaluate_row(row, image, filter, margin, round):
    height = len(image)
    width = len(image[0])
    result = ''
    if round % 2 == 0:
        # on even rounds, intergalactic space is '.'
        hyperspace = '0'
    else:
        hyperspace = '1'

    for col in range(-margin, width + margin):
        pixel = ''
        # splitting into easy and hard is much fatser
        if 0 < col < (width - 1) and 0 < row < (height - 1):
            # the easy way
            for y in range(row-1, row+2):
                for x in range(col-1, col+2):
                    p = image[y][x]
                    pixel += '1' if p == '#' else '0'
        else:
            # the hard way
            for y in range(row-1, row+2):
                for x in range(col-1, col+2):
                    if 0 <= x < width and 0 <= y < height:
                        p = image[y][x]
                        pixel += '1' if p == '#' else '0'
                    else:
                        pixel += hyperspace
        pixel = int(pixel, 2)
        value = filter[pixel]
        result += value
    return result


def main():
    margin = 1  # grow image to take care of edges
    found_image = False  # in case of multi-line filters
    image = []
    filter = ''

    if len(sys.argv) >= 2:
        input_file = sys.argv[1]
    else:
        input_file = 'input/20-input'

    if len(sys.argv) >= 3:
        rounds = int(sys.argv[2])
    else:
        rounds = 50

    lines = [l.strip() for l in open(input_file)]

    for l in lines:
        if len(l) == 0:
            found_image = True
        elif found_image:
            image.append(l)
        else:
            # the filter is multi-line in the instructions
            filter += l

    if len(filter) != 512:
        print("Error: wrong filter size")
        sys.exit()

    # print_image(image, True)

    for round in range(rounds):
        # print("Round", round)
        height = len(image)

        new_image = []
        for y in range(-margin, height + margin):
            row = evaluate_row(y, image, filter, margin, round)
            new_image.append(row)

        image = new_image
        # print_image(image, False)

    print_image(image, False)
    answer1 = brightness(image)
    print("Answer:", answer1)


if __name__ == '__main__':
    main()
