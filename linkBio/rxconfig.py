import reflex as rx

config = rx.Config(
    app_name="linkBio",
    cors_allowed_origins=[
        "https://migueldev-web-miguel-angel-rodriguez-sarays-projects.vercel.app/",
        "https://migueldev-web-git-main-miguel-angel-rodriguez-sarays-projects.vercel.app/",
        "http://localhost:3000"
    ]
)