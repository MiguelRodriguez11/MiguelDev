import reflex as rx
import linkBio.utils as utils
import linkBio.styles.styles as styles
from linkBio.routes import Route
from linkBio.components.navbar import navbar
from linkBio.components.footer import footer
from linkBio.views.header import header
from linkBio.styles.styles import Size
from linkBio.views.courses_links import courses_links

@rx.page(
    route=Route.COURSES.value,
    title=utils.courses_title,
    description=utils.courses_description
)
def courses() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                courses_links(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=Size.BIG.value,
                padding=Size.BIG.value
            )
        ),
        footer()
    )
