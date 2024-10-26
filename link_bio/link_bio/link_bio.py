import reflex as rx
from link_bio.components.navbar import navbar
from link_bio.views.header.header import header
from link_bio.views.links.links import links, linksExtra
from link_bio.views.footer.footer import footer
import link_bio.styles.styles as styles
from link_bio.components.title import title


class State(rx.State):
    pass

def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                title("Mis links!", "h3"),
                links(),
                title("Otros links interesantes", "h2"),
                linksExtra(),
                max_width = styles.MAX_WIDTH,
                width = "100%",
                margin_y = styles.Size.BIG 
            )
        ),
        footer()
        
    ) 
    


app = rx.App(
    style = styles.BASE_STYLE,
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Comfortaa:wght@300..700&family=Open+Sans:ital,wght@0,300..800;1,300..800&display=swap"
    ]
)
app.add_page(
    index,
    title = "ChispyDev todos los links relevantes",
    description = "Con estos links encontrarás toda la información relevante sobre mi")
app._compile()