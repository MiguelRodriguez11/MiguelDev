import reflex as rx
from linkBio.styles.styles import Size as Size

def info_text(title: str, body: str) -> rx.Component:
    return rx.box(
        rx.text(
            title,
            as_="span",
            font_weight="bold",
                color="blue"
        ),
        f"{body}",
        font_size=Size.MEDIUM.value
    )