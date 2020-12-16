#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        info = (0, None)
        return info
    else:
        info = (len(sentence), sentence[0])
        return info


def main():
    sentence = "At Holberton school, I learnt C!"
    length, first = multiple_returns(sentence)
    print("Length: {:d} - First character: {}".format(length, first))


if __name__ == "__main__":
    main()
