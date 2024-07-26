import reflex as rx
from linkBio.styles.styles import Size as Size
from linkBio.styles.styles import Color as Color
from linkBio.styles.colors import TextColor as TextColor

def info_text(title: str, body: str) -> rx.Component:
    return rx.box(
        rx.text(
            title,
            as_="span",
            font_weight="bold",
            color=Color.PRRIMARY.value
        ),
        f"{body}",
        font_size=Size.MEDIUM.value,
        color=TextColor.BODY.value
    )
