from shiny import ui, render, reactive
import state

def render_ui():
    return ui.panel_main(
        ui.h3("🔐 Login"),
        ui.input_text("username", "Enter Username:"),
        ui.action_button("login_btn", "Login"),
        ui.output_ui("login_msg")
    )

def server(input, output, session):
    @reactive.effect
    def login():
        if input.login_btn() > 0:
            uname = input.username()
            if uname:
                state.user.set(uname)
                session.redirect("/?page=dashboard")
            else:
                state.user.set(None)

    @output
    @render.ui
    def login_msg():
        if input.login_btn() > 0 and not input.username():
            return ui.div("❌ Please enter a username.", class_="alert alert-danger")
