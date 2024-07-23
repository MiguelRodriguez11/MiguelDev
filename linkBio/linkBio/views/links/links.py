import reflex as rx
import linkBio.constants as const
from linkBio.components.link_button import link_button
from linkBio.components.title import title
from linkBio.styles.styles import Size

def links() -> rx.Component:
    return rx.vstack(
        title("Comunidad"),
        link_button(
            "LinkedIn",
            "Mi perfil laboral",
            const.LINKEDIN_URL
        ),
        link_button(
            "GitHub",
            "Mi perfil de GitHub",
            const.GITHUB_URL
        ),
        link_button(
            "Spotify",
            "Playlist para codear",
            const.SPOTIFY_URL
        ),
        link_button(
            "YouTube",
            "Coming soon",
            const.YOUTUBE_URL
        ),
        width="100%"
    )