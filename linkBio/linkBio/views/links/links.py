import reflex as rx
from linkBio.components.link_button import link_button

def links() -> rx.Component:
    return rx.vstack(
        link_button("Twitch", "https://twitch.tv"),
        link_button("GitHub", "https://github.com/MiguelRodriguez11"),
        link_button("LinkedIn", "https://github.com/MiguelRodriguez11"),
        link_button("Me", "https://github.com/MiguelRodriguez11")
    )