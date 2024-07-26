import reflex as rx
import linkBio.constants as const
from linkBio.routes import Route
from linkBio.components.link_button import link_button
from linkBio.components.title import title
from linkBio.components.featured_link import featured_link
from linkBio.styles.styles import Color, Spacing
from linkBio.model.Featured import Featured
from linkBio.state.PageState import PageState

def index_links(featured: list[Featured]) -> rx.Component:
    return rx.vstack(
        title("Contacto"),
        link_button(
            "LinkedIn",
            "Mi perfil laboral",
            "/icons/linkedin.svg",
            const.LINKEDIN_URL,
            False,
            Color.SECONDARY.value,
            True
        ),
        link_button(
            "GitHub",
            "Mi perfil de GitHub",
            "/icons/github.svg",
            const.GITHUB_URL
        ),
        link_button(
            "Email",
            const.EMAIL,
            "/icons/email.svg",
            f"mailto: {const.EMAIL}",
        ),
        link_button(
            "Spotify",
            "Playlist para codear",
            "/icons/spotify.svg",
            const.SPOTIFY_URL
        ),
        rx.cond(
            PageState.featured_info,
            rx.vstack(
                title("Destacado"),
                rx.flex(
                    rx.foreach(
                        PageState.featured_info,
                        featured_link
                    ),
                    flex_direction=["column", "row"],
                    spacing=Spacing.DEFAULT.value
                ),
                spacing=Spacing.DEFAULT.value
            )
        ),
        title("Projectos"),
        link_button(
            "Free VPN service",
            "Deploy a VPN usando OpenVPN.",
            "/icons/repo.svg",
            const.REPOVPN_URL
        ),
        link_button(
            "Python Reflex",
            "Desarrollo frontend Web con Python",
            "/icons/repo.svg",
            const.REPO_URL
        ),
        link_button(
            "Referencias",
            "Documentacion utilizada como referencia",
            "/icons/code.svg",
            Route.COURSES.value,
            is_external=False
        ),
        width="100%",
        spacing="1"
    )
