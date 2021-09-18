import os
from collections import deque
import curses

from debugger import debug


def sample(a, b):
    # arr = []
    # for i in range(b):
    #     arr.append(a)
    # return arr
    q = deque()
    for i in range(b):
        q.append(a)
    return q


if __name__ == "__main__":
    os.system('color')
    curses.start_color()
    curses.echo()
    debug(sample, (2, 5))