from fastapi import APIRouter

router = APIRouter(
    prefix="/api",
    tags=["health"],
)


# Endpoints for health go here.
