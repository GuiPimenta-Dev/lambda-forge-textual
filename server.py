from rich.text import Text
from textual.widgets import Static, DataTable
from textual.app import ComposeResult
from textual.widgets import RichLog, Footer
from rich.table import Table


class Server(Static):
    def __init__(self, rows, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.rows = rows

    def compose(self) -> ComposeResult:
        yield RichLog(highlight=True, markup=True, min_width=300)

    def on_mount(self) -> None:
        text_log = self.query_one(RichLog)

        columns = ["Name", "Service", "Type", "Trigger"]
        table = Table(*columns)
        for row in self.rows:
            if None in row:
                continue
            table.add_row(*row)

        text_log.write(table)
