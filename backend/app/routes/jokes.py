import { Router } from 'fastapi import APIRouter
from httpx import AsyncClient
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

# External API base URLs
JOKE_API_BASE = "https://official-joke-api.appspot.com"
JOKE_API_V2_BASE = "https://v2.jokeapi.dev"


@router.get("/joke/random")
async def get_random_joke():
    """Get a random joke from external API"""
    try:
        async with AsyncClient() as client:
            response = await client.get(f"{JOKE_API_BASE}/random_joke")
            response.raise_for_status()
            return response.json()
    except Exception as e:
        logger.error(f"Error fetching joke: {str(e)}")
        return {"error": "Failed to fetch joke"}


@router.get("/joke/type/{joke_type}")
async def get_joke_by_type(joke_type: str):
    """Get joke by type (general, programming, knock-knock)"""
    try:
        async with AsyncClient() as client:
            response = await client.get(
                f"{JOKE_API_BASE}/jokes/{joke_type}/random"
            )
            response.raise_for_status()
            return response.json()
    except Exception as e:
        logger.error(f"Error fetching joke: {str(e)}")
        return {"error": f"Failed to fetch {joke_type} joke"}


@router.get("/joke/types")
async def get_joke_types():
    """Get all available joke types"""
    try:
        async with AsyncClient() as client:
            response = await client.get(f"{JOKE_API_BASE}/types")
            response.raise_for_status()
            return response.json()
    except Exception as e:
        logger.error(f"Error fetching joke types: {str(e)}")
        return {"error": "Failed to fetch joke types"}


@router.get("/jokes/batch/{count}")
async def get_batch_jokes(count: int = 5):
    """Get multiple jokes at once"""
    if count < 1 or count > 20:
        return {"error": "Count must be between 1 and 20"}
    
    try:
        async with AsyncClient() as client:
            response = await client.get(
                f"{JOKE_API_BASE}/jokes/random/{count}"
            )
            response.raise_for_status()
            return response.json()
    except Exception as e:
        logger.error(f"Error fetching jokes: {str(e)}")
        return {"error": "Failed to fetch jokes"}


@router.get("/jokes/category/{category}")
async def get_jokes_by_category(category: str, count: int = 10):
    """Get jokes by category"""
    if count < 1 or count > 50:
        return {"error": "Count must be between 1 and 50"}
    
    try:
        async with AsyncClient() as client:
            response = await client.get(
                f"{JOKE_API_BASE}/jokes/{category}/{count}"
            )
            response.raise_for_status()
            return response.json()
    except Exception as e:
        logger.error(f"Error fetching jokes: {str(e)}")
        return {"error": f"Failed to fetch {category} jokes"}


@router.get("/joke/advanced/random")
async def get_advanced_random_joke(blacklist: str = ""):
    """Get random joke with advanced options from JokeAPI v2"""
    try:
        params = {"type": "single", "format": "json"}
        if blacklist:
            params["blacklistFlags"] = blacklist
        
        async with AsyncClient() as client:
            response = await client.get(
                f"{JOKE_API_V2_BASE}/joke/Any",
                params=params
            )
            response.raise_for_status()
            return response.json()
    except Exception as e:
        logger.error(f"Error fetching advanced joke: {str(e)}")
        return {"error": "Failed to fetch advanced joke"}
