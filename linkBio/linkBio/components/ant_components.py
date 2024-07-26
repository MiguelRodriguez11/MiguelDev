import reflex as rx
from linkBio.styles.colors import Color

class FloatButton(rx.Component):
    library = "antd"
    tag = "FloatButton"
    icon: rx.Var[rx.el.Img]
    href = "https://"
    target = "_blank"
    badge = {"dot": True, "color": Color.PRRIMARY.value}


float_button = FloatButton.create
