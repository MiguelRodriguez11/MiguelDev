import reflex as rx
import linkBio.styles.styles as styles

def link_icon(url: str) -> rx.Component:
    return rx.link(
        rx.icon(
            tag="github"
        ),
        href=url,
        is_external=True
    )