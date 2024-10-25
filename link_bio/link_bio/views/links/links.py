import reflex as rx
from  link_bio.components.link_button import link_button

def links()-> rx.Component:
    return rx.vstack(
        link_button("Github", "https://github.com/jlopep09"),
        link_button("Youtube","https://www.youtube.com/channel/UCGJGaakyDW8POp07m23smcA"),
        link_button("Discord", "https://github.com/jlopep09"),
        link_button("Email", "https://github.com/jlopep09")
    )