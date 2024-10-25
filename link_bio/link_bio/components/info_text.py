import reflex as rx
import link_bio.styles.styles as styles
import link_bio.styles.colors as colors

def info_text(title: str,body: str) -> rx.Component:
    return rx.box(
        rx.text.strong(title, as_="span",  color = colors.Color.PRIMARY),
        f" {body}", font_size= styles.Size.MEDIUM,
        color = colors.TextColor.BODY
    )
    