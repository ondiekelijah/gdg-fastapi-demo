from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import ORJSONResponse
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from pydantic import ValidationError
import httpx
from sqlalchemy.exc import SQLAlchemyError

from src.routers import app_routes
from src.utils.exception_handlers import http_exception_handler, pydantic_validation_error_handler, sqlalchemy_exception_handler, validation_exception_handler

# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     # Initialize resources during startup
#     redis = Redis(host="localhost", port=6379, decode_responses=True)
#     http_client = httpx.AsyncClient()

#     app.state.redis = redis
#     app.state.http_client = http_client

#     yield  # This is where the app runs and processes requests

#     # Cleanup resources during shutdown
#     await redis.close()
#     await http_client.aclose()


app = FastAPI(
    title="Sauti Ya Comrade API",
    description="Sauti Ya Comrade is a platform designed for students to anonymously share their thoughts, complaints, or experiences. It prioritizes anonymity while enabling feedback, reactions, and moderation to ensure a safe, respectful environment. Users can post content, react using predefined emojis, and report inappropriate posts.",
    version="0.1.0",
    default_response_class=ORJSONResponse,
    # lifespan=lifespan,  # Pass the lifespan function here
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(ValidationError, pydantic_validation_error_handler)
app.add_exception_handler(SQLAlchemyError, sqlalchemy_exception_handler)

# Include routers
app.include_router(app_routes.router, tags=["API Endpoints"])


