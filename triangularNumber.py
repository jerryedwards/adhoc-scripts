# Part 3 - Coding Exercise: Decoding a Message from a Text File
# In this exercise, you will develop a function named decode(message_file). T
# This function should read an encoded message from a .txt file and return its decoded version as a string.

import pandas as pd

message_file = 'triangluarNumInput.txt'


def decode(filename):

    input = pd.read_csv(filename, delimiter=' ', names=['index', 'word'], header=None)
    df = input.sort_values(by = 'index').reset_index(drop=True)

    decodedMessage = ''
    n = 0
    increment = 1

    while n < len(df):
        newNum = n + increment
        decodedMessage += str(df.loc[df['index'] == newNum, 'word'].iloc[0]) + ' ' 
        n = newNum
        increment += 1

    return decodedMessage


if __name__ == '__main__':
    decodedMessage = decode(message_file)
    print(decodedMessage)
