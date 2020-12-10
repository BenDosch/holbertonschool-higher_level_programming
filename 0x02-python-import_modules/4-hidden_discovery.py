#!/usr/bin/python3
def main():
    import hidden_4
    for name in dir(hidden_4):
        if name[:2] != "__":
            print(name)

if __name__ == "__main__":
    main()
