import reflex as rx
import link_bio.styles.styles as styles
#Imports para que el router automatico pueda encontrar las paginas
import link_bio.pages.index as links_page
import link_bio.pages.courses as courses_page



app = rx.App(
    style = styles.BASE_STYLE,
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Comfortaa:wght@300..700&family=Open+Sans:ital,wght@0,300..800;1,300..800&display=swap"
    ]
)
#app.add_page(index)
app._compile()