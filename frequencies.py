

"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""
def frequencies(items):

    frequencies = {}

    i = 0

    while i < len(items):

        key =str(items[i]);

        if key in frequencies:

            count = frequencies[key]	

            frequencies[key] = count + 1

        else:

            frequencies[key] = 1

        i += 1

    return frequencies

















