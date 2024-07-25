import reflex as rx
import linkBio.constants as const
from linkBio.routes import Route
from linkBio.components.link_button import link_button
from linkBio.components.title import title
from linkBio.styles.styles import Size

def courses_links() -> rx.Component:
    return rx.vstack(
        title("Creditos"),
        link_button(
            "PYTHON para WEB desde cero",
            "MoureDev by Brais Moure",
            "/icons/youtube.svg",
            const.REFLEXYT_URL
        ),
        link_button(
            "OpenVPN con Docker",
            "Pelado Nerd",
            "/icons/youtube.svg",
            const.VPN_URL
        ),
        width="100%",
        spacing="1"
    )