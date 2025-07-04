from shiny import App, ui, render, reactive
from pages import login, dashboard, appointment, not_found

def app_ui(request):
    return ui.page_fluid(
        ui.h2("🩺 Doctor Booking App"),
        ui.output_ui("page_content")
    )

def server(input, output, session):
    # Attach all page servers
    login.server(input, output, session)
    dashboard.server(input, output, session)
    appointment.server(input, output, session)
    
    # Create a reactive value for current page
    current_page = reactive.Value("login")
    
    # Initialize page from URL query parameter
    @reactive.Effect
    def _():
        query = session.request.query
        page = query.get("page", "login")
        current_page.set(page)
    
    # Page mapping
    page_map = {
        "login": login.render_ui,
        "dashboard": dashboard.render_ui,
        "appointment": appointment.render_ui
    }
    
    @output
    @render.ui
    def page_content():
        page = current_page.get()
        if page in page_map:
            return page_map[page]()
        else:
            return not_found.render_ui(page)

app = App(app_ui, server)