import reflex as rx
from link_bio.components.navbar import navbar
from link_bio.views.header import header
from link_bio.views.links.links import links, linksExtra
from link_bio.views.footer import footer
import link_bio.styles.styles as styles
from link_bio.components.title import title
import link_bio.utils as utils

@rx.page(
    title = utils.index_title,
    description = utils.index_description
)
def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(showInfo = True),
                title("Mis links!", "h2"),
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
    