from rich.text import Text
from textual.widgets import Static,DataTable
from textual.app import ComposeResult


class Server(Static):
    def __init__(self, rows, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.rows = rows

    def compose(self) -> ComposeResult:
        yield DataTable()

    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        table.cursor_type = "none"
        styled_headers = [Text(header, style="bold green") for header in self.rows[0]]
        table.add_columns(*styled_headers)

        for row in self.rows[1:]:
            if None in row:
                continue
            styled_row = [Text(str(cell)) for cell in row]
            table.add_row(*styled_row)
