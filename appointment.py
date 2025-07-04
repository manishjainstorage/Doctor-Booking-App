from shiny import ui, render, reactive
import state

def render_ui():
    return ui.panel_main(
        ui.h3("📅 Book Appointment"),
        ui.input_date("date", "Choose Date:"),
        ui.input_select("time", "Select Time Slot", choices=["10:00", "11:00", "12:00"]),
        ui.action_button("book_btn", "Book"),
        ui.output_ui("book_msg")
    )

def server(input, output, session):
    @reactive.effect
    def book():
        if input.book_btn() > 0:
            state.appointment.set(
                f"📅 Appointment booked for {input.date()} at {input.time()}"
            )

    @output
    @render.ui
    def book_msg():
        if state.appointment():
            return ui.div(state.appointment(), class_="alert alert-info")
