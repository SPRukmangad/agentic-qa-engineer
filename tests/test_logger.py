from agentic_qa_engineer.logging import get_logger

logger = get_logger(__name__)

logger.debug("Debug message")
logger.info("Information message")
logger.warning("Warning message")
logger.error("Error message")
logger.critical("Critical message")