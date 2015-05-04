from __future__ import print_function

def rgb(red, green, blue):
    return 16 + (red * 36) + (green * 6) + blue

def set_color(fg=None, bg=None):
    print(_set_color(fg, bg), end='')

def _set_color(fg=None, bg=None):
    result = ''
    if fg:
        result += '\x1b[38;5;%dm' % fg
    if bg:
        result += '\x1b[48;5;%dm' % bg
    return result

def reset_color():
    print(_reset_color(), end='')

def _reset_color():
    return '\x1b[0m'

def print_color(*args, **kwargs):
    fg = kwargs.pop('fg', None)
    bg = kwargs.pop('bg', None)
    set_color(fg, bg)
    print(*args, **kwargs)
    reset_color()

def format_color(string, fg=None, bg=None):
    return _set_color(fg, bg) + string + _reset_color()
