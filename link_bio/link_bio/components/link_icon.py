import reflex as rx
import link_bio.styles.styles as styles

def link_icon(url: str, icon_tag: str) -> rx.Component:
    return rx.link(
        rx.icon(
            tag=icon_tag,
            id="mini_icono_tag",
            **styles.link_icon_icon_styles
        ),
        href=url,
        **styles.link_icon_styles
    )
