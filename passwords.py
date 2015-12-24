#!/usr/bin/python3

# takes up to five arguments
# each of those is a survey of the password input selections from
# keep talking and nobody explodes
# returns the list of passwords from the game that are valid

import sys

# get the list of passwords from a file
def getPasswords(filename):
    with open(filename, 'r') as passwordFile:
        passwords = passwordFile.read().splitlines()
    return passwords

def checkForValidPasswords(passwords, inputs):
    toDelete = []
    # this declaration seems weird, but the index is the important part
    for i in range(len(inputs)):
        for password in passwords:
            # if the letter that we're looking at is in the relevant listing
            if not password[i] in inputs[i]:
                # this whole toDelete thing is because of a quirk in list handling
                # you can't pop from a list while iterating over it, or it gets
                # messed up
                toDelete.append(password)
        for password in toDelete:
            passwords.remove(password)
        toDelete = []
    return passwords

if __name__ == '__main__':
    passwords = getPasswords('passwords')
    inputStrings = sys.argv[1:]
    matches = checkForValidPasswords(passwords, inputStrings)
    print('matches:')
    for match in matches:
        print(match)
