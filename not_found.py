from shiny import ui

def render_ui(bad_page):
    return ui.div(
        ui.h3("🚫 404 - Page Not Found"),
        ui.p(f"The page '{bad_page}' does not exist."),
        ui.a("Go back to Login", href="/?page=login", class_="btn btn-primary")
    )
