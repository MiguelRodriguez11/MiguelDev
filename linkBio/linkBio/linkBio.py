import reflex as rx 
import linkBio.constants as const
import linkBio.styles.styles as styles
from linkBio.pages.index import index
from linkBio.pages.courses import courses

app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASED_STYLES
)
