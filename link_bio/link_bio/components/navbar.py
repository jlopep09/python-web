import reflex as rx
import link_bio.styles.styles as styles
import link_bio.styles.colors as colors
from link_bio.components.ant_components import float_button


def navbar() -> rx.Component:
    return rx.hstack(
        rx.link(
            rx.flex(
                rx.text("Chispy", _as="span", color= colors.Color.PRIMARY),
                rx.text("Dev", _as="span", color= colors.Color.SECONDARY),
                font_family="Comfortaa-Medium",
                font_size = "1.5em"
            ), 
            href="/"
        ),
        float_button(), 
        position = "sticky",
        bg="lightgray",
        padding_x=styles.Size.BIG,
        padding_y=styles.Size.DEFAULT,
        z_index= "999",
        top=0,
        background_color=colors.Color.CONTENT,
    )
