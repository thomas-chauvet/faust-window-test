import random
from time import sleep, time

import pytest

from app.app import RawModel, print_windowed_events, tumbling_table


@pytest.mark.asyncio()
async def test_window():

    async with print_windowed_events.test_context() as agent:

        for _ in range(10):
            raw = RawModel(value=random.random(), date=time())
            _ = await agent.put(raw)
            sleep(1)

        assert tumbling_table.table.last_closed_window != 0.0
