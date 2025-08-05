from fastapi import FastAPI
from app.api import users, bookings, movies, screenings

app = FastAPI(title="Cinema Ticketing System")

# Register routes
app.include_router(users.router, prefix="/users", tags=["Users"])
# app.include_router(bookings.router, prefix="/bookings", tags=["Bookings"])
# app.include_router(movies.router, prefix="/movies", tags=["Movies"])
# app.include_router(screenings.router, prefix="/screenings", tags=["Screenings"])


@app.get("/health")
def health_check():
    return {"status": "ok"}
