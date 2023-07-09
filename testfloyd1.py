import sys
from floyd import floyd_recursive


def test_floyd_recursive():
    # Test case 1
    graph = [[0, 5, sys.maxsize, 10],
             [sys.maxsize, 0, 3, sys.maxsize],
             [sys.maxsize, sys.maxsize, 0, 1],
             [sys.maxsize, sys.maxsize, sys.maxsize, 0]]
    expected = [[0, 5, 8, 9],
                [sys.maxsize, 0, 3, 4],
                [sys.maxsize, sys.maxsize, 0, 1],
                [sys.maxsize, sys.maxsize, sys.maxsize, 0]]
    assert floyd_recursive(graph, len(graph)) == expected

    # Test case 2
    graph = [[0, 3, sys.maxsize, 7],
             [8, 0, 2, sys.maxsize],
             [5, sys.maxsize, 0, 1],
             [2, sys.maxsize, sys.maxsize, 0]]
    expected = [[0, 3, 5, 6],
                [5, 0, 2, 3],
                [3, 6, 0, 1],
                [2, 5, 7, 0]]
    assert floyd_recursive(graph, len(graph)) == expected

    # Add more test cases as needed

