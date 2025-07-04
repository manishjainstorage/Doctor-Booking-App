from shiny import ui, render
import state

def render_ui():
    return ui.panel_main(
        ui.h3("🏠 Dashboard"),
        ui.output_ui("welcome_msg"),
        ui.a("Book Appointment", href="/?page=appointment", class_="btn btn-success me-2"),
        ui.a("Logout", href="/?page=login", class_="btn btn-danger")
    )

def server(input, output, session):
    @output
    @render.ui
    def welcome_msg():
        uname = state.user()
        if uname:
            return ui.div(f"✅ Welcome, {uname}!", class_="alert alert-success")
        else:
            return ui.div("⚠️ You are not logged in.", class_="alert alert-warning")
