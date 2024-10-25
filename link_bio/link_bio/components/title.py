import reflex as rx
import link_bio.styles.styles as styles

def title(text:str, h_type:str) -> rx.Component:
    return rx.heading(
        text, 
        as_= h_type,  
        style= styles.title_style,
        size= styles.TITLE_SIZE
    )