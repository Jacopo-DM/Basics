#!/usr/bin/env python3

"""
Author:     jmdm
Date:       2022-12-30
OS:         macOS 12.6 (Monterey)
Hardware:   M1 chip

This code is provided "As Is"
"""

# Standard libraries
from dataclasses import dataclass


@dataclass
class Palette:
    """Color palette for plots"""

    # Basics
    BLACK: str = "#000000"
    WHITE: str = "#FFFFFF"
    RED: str = "#FF0000"
    GREEN: str = "#00FF00"
    BLUE: str = "#0000FF"

    # https://coolors.co/3a86ff-ff006e-ff9f1c-8338ec-8fa739
    BLUE: str = "#3A86FF"
    PINK: str = "#FF006E"
    ORANGE: str = "#FF9F1C"
    PURPLE: str = "#8338EC"
    GREEN: str = "#8FA739"

    # https://coolors.co/f0cf65-00b84d-51d6ff-ff5a5f-394053
    YELLOW: str = "#CCA114"
    RED: str = "#D80032"
    GRAY: str = "#394053"
    GREEN2: str = "#00B84D"
    BLUE2: str = "#00BCF5"


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
    end: str = "\033[0m"
    gray: str = "\033[90m"
    cyan: str = "\033[95m"

    # Colours bolded
    green_em: str = "\033[92m\033[1m"
    red_em: str = "\033[91m\033[1m"
    yellow_em: str = "\033[93m\033[1m"
    gray_em: str = "\033[90m\033[1m"
    cyan_em: str = "\033[95m\033[1m"

    # Styles
    em: str = "\033[1m"  # bold
    ul: str = "\033[4m"  # underline
