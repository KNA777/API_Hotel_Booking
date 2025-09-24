from fastapi import APIRouter

from src.api.auth import router as auth_router
from src.api.bookings import router as booking_router
from src.api.facilities import router as facility_router
from src.api.hotels import router as hotel_router
from src.api.images import router as image_router
from src.api.rooms import router as room_router

main_router = APIRouter()

main_router.include_router(auth_router)
main_router.include_router(hotel_router)
main_router.include_router(room_router)
main_router.include_router(booking_router)
main_router.include_router(facility_router)
main_router.include_router(image_router)
