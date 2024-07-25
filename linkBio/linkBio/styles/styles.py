import reflex as rx
from enum import Enum
from .colors import Color as Color
from .colors import TextColor as TextColor
from .fonts import Font as Font

#Constants
MAX_WIDTH = "560px"

#Sizes
class Size(Enum):
    ZERO = "0px !import"
    SMALL = "0.5em",
    MEDIUM = "0.8em",
    DEFAULT = "1em",
    LARGE = "1.5em",
    BIG = "2em"
    VERY_BIG = "4em"

#Styles
BASED_STYLES = {
    "font_family": Font.DEFAULT.value,
    "background_color": Color.BACKGROUN.value,
    rx.heading: {
        "color":TextColor.HEADER.value,
        "font_family": Font.TITLE.value
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
        "display": "block",
        "_hover": {
            "background_color": Color.SECONDARY.value
        }
    },
    rx.link: {
        "text_decoration": "none",
        "_hover": {}
    }
}

navbar_title_style = dict(
    font_family=Font.LOGO.value,
    font_size=Size.LARGE.value
)

title_style = dict(
    widht="100%",
    padding_top=Size.DEFAULT.value,
    font_size=Size.LARGE.value

)

button_title_style = dict(
    font_family=Font.TITLE.value,
    font_size=Size.DEFAULT.value,
    Color=TextColor.HEADER.value
)

button_body_style = dict(
    font_family=Font.DEFAULT.value,
    font_size=Size.MEDIUM.value,
    Color=TextColor.BODY.value
)
