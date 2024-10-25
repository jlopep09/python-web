import reflex as rx
from  link_bio.components.link_button import link_button

def links()-> rx.Component:
    return rx.vstack(
        link_button("Github","Mis proyectos", "https://github.com/jlopep09"),
        link_button("Youtube","Tutoriales","https://www.youtube.com/channel/UCGJGaakyDW8POp07m23smcA"),
        link_button("Discord","Mi discord", "https://github.com/jlopep09"),
        link_button("Email","Contactame", "https://github.com/jlopep09"),
        width = "100%"
    )