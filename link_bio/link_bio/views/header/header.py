import datetime
import reflex as rx
from link_bio.components.link_icon import link_icon
from link_bio.components.info_text import info_text
import link_bio.styles.styles as styles
import link_bio.styles.colors as colors

def header()-> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(fallback="JL", size="4"),
            rx.vstack(
                rx.heading("José López",_ag="h1", size="4",  color = colors.TextColor.HEADER),
                rx.heading("@ChispyDev", size="1", margin_top="0px", color = colors.TextColor.BODY),
                rx.hstack(
                    link_icon("http://localhost:3000"),
                    link_icon("http://localhost:3000"),
                    link_icon("http://localhost:3000"),
                    link_icon("http://localhost:3000")
                ),
                spacing="0",
                align="left"

            ),
            align="center"
        ),
        rx.flex(
            info_text(f"+{(datetime.date.today().year - 2024)}","años de experiencia"),
            rx.spacer(),
            info_text(f"+{(datetime.date.today().year - 2024)}","años de experiencia"),
            rx.spacer(),
            info_text(f"+{(datetime.date.today().year - 2024)}","años de experiencia"),
            width = "100%"
        ) ,
        rx.text("""Soy estudiante de ingeniería informática en la Universidad de León.
                Estoy aprendiendo a desarrollar aplicaciones web usando únicamente python.
                ¿Qué te parece la web? Aquí encontrarás todos mis links!
                """, color=colors.TextColor.BODY),
    spacing= "6"
    )