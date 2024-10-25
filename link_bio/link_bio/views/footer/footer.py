import reflex as rx
import datetime
import link_bio.styles.styles as styles
import link_bio.styles.colors as colors

def footer()-> rx.Component:
    return rx.vstack(
        rx.image(src="favicon.ico"),
        rx.link(f"© 2023-{datetime.date.today().year} ChispyDev by José López v1.", href="http://localhost:3000/", is_external=True, font_size= styles.Size.MEDIUM,color = colors.TextColor.FOOTER ),
        rx.text("Convirtiendo la programación como hobby en mi futuro trabajo.", font_size= styles.Size.MEDIUM),
        margin_bottom = styles.Size.BIG,
        padding_bottom = styles.Size.BIG,
        spacing="0",
        align="center",
        color = colors.TextColor.FOOTER
    )