from textual.app import ComposeResult
from textual.widgets import DataTable
from textual.widget import Widget


class ServerTable(Widget):
    DEFAULT_CSS = """
    ServerTable {
        height: auto;
    }
    """

    COLUMNS = ["Name", "Service", "Type", "Trigger"]

    @property
    def table(self) -> DataTable:
        return self.query_one(DataTable)

    def on_mount(self) -> None:
        for column in self.COLUMNS:
            self.table.add_column(column)

    def compose(self) -> ComposeResult:
        yield DataTable(cursor_type="row")
