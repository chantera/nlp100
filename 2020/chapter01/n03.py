def main():
    s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."  # NOQA
    lengths = [len(w) for w in s.replace(',', '').rstrip('.').split()]
    print(lengths)


if __name__ == "__main__":
    main()
