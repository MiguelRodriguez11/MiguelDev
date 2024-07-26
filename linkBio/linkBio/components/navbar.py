import reflex as rx
import linkBio.styles.styles as styles
from linkBio.routes import Route
from linkBio.styles.styles import Size as Size
from linkBio.styles.colors import Color as Color
from linkBio.components.ant_components import float_button

def navbar() -> rx.Component:
    return rx.hstack(
        rx.link(
            rx.box(
                rx.text("Miguel", as_="span", color=Color.PRRIMARY.value),
                rx.text("DEV", as_="span", color=Color.SECONDARY.value),
                style=styles.navbar_title_style
            ),
            href=Route.INDEX.value
        ),
        float_button(
            icon=rx.image(src="/icons/donate.svg")
        ),
        position="sticky",
        bg=Color.CONTENT.value,
        padding_x=Size.DEFAULT.value,
        padding_y=Size.SMALL.value,
        z_index="999",
        top="0"
    )
