def foo(file_name):
    file = open(file_name, "r")
    lines = file.readlines()

    print(lines)

    for i in range(len(lines)):
        print(lines[i])

    file.close()


def main():
    foo("TEST TEXT.txt")


if __name__ == '__main__':
    main()