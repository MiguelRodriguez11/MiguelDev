import reflex as rx
import datetime
import linkBio.constants as const
from linkBio.styles.styles import Size as Size
from linkBio.styles.colors import Color, TextColor

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="/logoM.png",
            height=Size.VERY_BIG.value,
            widht=Size.VERY_BIG.value
            ),
        rx.link(
            rx.box(
                f"© {datetime.date.today().year} ",
                rx.text(
                    "MIGUELDEV by Miguel Rodriguez",
                    as_="span",
                    color=Color.PRRIMARY.value
                ),
                " v1.",
                padding_top=Size.DEFAULT.value
            ),
            href=const.INDEX_URL,
            is_external=True,
            font_size=Size.MEDIUM.value
        ),
        rx.hstack(
            rx.link(
                rx.image(
                    src="/icons/github.svg",
                    height=Size.LARGE.value,
                    width=Size.LARGE.value
                ),
                href=const.REPO_URL,
                is_external=True
            ),
            rx.text(
                "Building software whith passion <3|",
                margin_top=Size.ZERO.value,
                font_size=Size.MEDIUM.value
            ),
        ),
        align="center",
        margin_bottom=Size.BIG.value,
        padding_bottom=Size.BIG.value,
        padding_x=Size.BIG.value,
        color=TextColor.FOOTER.value
    )