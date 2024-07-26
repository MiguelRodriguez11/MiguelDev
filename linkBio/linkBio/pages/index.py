import reflex as rx
import linkBio.utils as utils
import linkBio.styles.styles as styles
import linkBio.state.PageState as PageState
from linkBio.components.navbar import navbar
from linkBio.components.footer import footer
from linkBio.views.header import header
from linkBio.views.index_links import index_links
from linkBio.styles.styles import Size as Size
from linkBio.state.PageState import PageState

@rx.page(
    title=utils.index_title,
    description=utils.index_description,
    meta=utils.meta,
    on_load=PageState.featured_links
    )
def index() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                index_links(PageState.featured_info),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=Size.BIG.value,
                padding=Size.LARGE.value
            ),
        ),
        footer()
    )
