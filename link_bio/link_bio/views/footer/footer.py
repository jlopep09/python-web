import reflex as rx
import datetime
import link_bio.styles.styles as styles
import link_bio.styles.colors as colors

def footer()-> rx.Component:
    return rx.vstack(
        rx.image(src="favicon.ico", width="32px", height="auto"),
        rx.link(
            rx.text(
                f"© 2023-{datetime.date.today().year} ChispyDev by José López v1.",
                _hover={"color": colors.TextColor.BODY}
                ), 
            href="http://localhost:3000/", 
            is_external=True, 
            font_size= styles.Size.MEDIUM,
            color = colors.TextColor.FOOTER,

            ),
        rx.text("Convirtiendo la programación en mi futuro trabajo.", font_size= styles.Size.MEDIUM),
        padding_bottom = styles.Size.BIG,
        spacing="0",
        align="center",
        color = colors.TextColor.FOOTER
    )