import reflex as rx

#Comun

def lang() -> rx.Component:
    return rx.script("document.documentElement.lang='es'")

#Meta
meta = [
    {"name": "og:type", "content": "website"},
    {"name": "og:title", "title": "miguelDEV | Profile page"},
    {"name": "og:description", "description": "Profile page."}
]

#Index
index_title = "miguelDEV | Profile page"
index_description = "Profile page."

#Courses
courses_title = "miguelDEV | Chanels & videos to reference"
courses_description = "Este es un listado de canales y videos de programación."
