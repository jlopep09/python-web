import reflex as rx
import datetime
import link_bio.styles.styles as styles
import link_bio.styles.colors as colors

FOOTER_LINK = "http://localhost:3000/"
FOOTER_LINK_TEXT = f"© 2023-{datetime.date.today().year} ChispyDev by José López v1."
FOOTER_TEXT = "Convirtiendo la programación en mi futuro trabajo."

def footer()-> rx.Component:
    return rx.vstack(
        rx.image(src="/favicon.ico", width="32px", height="auto"),
        rx.link(rx.text(FOOTER_LINK_TEXT, _hover={"color": colors.TextColor.BODY}),
                href = FOOTER_LINK, 
                **styles.footer_link_styles
            ),
        rx.text(FOOTER_TEXT, font_size= styles.Size.MEDIUM),
        **styles.footer_style
    )