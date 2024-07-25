import reflex as rx
import linkBio.styles.styles as styles
from linkBio.styles.styles import Size as Size
from linkBio.styles.colors import Color as Color

def navbar() -> rx.Component:
    return rx.hstack(
        rx.link(
            rx.box(
                rx.text("Miguel", as_="span", color=Color.PRRIMARY.value),
                rx.text("DEV", as_="span", color=Color.SECONDARY.value),
                style=styles.navbar_title_style
            ),
            href="http://localhost:3000/"
        ),
        position="sticky",
        bg=Color.CONTENT.value,
        padding_x=Size.DEFAULT.value,
        padding_y=Size.SMALL.value,
        z_index="999",
        top="0"
    )