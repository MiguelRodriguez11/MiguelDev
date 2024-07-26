import reflex as rx
import linkBio.constants as const
from linkBio.components.link_icon import link_icon
from linkBio.components.info_text import info_text
from linkBio.styles.styles import Size, Spacing
from linkBio.styles.colors import TextColor as TextColor
from linkBio.styles.colors import Color as Color

def header(details=True) -> rx.Component:
        return rx.vstack(
                rx.hstack(
                        rx.box(
                                rx.avatar(
                                        name="miguelDEV",
                                        size=Spacing.VERY_BIG.value,
                                        fallback=">_|",
                                        variant="soft",
                                        high_contrast=True,
                                        radius="full",
                                        color=TextColor.BODY.value,
                                        bg=Color.CONTENT.value,
                                        padding="1px",
                                        border=f"2px solid {Color.PRRIMARY.value}"
                                ),
                                position="relative"
                        ),
                        rx.vstack(
                                rx.heading(
                                        "Hola! mi nombre es Miguel Rodriguez."
                                ),
                                rx.text(
                                        "@MiguelRodriguez11",
                                        margin_top=Size.ZERO.value,
                                        color=TextColor.BODY.value
                                ),
                                rx.hstack(
                                        link_icon(
                                                "/icons/dev.svg",
                                                const.DEV_URL
                                        ),

                                        link_icon(
                                                "/icons/stackoverflow.svg",
                                                const.STACKOVERFLOW
                                        ),
                                        spacing=Spacing.LARGE.value,
                                        padding_top=Size.SMALL.value
                                ),
                                spacing=Spacing.ZERO.value,
                                align_items="start"
                        ),
                        align="end",
                        spacing=Spacing.DEFAULT.value
                ),
                rx.cond(
                        details,
                        rx.vstack(
                                rx.flex(
                                        info_text("+3 ", "años de experiencia"),
                                        rx.spacer(),
                                        info_text("+3 ", "años de experiencia"),
                                        rx.spacer(),
                                        info_text("+3 ", "años de experiencia"),
                                        width="100%"
                                ),
                                rx.text(
                                        f"""
                                        Soy desarrollador DevOps con experiencia en la utomatización 
                                        de procesos de desarrollo y despliegue de software. Ayudo a las empresas 
                                        a acortar sus ciclos de desarrollo, mejorar la calidad del software y reducir 
                                        los errorres mediante la implementación de practicas DevOps. 
                                        Aquí podrás encontrar todos mis enlaces de interés. Bienvenid@s!
                                        """,
                                        font_size=Size.DEFAULT.value,
                                        color=TextColor.BODY.value
                                ),
                                widht="100%",
                                spacing=Size.BIG.value
                        )
                ),
                width="100%",
                spacing=Spacing.BIG.value,
                align_items="start"
        )
