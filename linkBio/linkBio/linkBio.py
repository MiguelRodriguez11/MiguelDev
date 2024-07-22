import reflex as rx 
from linkBio.components.navbar import navbar_link
from linkBio.components.footer import footer
from linkBio.views.header.header import header
from linkBio.views.links.links import links

class State(rx.State):
    pass

def index() -> rx.Component:
    return  rx.vstack(
        navbar_link("Home", "http://localhost:3000/"),
        header(),
        links(),
        footer()
    )

app = rx.App()
app.add_page(index)