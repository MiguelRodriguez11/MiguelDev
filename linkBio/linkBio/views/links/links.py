import reflex as rx
import linkBio.constants as const
from linkBio.components.link_button import link_button
from linkBio.components.title import title
from linkBio.styles.styles import Size

def links() -> rx.Component:
    return rx.vstack(
        title("Contacto"),
        link_button(
            "LinkedIn",
            "Mi perfil laboral",
            "icons/linkedin.svg",
            const.LINKEDIN_URL
        ),
        link_button(
            "GitHub",
            "Mi perfil de GitHub",
            "icons/github.svg",
            const.GITHUB_URL
        ),
        link_button(
            "Email",
            const.EMAIL,
            "icons/email.svg",
            f"mailto: {const.EMAIL}",
        ),

        title("Recursos y más"),
        link_button(
            "Spotify",
            "Playlist para codear",
            "icons/spotify.svg",
            const.SPOTIFY_URL
        ),
        link_button(
            "YouTube",
            "Coming soon",
            "icons/youtube.svg",
            const.YOUTUBE_URL
        ),
        width="100%",
        spacing="1"
    )