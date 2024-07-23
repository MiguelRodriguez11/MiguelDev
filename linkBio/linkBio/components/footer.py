import reflex as rx
import datetime
from linkBio.styles.styles import Size as Size

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(src="logo.png"),
        rx.link(
            rx.box(
                f"© {datetime.date.today().year} ",
                rx.text(
                    "MIGUELDEV by Miguel Rodriguez"
                ),
                " v1.",
                padding_top=Size.DEFAULT.value
            ),
            href="http://localhost:3000/",
            is_external=True,
            font_size=Size.MEDIUM.value
        ),
        rx.text(
            "Building software whith passion <3|",
            margin_top="0px !import",
            font_size=Size.MEDIUM.value
        ),
        margin_bottom=Size.BIG.value
    )