import reflex as rx
from linkBio.components.link_button import link_button
from linkBio.components.title import title
from linkBio.styles.styles import Size

def links() -> rx.Component:
    return rx.vstack(
        title("Comunidad"),
        link_button(
            "LinkedIn",
            "Mi perfil laboral",
            "https://github.com/MiguelRodriguez11"
        ),
        link_button(
            "GitHub",
            "Mi perfil de GitHub",
            "https://github.com/MiguelRodriguez11"
        ),
        link_button(
            "YouTube", "Coming soon",
             "https://youtube.com"
        ),
        width="100%"
    )