import datetime
import reflex as rx
from link_bio.components.link_icon import link_icon
from link_bio.components.info_text import info_text
import link_bio.styles.styles as styles
import link_bio.styles.colors as colors

"""
HEADER FUNCTION
"""

def header(showInfo:bool)-> rx.Component:
    return rx.vstack(
        profile_section(),
        rx.cond(showInfo, user_experience()),
        rx.cond(showInfo, user_text_section()),
        
        spacing= "6")


"""
SECTION FUNCTIONS
"""

def profile_section()-> rx.Component:
    return rx.hstack(
            rx.avatar( src= "/profile.png", fallback="JL", size="7",radius="medium"),
            user_info(),
            align="center")

def user_info()-> rx.Component:
    return rx.vstack(
        rx.heading("José López",_ag="h1", size="4",  color = colors.TextColor.HEADER),
        rx.heading("@ChispyDev", size="1", margin_top="0px", color = colors.TextColor.BODY, margin_bottom = styles.Size.SMALL),
        rx.hstack(
            link_icon("https://github.com/jlopep09", "github"),
            link_icon("https://www.instagram.com/jose_loppz/", "instagram"),
        ),
        spacing="0",
        align="left"
    )
def user_experience()-> rx.Component:
    return rx.flex(
        info_text(f"+{(datetime.date.today().year - 2024)}","años de experiencia"),
        rx.spacer(),
        info_text(f"+{(datetime.date.today().year - 2024)}","años de experiencia"),
        rx.spacer(),
        info_text(f"+{(datetime.date.today().year - 2024)}","años de experiencia"),
        width = "100%"
    )
def user_text_section()-> rx.Component:
    return rx.text("""Soy estudiante de ingeniería informática en la Universidad de León.
                Estoy aprendiendo a desarrollar aplicaciones web usando únicamente python.
                ¿Qué te parece la web? Aquí encontrarás todos mis links!
                """, color=colors.TextColor.BODY)