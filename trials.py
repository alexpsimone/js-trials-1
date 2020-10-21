"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    """Print each item in the given array.
    
    
    >>> output_all_items([1, 'hello', True])
    1
    hello
    True
    """
    for item in items:
        print(item)


def get_all_evens(nums):
    """Given an array of numbers, return an array of all even numbers.
    
    >>> get_all_evens([7, 8, 10, 1, 2, 2])
    [8, 10, 2, 2]
    """

    return [num for num in nums if num % 2 == 0]


def get_odd_indices(items):
    """Given an array, return all elements at odd numbered indices.
    
    >>> get_odd_indices([1, 'hello', True, 500])
    ['hello', 500]
    """

    # Alternate solution:
    # return [item for item in items[1::2]]

    return [item for item in items if items.index(item) % 2 != 0]

def print_as_numbered_list(items):
    """Given an array, output a numbered list.
    
    >>> print_as_numbered_list([1, 'hello', True])
    1. 1
    2. hello
    3. True
    """

    number = 1
    for item in items:
        print(f"{number}. {item}")
        number += 1


def get_range(start, stop):
    """Return an array of numbers in a certain range.
    
    >>> get_range(0, 5)
    [0, 1, 2, 3, 4]
    
    >>> get_range(1, 3)
    [1, 2]

    >>> get_range(6, 10)
    [6, 7, 8, 9]
    """

    return [start + num for num in range(stop-start)]


def censor_vowels(word):
    """Given a string, return a string where vowels are replaced with '*'.
    
    >>> censor_vowels('hello world')
    'h*ll* w*rld'
    """

    # This alternate solution is "fancy" but harder to 
    # understand at a glance, I think:
    #
    # newstring = ['*' if letter in 'aeiou' else letter for letter in word]
    # return ''.join(newstring)

    newstring = ''

    for letter in word:
        if letter in 'aeiou':
            newstring += '*'
        else:
            newstring += letter
    
    return newstring


def snake_to_camel(string):
    pass  # TODO: replace this line with your code


def longest_word_length(words):
    pass  # TODO: replace this line with your code


def truncate(string):
    pass  # TODO: replace this line with your code


def has_balanced_parens(string):
    pass  # TODO: replace this line with your code


def compress(string):
    pass  # TODO: replace this line with your code
