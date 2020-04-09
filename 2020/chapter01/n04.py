def main():
    s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."  # NOQA
    idxs = {1, 5, 6, 7, 8, 9, 15, 16, 19}
    d = {i + 1: w[:2 - int(i + 1 in idxs)] for i, w in enumerate(s.split())}
    print(d)


if __name__ == "__main__":
    main()
