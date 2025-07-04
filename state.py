from shiny import reactive

user = reactive.Value(None)
appointment = reactive.Value(None)

def logout():
    user.set(None)
    appointment.set(None)
