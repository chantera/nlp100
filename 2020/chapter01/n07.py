def fmt(x, y, z):
    return "{}時の{}は{}".format(x, y, z)


def main():
    print(fmt(x=12, y="気温", z=22.4))


if __name__ == "__main__":
    main()
