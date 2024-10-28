import reflex as rx
import link_bio.styles.styles as styles


app = rx.App(
    style = styles.BASE_STYLE,
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Comfortaa:wght@300..700&family=Open+Sans:ital,wght@0,300..800;1,300..800&display=swap"
    ]
)



app._compile()