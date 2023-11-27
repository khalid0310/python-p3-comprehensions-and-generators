#!/usr/bin/env python3


def return_evens(sequence):
    """Return a list of all even elements in the sequence."""
    return [num for num in sequence if num % 2 == 0]

def make_exclamation(sentences):
    """Add exclamation marks at the end of each sentence in the list."""
    return [sentence + '!' for sentence in sentences]