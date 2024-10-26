import reflex as rx
from  link_bio.components.link_button import link_button, link_stay_button
from link_bio.routes import Route

def links()-> rx.Component:
    return rx.vstack(
        link_stay_button("Mi experiencia","Mi formación y experiencia",Route.COURSES.value, "book-marked"),
        link_button("Github","Mis proyectos", "https://github.com/jlopep09", "github"),
        link_button("Youtube","Tutoriales","https://www.youtube.com/channel/UCGJGaakyDW8POp07m23smcA", "youtube"),
        width = "100%"
    )
def linksExtra()-> rx.Component:
    return rx.vstack(
        link_button("Email","Contáctame", "mailto:jlopep09@estudiantes.unileon.es","at-sign" ),
        link_button("Repositorio","Repositorio con el código completo de esta web", "https://github.com/jlopep09/python-web", "github"),
        link_button("Discord","Mi discord", "https://github.com/jlopep09", "headset"),
        width = "100%"
    )
def links_courses_formacion()-> rx.Component:
    return rx.vstack(
        link_button("Ingeniería Informática","Estudiante de 4º curso de ingeniería informática en la Universidad de León","https://ingenierias.unileon.es/", "book-open-text"),
        link_button("Microcredencial C++","Microcredencial universitaria de C++ impartida por HPe SCDS","https://ingenierias.unileon.es/2023/12/17/microcredencial-en-lenguaje-de-programacion-c-de-la-universidad-de-leon-y-hp-scds/", "graduation-cap"),
        link_button("REGINNA 4.0","Curso tecnológico sobre emprendimiento, innovación y tecnologías punteras", "https://www.reginna4-0.eu/", "factory"),
        width = "100%"
    )
def links_courses_experiencia()-> rx.Component:
    return rx.vstack(
        link_button("Prácticas en HPe CDS","Programador en prácticas", "https://uk.linkedin.com/company/hpecds","briefcase-business" ),
        width = "100%"
    )