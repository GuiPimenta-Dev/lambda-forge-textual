from textual.widgets import Static, RichLog
from textual import events
import asyncio


class Logs(Static):

    BINDINGS = [
        ("c", "clear", "Clear"),
    ]

    def __init__(self, log_file: str, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.log_file = log_file
        self._task = None
        self.file_position = 0

    def compose(self):
        yield RichLog(highlight=True, markup=True)

    async def tail_log(self):
        text_log = self.query_one(RichLog)
        with open(self.log_file, "r") as file:
            file.seek(0, 2)
            while True:
                line = file.readline()
                if line:
                    await self.update_log(text_log, line)
                else:
                    await asyncio.sleep(0.1)

    async def update_log(self, text_log, line):
        text_log.write(line.strip())

    async def on_mount(self) -> None:
        """Called when the DOM is ready."""
        self._task = asyncio.create_task(self.tail_log())

    async def on_unmount(self, event: events.Unmount) -> None:
        if self._task:
            self._task.cancel()
            try:
                await self._task
            except asyncio.CancelledError:
                pass

    def action_clear(self):
        text_log = self.query_one(RichLog)
        text_log.clear()
