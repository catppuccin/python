"""Functionality relating to Catppuccin flavors.

A flavor is a collection of colors.
"""
from dataclasses import dataclass

from catppuccin.color import Color


@dataclass(frozen=True)
class Flavor:
    """All the colors in a flavor of Catppuccin."""

    name: str
    rosewater: Color
    flamingo: Color
    pink: Color
    mauve: Color
    red: Color
    maroon: Color
    peach: Color
    yellow: Color
    green: Color
    teal: Color
    sky: Color
    sapphire: Color
    blue: Color
    lavender: Color
    text: Color
    subtext1: Color
    subtext0: Color
    overlay2: Color
    overlay1: Color
    overlay0: Color
    surface2: Color
    surface1: Color
    surface0: Color
    base: Color
    mantle: Color
    crust: Color

    @staticmethod
    def latte() -> "Flavor":
        """Latte flavored Catppuccin."""
        return Flavor(
            name="Latte",
            rosewater=Color(220, 138, 120),
            flamingo=Color(221, 120, 120),
            pink=Color(234, 118, 203),
            mauve=Color(136, 57, 239),
            red=Color(210, 15, 57),
            maroon=Color(230, 69, 83),
            peach=Color(254, 100, 11),
            yellow=Color(223, 142, 29),
            green=Color(64, 160, 43),
            teal=Color(23, 146, 153),
            sky=Color(4, 165, 229),
            sapphire=Color(32, 159, 181),
            blue=Color(30, 102, 245),
            lavender=Color(114, 135, 253),
            text=Color(76, 79, 105),
            subtext1=Color(92, 95, 119),
            subtext0=Color(108, 111, 133),
            overlay2=Color(124, 127, 147),
            overlay1=Color(140, 143, 161),
            overlay0=Color(156, 160, 176),
            surface2=Color(172, 176, 190),
            surface1=Color(188, 192, 204),
            surface0=Color(204, 208, 218),
            base=Color(239, 241, 245),
            mantle=Color(230, 233, 239),
            crust=Color(220, 224, 232),
        )

    @staticmethod
    def frappe() -> "Flavor":
        """Frappé flavored Catppuccin."""
        return Flavor(
            name="Frappé",
            rosewater=Color(242, 213, 207),
            flamingo=Color(238, 190, 190),
            pink=Color(244, 184, 228),
            mauve=Color(202, 158, 230),
            red=Color(231, 130, 132),
            maroon=Color(234, 153, 156),
            peach=Color(239, 159, 118),
            yellow=Color(229, 200, 144),
            green=Color(166, 209, 137),
            teal=Color(129, 200, 190),
            sky=Color(153, 209, 219),
            sapphire=Color(133, 193, 220),
            blue=Color(140, 170, 238),
            lavender=Color(186, 187, 241),
            text=Color(198, 208, 245),
            subtext1=Color(181, 191, 226),
            subtext0=Color(165, 173, 206),
            overlay2=Color(148, 156, 187),
            overlay1=Color(131, 139, 167),
            overlay0=Color(115, 121, 148),
            surface2=Color(98, 104, 128),
            surface1=Color(81, 87, 109),
            surface0=Color(65, 69, 89),
            base=Color(48, 52, 70),
            mantle=Color(41, 44, 60),
            crust=Color(35, 38, 52),
        )

    @staticmethod
    def macchiato() -> "Flavor":
        """Macchiato flavored Catppuccin."""
        return Flavor(
            name="Macchiato",
            rosewater=Color(244, 219, 214),
            flamingo=Color(240, 198, 198),
            pink=Color(245, 189, 230),
            mauve=Color(198, 160, 246),
            red=Color(237, 135, 150),
            maroon=Color(238, 153, 160),
            peach=Color(245, 169, 127),
            yellow=Color(238, 212, 159),
            green=Color(166, 218, 149),
            teal=Color(139, 213, 202),
            sky=Color(145, 215, 227),
            sapphire=Color(125, 196, 228),
            blue=Color(138, 173, 244),
            lavender=Color(183, 189, 248),
            text=Color(202, 211, 245),
            subtext1=Color(184, 192, 224),
            subtext0=Color(165, 173, 203),
            overlay2=Color(147, 154, 183),
            overlay1=Color(128, 135, 162),
            overlay0=Color(110, 115, 141),
            surface2=Color(91, 96, 120),
            surface1=Color(73, 77, 100),
            surface0=Color(54, 58, 79),
            base=Color(36, 39, 58),
            mantle=Color(30, 32, 48),
            crust=Color(24, 25, 38),
        )

    @staticmethod
    def mocha() -> "Flavor":
        """Mocha flavored Catppuccin."""
        return Flavor(
            name="Mocha",
            rosewater=Color(245, 224, 220),
            flamingo=Color(242, 205, 205),
            pink=Color(245, 194, 231),
            mauve=Color(203, 166, 247),
            red=Color(243, 139, 168),
            maroon=Color(235, 160, 172),
            peach=Color(250, 179, 135),
            yellow=Color(249, 226, 175),
            green=Color(166, 227, 161),
            teal=Color(148, 226, 213),
            sky=Color(137, 220, 235),
            sapphire=Color(116, 199, 236),
            blue=Color(137, 180, 250),
            lavender=Color(180, 190, 254),
            text=Color(205, 214, 244),
            subtext1=Color(186, 194, 222),
            subtext0=Color(166, 173, 200),
            overlay2=Color(147, 153, 178),
            overlay1=Color(127, 132, 156),
            overlay0=Color(108, 112, 134),
            surface2=Color(88, 91, 112),
            surface1=Color(69, 71, 90),
            surface0=Color(49, 50, 68),
            base=Color(30, 30, 46),
            mantle=Color(24, 24, 37),
            crust=Color(17, 17, 27),
        )
