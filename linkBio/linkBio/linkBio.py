import reflex as rx 
from linkBio.components.navbar import navbar
from linkBio.components.footer import footer
from linkBio.views.header import header
from linkBio.views.links import links
from linkBio.styles.styles import Size as Size

import linkBio.styles.styles as styles

class State(rx.State):
    pass

def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                links(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=Size.BIG.value,
                padding=Size.LARGE.value
            ),
        ),
        footer()
    )

app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASED_STYLES
)
app.add_page(
    index,
    title="miguelDEV | Profile page",
    description="Profile page.",
    meta=[
        {"name": "og:type", "content": "website"},
        {"name": "og:title", "title": "miguelDEV | Profile page"},
        {"name": "og:description", "description": "Profile page."}
    ]
)