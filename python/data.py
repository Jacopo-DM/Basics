#!/usr/bin/env python3

"""
Author:     jmdm
Date:       2022-12-30
OS:         macOS 12.6 (Monterey)
Hardware:   M1 chip

This code is provided "As Is"
"""

# Standard libraries
from dataclasses import dataclass, field
from typing import Any


@dataclass
class Plotting:
    STYLE: str = "bmh"
    DPI: int = 500
    FIG_SIZE: tuple[int, int] = (8, 6)
    WEIGHT: str = "bold"
    SIZE: int = 8
    # font = {"weight": Plotting.WEIGHT, "size": Plotting.SIZE}
    # plt.rc("font", **font)


@dataclass
class Palette:
    """Color palette for plots

    See:
        - Shades: https://coolors.co/ffffff-c2c2c2-858585-474747-000000

        - RGB: https://coolors.co/ff0000-00ff00-0000ff
        - RGB (light): https://coolors.co/ff4d4d-4dff4d-4d4dff
        - RGB (dark): https://coolors.co/b30000-00b300-0000b3

        - CYMK: https://coolors.co/00ffff-ff00ff-ffff00
        - CYMK (light): https://coolors.co/4dffff-ff4dff-ffff4d
        - CYMK (dark): https://coolors.co/00b2b3-b300b2-b2b300

        - Supplementary: https://coolors.co/ff7f00-7f00ff-00ff7f-7fff00-ff007f-007fff
        - Supplementary (light): https://coolors.co/ffa64d-a64dff-4dffa6-a6ff4d-ff4da6-4da6ff
        - Supplementary (dark): https://coolors.co/b35900-5900b3-00b359-59b300-b30059-0059b3
    """

    # Shades
    white: str = "#ffffff"
    light_gray: str = "#c2c2c2"
    gray: str = "#858585"
    dark_gray: str = "#474747"
    black: str = "#000000"

    # RGB
    R: str = "#ff0000"
    G: str = "#00ff00"
    B: str = "#0000ff"

    # RGB (light)
    R_light: str = "#ff4d4d"
    G_light: str = "#4dff4d"
    B_light: str = "#4d4dff"

    # RGB (dark)
    R_dark: str = "#b30000"
    G_dark: str = "#00b300"
    B_dark: str = "#0000b3"

    # CYMK
    C: str = "#00ffff"
    M: str = "#ff00ff"
    Y: str = "#ffff00"

    # CYMK (light)
    C_light: str = "#4dffff"
    M_light: str = "#ff4dff"
    Y_light: str = "#ffff4d"

    # CYMK (dark)
    C_dark: str = "#00b2b3"
    M_dark: str = "#b300b2"
    Y_dark: str = "#b2b300"

    # Supplementary
    orange: str = "#ff7f00"
    purple: str = "#7f00ff"
    blue_green: str = "#00ff7f"
    yellow_green: str = "#7fff00"
    pink: str = "#ff007f"
    azure: str = "#007fff"

    # Supplementary (light)
    orange_light: str = "#ffa64d"
    purple_light: str = "#a64dff"
    blue_green_light: str = "#4dffa6"
    yellow_green_light: str = "#a6ff4d"
    pink_light: str = "#ff4da6"
    azure_light: str = "#4da6ff"

    # Supplementary (dark)
    orange_dark: str = "#b35900"
    purple_dark: str = "#5900b3"
    blue_green_dark: str = "#00b359"
    yellow_green_dark: str = "#59b300"
    pink_dark: str = "#b30059"
    azure_dark: str = "#0059b3"


@dataclass
class ShellColours:
    """Color palette for printing in the terminal.

    See:
        - https://stackoverflow.com/questions/4842424/list-of-ansi-color-escape-sequences
        - https://stackoverflow.com/questions/287871/how-to-print-colored-text-to-the-terminal
    """

    # Colours
    green: str = "\033[92m"
    red: str = "\033[91m"
    yellow: str = "\033[93m"
    gray: str = "\033[90m"
    purple: str = "\033[95m"
    cyan: str = "\033[96m"

    # Colours bolded
    green_em: str = "\033[92m\033[1m"
    red_em: str = "\033[91m\033[1m"
    yellow_em: str = "\033[93m\033[1m"
    gray_em: str = "\033[90m\033[1m"
    purple_em: str = "\033[95m\033[1m"
    cyan_em: str = "\033[96m\033[1m"

    # Styles
    em: str = "\033[1m"  # bold
    ul: str = "\033[4m"  # underline

    # Functional
    end: str = "\033[0m"


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    from matplotlib import rcParams

    plt.style.use(Plotting.STYLE)

    # Get the colours
    colours = [
        getattr(Palette, attr) for attr in dir(Palette) if not attr.startswith("__")
    ]

    # Plot the colours
    fig, ax = plt.subplots()
    ax.barh(range(len(colours)), [1] * len(colours), color=colours)
    ax.set_yticks(range(len(colours)))
    ax.set_yticklabels([attr for attr in dir(Palette) if not attr.startswith("__")])
    # ax.set_yticklabels(colours)
    ax.set_title("Colours")
    ax.set_xlabel("Colour")
    ax.set_ylabel("Hex code")
    plt.tight_layout()
    plt.show()
