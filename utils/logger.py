import logging

logging.basicConfig(
    filename="data/support_desk.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

logger = logging.getLogger(__name__)