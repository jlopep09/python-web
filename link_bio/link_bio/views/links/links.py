import reflex as rx
from  link_bio.components.link_button import link_button

def links()-> rx.Component:
    return rx.vstack(
        link_button("Github","Mis proyectos", "https://github.com/jlopep09", "github"),
        link_button("Youtube","Tutoriales","https://www.youtube.com/channel/UCGJGaakyDW8POp07m23smcA", "youtube"),
        link_button("Discord","Mi discord", "https://github.com/jlopep09", "headset"),
        width = "100%"
    )
def linksExtra()-> rx.Component:
    return rx.vstack(
        link_button("Email","Contáctame", "https://github.com/jlopep09","at-sign" ),
        width = "100%"
    )