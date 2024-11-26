# worker.py
import asyncio

from temporalio import worker, workflow
from temporalio.client import Client

import activities
from workflows import GreetingWorkflow


async def main():
    client = await Client.connect("192.168.100.16:7233")
    w = worker.Worker(
        client,
        task_queue="greeting-task-queue",
        workflows=[GreetingWorkflow],
        activities=[activities.greet],
    )
    await w.run()

if __name__ == "__main__":
    asyncio.run(main())
