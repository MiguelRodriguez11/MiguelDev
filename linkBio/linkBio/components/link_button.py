import reflex as rx
import linkBio.styles.styles as styles
from linkBio.styles.styles import Size as Size

def link_button(title: str, body: str, image: str, url: str, is_external = True) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.image(
                    src=image,
                    width=Size.LARGE.value,
                    height=Size.LARGE.value,
                    margin=Size.MEDIUM.value
                ),
                rx.vstack(
                    rx.text(title, style=styles.button_title_style),
                    rx.text(body, style=styles.button_body_style),
                    align_items="start",
                    spacing=Size.ZERO.value,
                    margin=Size.ZERO.value
                )
            ),
            align="center",
            width="100%",
        ),
        href=url,
        is_external=is_external,
        width="100%"
    )
