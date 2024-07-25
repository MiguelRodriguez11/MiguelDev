import reflex as rx
from enum import Enum
from .colors import Color as Color, TextColor
from .fonts import Font, FontWeight

#Constants
MAX_WIDTH = "560px"

#Sizes

STYLESHEETS = [
    "https://fonts.googleapis.com/css2?family=Poppins:wght@300;500&display=swap",
    "https://fonts.googleapis.com/css2?family=Comfortaa:wght@500&display=swap"
]

class Size(Enum):
    ZERO = "0px !import"
    SMALL = "0.5em",
    MEDIUM = "0.8em",
    DEFAULT = "1em",
    LARGE = "1.5em",
    BIG = "2em"
    VERY_BIG = "4em"

class Spacing(Enum):
    ZERO = "0"
    VERY_SMALL = "1"
    SMALL = "3"
    DEFAULT = "4"
    LARGE = "5"
    BIG = "6"
    MEDIUM_BIG = "7"
    VERY_BIG = "9"

#Styles
BASED_STYLES = {
    "font_family": Font.DEFAULT.value,
    "font_weight": FontWeight.LIGHT.value,
    "background_color": Color.BACKGROUN.value,
    rx.heading: {
        "color":TextColor.HEADER.value,
        "font_family": Font.TITLE.value,
        "font_weight": FontWeight.LIGHT.value
    },
    rx.button: {
        "width" : "100%",
        "height" : "100%",
        "padding": Size.SMALL.value,
        "border_radius": Size.DEFAULT.value,
        "color": "TextColor.HEADER.value",
        "background_color": Color.CONTENT.value,
        "white_space": "normal",
        "text_align": "start",
        "--cursor-button": "pointer",
        "display": "block",
        "_hover": {
            "background_color": Color.SECONDARY.value
        }
    },
    rx.link: {
        "color": TextColor.BODY.value,
        "text_decoration": "none",
        "_hover": {}
    }
}

navbar_title_style = dict(
    font_family=Font.LOGO.value,
    font_weight=FontWeight.MEDIUM.value,
    font_size=Size.LARGE.value
)

title_style = dict(
    widht="100%",
    padding_top=Size.DEFAULT.value,
    font_size=Size.LARGE.value

)

button_title_style = dict(
    font_family=Font.TITLE.value,
    font_weight=FontWeight.MEDIUM.value,
    font_size=Size.DEFAULT.value,
    Color=TextColor.HEADER.value
)

button_body_style = dict(
    font_family=Font.DEFAULT.value,
    font_weight=FontWeight.LIGHT.value,
    font_size=Size.MEDIUM.value,
    Color=TextColor.BODY.value
)
