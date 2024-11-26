import asyncio

from temporalio.client import Client

from workflows import GreetingWorkflow


async def main():
    client = await Client.connect("192.168.100.16:7233")
    result = await client.execute_workflow(
        GreetingWorkflow.run,
        "Temporal",
        id="greeting-workflow-1",
        task_queue="greeting-task-queue",
        # Optional: Specify timeout and other options
    )
    print(f"Workflow result: {result}")

if __name__ == "__main__":
    asyncio.run(main())