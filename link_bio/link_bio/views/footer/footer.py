import reflex as rx
import datetime

def footer()-> rx.Component:
    return rx.vstack(
        rx.image(src="favicon.ico"),
        rx.link(f"© 2023-{datetime.date.today().year} ChispyDev by José López v1.", href="http://localhost:3000/", is_external=True),
        rx.text("Convirtiendo la programación como hobby en mi futuro trabajo.")
    )