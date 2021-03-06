#!/usr/bin/env python3
"""Retrieve and print words from a URl

Usage:
    python3 words.py <URL>
"""

import sys
from urllib.request import urlopen


def fetch_words(url):
    """Fetch a list of words from a URL.

    Args:
        url: The URL of a utf-8 document

    Returns:
        A list of strings containing the words from document.
    """
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    return story_words


def print_items(items):
    """ Print items one per line

    Args:
        An iterable series of printable items
    """
    for item in items:
        print(item)


def main(url):
    """Print each word from a text document from a url

    Args:
        url: The URL of a utf-8 document
    """
    words = fetch_words(url)
    print_items(words)


if __name__ == '__main__':
    # Accept the url via a command line argument
    main(sys.argv[1])       # The 0th argument is the filename


# 'http://sixty-north.com/c/t.txt'
