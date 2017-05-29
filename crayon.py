from __future__ import print_function
"""
Utilities for printing text to terminal using styling, colors, indentation etc.
"""

# System color name constants.
COLORS = (
    BLACK,
    RED,
    GREEN,
    YELLOW,
    BLUE,
    MAGENTA,
    CYAN,
    LIGHT_GRAY,
    DARK_GRAY,
    BRIGHT_RED,
    BRIGHT_GREEN,
    BRIGHT_YELLOW,
    BRIGHT_BLUE,
    BRIGHT_MAGENTA,
    BRIGHT_CYAN,
    WHITE,
) = range(16)

# styling constants
_SET_BOLD = '\033[1m'
_SET_UNDERLINE = '\033[4m'
_SET_FG = '\x1b[38;5;{}m'
_SET_BG = '\x1b[48;5;{}m'
_STYLE_RESET = '\x1b[0m'


def printout(*args, **kwargs):
    """
    Print function with extra options for formating text in terminals.
    """

    # TODO(Lukas): conflicts with function names
    color = kwargs.pop('color', {})
    style = kwargs.pop('style', {})
    prefx = kwargs.pop('prefix', '')
    suffx = kwargs.pop('suffix', '')
    ind = kwargs.pop('indent', 0)

    print_args = []
    for arg in args:
        arg = str(arg)
        arg = colorize(arg, **color)
        arg = stylize(arg, **style)
        arg = prefix(arg, prefx)
        arg = indent(arg, ind)
        arg += str(suffx)
        print_args.append(arg)

    print(*print_args, **kwargs)


def colorize(txt, fg=None, bg=None):
    """
    Print escape codes to set the terminal color.

    fg and bg are indices into the color palette for the foreground and
    background colors.
    """

    setting = ''
    setting += _SET_FG.format(fg) if fg else ''
    setting += _SET_BG.format(bg) if bg else ''
    return setting + str(txt) + _STYLE_RESET


def stylize(txt, bold=False, underline=False):
    """
    Changes style of the text.
    """

    setting = ''
    setting += _SET_BOLD if bold is True else ''
    setting += _SET_UNDERLINE if underline is True else ''
    return setting + str(txt) + _STYLE_RESET


def indent(txt, spacing=4):
    """
    Indent given text using custom spacing, default is set to 4.
    """
    return prefix(str(txt), ''.join([' ' for _ in range(spacing)]))


def prefix(txt, pref):
    """
    Place a prefix in front of the text.
    """
    return str(pref) + str(txt)

# Color value generators
def rgb(red, green, blue):
    """
    Calculate the palette index of a color in the 6x6x6 color cube.

    The red, green and blue arguments may range from 0 to 5.
    """
    for value in (red, green, blue):
        if value not in range(6):
            raise ColorError('Value must be within 0-5, was {}.'.format(value))
    return 16 + (red * 36) + (green * 6) + blue

def gray(value):
    """
    Calculate the palette index of a color in the grayscale ramp.

    The value argument may range from 0 to 23.
    """
    if value not in range(24):
        raise ColorError('Value must be within 0-23, was {}.'.format(value))
    return 232 + value


class ColorError(Exception):
    pass


if __name__ == '__main__':
    # test terminal output by displaying all possible colors and styles

    def print_line(txt, color):
        style = {'bold':True, 'underline':True}
        color_fg = {'fg':color}
        color_bg = {'bg':color}
        printout(txt, color=color_fg, end='')
        printout(colorize(' -> '), end='')
        printout(txt, color=color_fg, style=style, end='')
        printout(colorize(' -> '), end='')
        printout('        ', color=color_bg)

    for color in COLORS:
        txt = 'System color: {:2.0f}'.format(color)
        print_line(txt, color)

    for color in range(24):
        txt = 'Gray color: {:2.0f}'.format(color)
        print_line(txt, gray(color))

    for r in range(6):
        for g in range(6):
            for b in range(6):
                txt = 'rgb({},{},{})'.format(r, g, b)
                print_line(txt, rgb(r, g, b))
