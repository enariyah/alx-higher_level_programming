#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    file = dir(hidden_4)
    for name in file:
        if name[:2] != "__":
            print(name)
