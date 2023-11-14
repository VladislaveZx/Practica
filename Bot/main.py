import sys
import logging
import asyncio

from bot_app.app import main
from bot_app.modules.graph_tables import refresh_graphs_jsons
from bot_app.database.requests import refresh_graph_table
from bot_app.database.models import async_main


if __name__ == "__main__":
    try:
        logging.basicConfig(level=logging.INFO, stream=sys.stdout)
        asyncio.run(async_main())
        # paths = refresh_graphs_jsons()
        # asyncio.run(refresh_graph_table(paths))
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")
