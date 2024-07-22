import reflex as rx

def link_button(txt: str, url: str) -> rx.Component:
    return rx.link(
        rx.button(txt),
        href=url,
        is_external=True
    )