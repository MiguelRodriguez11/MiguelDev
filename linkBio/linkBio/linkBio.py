import reflex as rx 
import linkBio.constants as const
import linkBio.styles.styles as styles
from linkBio.pages.index import index
from linkBio.pages.courses import courses
from linkBio.api.api import repo, live

app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASED_STYLES
)

app.api.add_api_route("/repo", repo)
app.api.add_api_route("/live/{user}", live)