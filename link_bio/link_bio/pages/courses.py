import reflex as rx
from link_bio.components.navbar import navbar
from link_bio.views.header.header import header
from link_bio.views.links.links import links, linksExtra, links_courses_formacion, links_courses_experiencia
from link_bio.views.footer.footer import footer
import link_bio.styles.styles as styles
from link_bio.components.title import title
import link_bio.utils as utils
import link_bio.routes as routes

@rx.page(
    route = routes.Route.COURSES.value,
    title = utils.courses_title,
    description = utils.courses_description
)
def courses() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(showInfo = False),
                title("Formación", "h2"),
                links_courses_formacion(),
                title("Experiencia", "h2"),
                links_courses_experiencia(),
                max_width = styles.MAX_WIDTH,
                width = "100%",
                margin_y = styles.Size.BIG 
            )
        ),
        footer()
    ) 
    