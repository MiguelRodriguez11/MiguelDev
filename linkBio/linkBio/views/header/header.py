import reflex as rx

def header() -> rx.Component:
        return rx.vstack(
                rx.avatar(fallback="MD", size="xl", color_scheme="orange"),
                rx.text("@MiguelRodriguez11"),
                rx.text("Hola, mi nombre es Miguel Rodriguez."),
                rx.text("""Estudiante de octavo semestre de Ingenieria de Sistemas con Tecnólogo 
                        en Análisis y Desarrollo de Sistemas de Información, con 3 años de 
                        experiencia como DevOps""")
        )
