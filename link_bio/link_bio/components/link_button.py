import reflex as rx
import link_bio.styles.styles as styles
import link_bio.styles.colors as colors 

def link_button(title: str, body: str, url: str, iconTag: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(
                    tag=iconTag,
                    width=styles.Size.BIG,
                    height=styles.Size.BIG,
                    margin=styles.Size.DEFAULT,
                    color=colors.Color.SECONDARY,
                    id="hover-icon"  
                ),
                rx.vstack(
                    rx.text(title, style=styles.button_title_styles),
                    rx.text(body, style=styles.button_body_styles),
                    align_items="start",
                    gap="0",
                ),
                align="center",
                _hover={
                    "#hover-icon": { "color": colors.Color.CONTENT }
                }  
            ),
        ), 
        href=url, 
        is_external=True,
        width="100%"
    )
