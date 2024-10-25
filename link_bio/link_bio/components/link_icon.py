import reflex as rx
import link_bio.styles.styles as styles

def link_icon(url: str) -> rx.Component:
    return rx.link(
        rx.icon(tag = "facebook", size=16),
        href=url, 
        is_external=True
    )
    