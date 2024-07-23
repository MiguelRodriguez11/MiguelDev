import reflex as rx
from linkBio.components.link_icon import link_icon
from linkBio.components.info_text import info_text
from linkBio.styles.styles import Size as Size

def header() -> rx.Component:
        return rx.vstack(
                rx.hstack(
                        rx.avatar(fallback="MD", size="xl", color_scheme="orange"),
                        rx.vstack(
                                rx.heading(
                                        "Hola! mi nombre es Miguel Rodriguez.",
                                        size="lg"
                                ),
                                rx.text(
                                        "@MiguelRodriguez11",
                                        margin_top="0px !important"
                                ),
                                rx.hstack(
                                        link_icon("https://github.com/MiguelRodriguez11"),
                                        link_icon("https://github.com/MiguelRodriguez11"),
                                        link_icon("https://github.com/MiguelRodriguez11")
                                ),
                                align_items="start"
                        ),
                        spacing=Size.BIG.value
                ),

                rx.flex(
                        info_text("+3 ", "años de experiencia"),
                        rx.spacer(),
                        info_text("+3 ", "años de experiencia"),
                        rx.spacer(),
                        info_text("+3 ", "años de experiencia"),
                        width="100%"
                ),
                rx.text("""Soy desarrollador DevOps con experiencia en la utomatización 
                        de procesos de desarrollo y despliegue de software. Ayudo a las empresas 
                        a acortar sus ciclos de desarrollo, mejorar la calidad del software y reducir 
                        los errorres mediante la implementación de practicas DevOps. 
                        Aquí podrás encontrar todos mis enlaces de interés. Bienvenid@s!"""),
                spacing=Size.BIG.value,
                align_items="start"
        )
