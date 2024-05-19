from fastapi import APIRouter

router = APIRouter()

from loguru import logger


@router.get("/")
async def root():
    logger.trace("trace")
    logger.debug("debug")
    logger.info("info")
    logger.warning("warning")
    logger.error("error")
    logger.critical("critical")
