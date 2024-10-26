from enum import Enum
import reflex as rx
import link_bio.styles.colors as colors


#Constants
MAX_WIDTH = "600px"

#Sizes
class Size(Enum):
    SMALL = "0.5em",
    MEDIUM = "0.8em",
    DEFAULT = "1em",
    BIG = "2em"



#Styles
BASE_STYLE = {
    "background_color" : colors.Color.BACKGROUND.value,
    rx.button:{
        "width" : "100%",
        "height" : "100%",
        "display" : "block",
        "padding" : Size.SMALL.value,
        "border_radius" : Size.DEFAULT.value ,
        "background_color" : colors.Color.CONTENT.value,
        "color" : colors.TextColor.HEADER.value,
        "_hover":{"background_color" : colors.Color.SECONDARY.value}
    },
    rx.link:{
        "text_decoration" : "none",
        "_hover" : {}
    },
    
}

title_style = dict(
    width = "100%",
    padding_top = Size.DEFAULT.value,
    color = colors.TextColor.HEADER.value,
)
#title size 1-9
TITLE_SIZE = "6"


button_title_styles = dict(
    font_size = Size.DEFAULT.value,
    color = colors.TextColor.HEADER.value,
)
button_body_styles = dict(
    font_size = Size.MEDIUM.value,
    color = colors.TextColor.BODY.value,
)