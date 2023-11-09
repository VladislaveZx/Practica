import logging
import asyncio

from bot_app.app import main


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
