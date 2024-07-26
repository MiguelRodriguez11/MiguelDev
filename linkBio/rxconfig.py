import reflex as rx

config = rx.Config(
    app_name="linkBio",
    cors_allowed_origins=[
        "http://localhost:3000",
        "https://migueldev-web.vercel.app"
    ]
)