from fastapi import FastAPI
from app.api.health import router as health_router
from app.api.users import router as users_router


app = FastAPI(title="User Management API")

app.include_router(users_router)
app.include_router(health_router)


@app.get("/")
def root():
    return {"message": "API is Running"}
