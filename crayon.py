from __future__ import print_function
"""
Utilities for displaying text in terminals using styling, colors, indentation etc.
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

BOLD = '\033[1m'
UNDERLINE = '\033[4m'


def printout(*args, **kwargs):
    """
    Print function with extra options for formating text in terminals.
    """
    # unpack parameters
    color = kwargs.pop('color', {})
    spacing = kwargs.pop('indent', 0)
    pref = kwargs.pop('prefix', '')
    suf = kwargs.pop('suffix', '')
    style = kwargs.pop('style', {})

    # unwrap text from list of arguments and modify it
    args = list(args)
    args[0] = colorize(args[0], **color)
    args[0] = stylize(args[0], **style)
    args[0] = prefix(args[0], pref)
    args[0] += str(suf)
    args[0] = indent(args[0], spacing)
    args = tuple(args)
    print(*args, **kwargs)


def colorize(txt, **color):
    """
    Print escape codes to set the terminal color.

    fg and bg are indices into the color palette for the foreground and
    background colors.
    """
    if not color:
        return txt
    fg = color.pop('fg', None)
    bg = color.pop('bg', None)
    setting = ''
    setting += '\x1b[38;5;{}m'.format(fg) if fg else ''
    setting += '\x1b[48;5;{}m'.format(bg) if bg else ''
    return setting + txt + '\x1b[0m'


def indent(txt, spacing=4):
    """
    Indent given text using custom spacing, default is set to 4.
    """
    return prefix(txt, ''.join([' ' for _ in range(spacing)]))


def prefix(txt, pref):
    """
    Place a prefix in front of the text.
    """
    return str(pref) + txt


def stylize(txt, **style):
    """
    Changes style of the text.
    """
    if not style:
        return txt
    bold = style.pop('bold', None)
    underline = style.pop('underline', None)
    setting = ''
    setting += '\033[1m' if bold else ''
    setting += '\033[4m' if underline else ''
    return setting + txt + '\033[0m'


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
