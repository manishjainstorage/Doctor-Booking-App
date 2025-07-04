— multi-page architecture
— shared & page-specific server logic
— reactive shared state & inter-page communication
— URL-based navigation with fallback & 404
— alerts & messages

to build a Doctor Booking Application in Python Shiny.

 minimal Login → Dashboard → Appointment app with clean modular code.


 Features

Login page: enter username → saves in session → redirects to dashboard
Dashboard: welcome user, show alerts, navigate to appointment
Appointment: book slot, update shared state, show confirmation
URL-based navigation: /, /?page=login, etc.
Handles invalid page with a 404.


/ → login

/?page=login → login

/?page=dashboard → dashboard

/?page=appointment → book appointment

/?page=unknown → 404


🔗 http://127.0.0.1:8000/ (default → login page)
🔗 http://127.0.0.1:8000/?page=login
🔗 http://127.0.0.1:8000/?page=dashboard
🔗 http://127.0.0.1:8000/?page=appointment