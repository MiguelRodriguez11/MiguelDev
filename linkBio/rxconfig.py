import reflex as rx

config = rx.Config(
    app_name="linkBio",
    cors_allowed_origins=[
        "https://migueldev-web.vercel.app",
        "http://localhost:3000"
    ]
)