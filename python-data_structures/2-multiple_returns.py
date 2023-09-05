def multiple_returns(sentence):
    length = len(sentence)
    if length == 0:
        first = None
    else:
        first = sentence[0]
    return length, first

if __name__ == "__main__":
    sentence = "At Holberton school, I learnt C!"
    length, first = multiple_returns(sentence)
    print("Length: {:d} - First character: {}".format(length, first))
