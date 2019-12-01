from time import sleep
import os
import asyncio
class SleepD:
    def __init__(self, time: int = None):
        self.loop = asyncio.get_event_loop()
        self.time = int(time)       
        self.loop.run_until_complete(self.sleeptitle())

    async def oscorutine(self):
        os.system('title Time Left: ' + str(int(self.time)))
        
    async def sleeptitle(self):
        while self.time > 0:
            await self.oscorutine()
            sleep(1)
            self.time -= 1
        await self.oscorutine()