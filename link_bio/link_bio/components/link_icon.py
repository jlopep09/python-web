import reflex as rx
import link_bio.styles.styles as styles
import link_bio.styles.colors as colors

def link_icon(url: str, icon_tag: str) -> rx.Component:
    return rx.link(
        rx.icon(
            tag=icon_tag,
            size=16,
            id="mini_icono_tag",
            color=colors.Color.SECONDARY,
            _hover={"color": colors.TextColor.BODY}  # Aplicar hover directo al icono
        ),
        href=url,
        is_external=True,
    )
