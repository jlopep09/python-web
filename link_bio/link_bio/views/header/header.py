import reflex as rx

def header()-> rx.Component:
    return rx.vstack(
        rx.avatar(fallback="JL", size="4"),
        rx.text("@ChispyDev"),
        rx.text("HOLA, MI NOMBRE ES CHISPYDEV"),
        rx.text("""Soy estudiante de ingeniería informática en la Universidad de León.
                Estoy aprendiendo a desarrollar aplicaciones web usando únicamente python.
                ¿Qué te parece la web? Aquí encontrarás todos mis links!
                """)
    )