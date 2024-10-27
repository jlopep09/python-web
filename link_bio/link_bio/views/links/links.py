import reflex as rx
from  link_bio.components.link_button import link_button, link_stay_button
from link_bio.routes import Route
import link_bio.urls as URLS

def links()-> rx.Component:
    return rx.vstack(
        link_stay_button("Mi experiencia","Mi formación y experiencia",Route.COURSES.value, "book-marked"),
        link_button("Github","Mis proyectos", URLS.GITHUB_PROFILE_URL, "github"),
        link_button("Youtube","Tutoriales",URLS.YOUTUBE_URL, "youtube"),
        width = "100%"
    )
def linksExtra()-> rx.Component:
    return rx.vstack(
        link_button("Email","Contáctame", URLS.MAILTO_URL,"at-sign" ),
        link_button("Repositorio","Repositorio con el código completo de esta web", URLS.GITHUB_PYTHON_WEB_URL, "github"),
        link_button("Discord","Mi discord", URLS.DISCORD_URL, "headset"),
        width = "100%"
    )
def links_courses_formacion()-> rx.Component:
    return rx.vstack(
        link_button("Ingeniería Informática","Estudiante de 4º curso de ingeniería informática en la Universidad de León",URLS.ULE_URL, "book-open-text"),
        link_button("Microcredencial C++","Microcredencial universitaria de C++ impartida por HPe SCDS",URLS.MICROCREDENCIAL_C_URL, "graduation-cap"),
        link_button("REGINNA 4.0","Curso tecnológico sobre emprendimiento, innovación y tecnologías punteras", URLS.REGINNA_4_URL, "factory"),
        width = "100%"
    )
def links_courses_experiencia()-> rx.Component:
    return rx.vstack(
        link_button("Prácticas en HPe CDS","Programador en prácticas", URLS.LINKEDIN_CDS_URL,"briefcase-business" ),
        width = "100%"
    )