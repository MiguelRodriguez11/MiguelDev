import reflex as rx
import datetime

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(src="logo.png"),
        rx.link(
            rx.box(
                f"© {datetime.date.today().year} ",
                rx.text(
                    "MIGUELDEV by Miguel Rodriguez"
                ),
                " v4."
            ),
        ),
        rx.text("Building software whith passion <3|")
    )