# crayon
[![PyPI](https://img.shields.io/pypi/v/crayon.svg)](https://pypi.python.org/pypi/crayon/) [![PyPI](https://img.shields.io/pypi/status/crayon.svg)](https://pypi.python.org/pypi/crayon/) [![PyPI](https://img.shields.io/pypi/pyversions/crayon.svg)](https://pypi.python.org/pypi/crayon/) [![License](https://img.shields.io/badge/license-MIT-lightgrey.svg)](https://raw.githubusercontent.com/lukaskubis/crayon/master/LICENSE)

![Imgur](http://i.imgur.com/LznDkYy.gif)

Minimal python utility for styling your terminal output. The idea here is to use a wrapper to add styling options for print function. Let me explain...

    pip install crayon

To test your terminal output just launch the crayon module

## How-to
Define your preferred style as a dictionary
```python
from crayon import *

my_style = dict(prefix='* ', # prefix
                color= dict(fg=rgb(5, 3, 1), bg=BLUE),
                style= dict(bold=True),
                indent=4,

                # you can also set 'print' function kwargs
                sep=' *\n',
                end=' *\n***\n')
```
Call function `printout` the same way as `print`. If you used `print` function keywords, they get passed to it as usual. Example:

```python
printout(False, "Hello", 4, **my_style)
```

### Colors
The default 16 terminal colors are set as constants for easy access.

```python
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
```

The grayscale supports 24 values.
```python
my_grayscale_color = gray(10) # (0 - 23)
```

The rest is set by `rgb` function.
```python
my_rgb_color = rgb(5, 3, 1) # (0 - 5) scale to accomodate 216 colors
```

That's all 256 colors supported by most modern terminals.

```python
color_config = {'fg':my_grayscale_color, 'bg':my_rgb_color}
printout(my_text, color=color_config)
```

### Styles
Set up a style config the same way as color config, this one is simple.
```python
style_config = {'bold':True, 'underline':True} # True/False for each, False by default
```

Combine these configs into one complete style configuration. Feel free to add `print` function keyword arguments as well.
```python
config = {'color':color_config, 'style':style_config, 'end':'\n***\n'}

# color and style config gets applied for every thing in things
# 'print' function kwargs work as usual
printout(*things, **config)

```

## Todos:
- conditional styling? (v1.0)
- fix some name conflicts
- proper project description and documentation
