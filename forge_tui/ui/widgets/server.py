from rich.console import RenderableType
from textual.widget import Widget
from rich.table import Table
from forge_tui.api import Forge

# from textual.app import ComposeResult, on
# from textual.events import Resize
# from textual.widgets import DataTable

forge = Forge()


class ServerTable(Widget):
    DEFAULT_CSS = """
    ServerTable {
        height: auto;
    }

    ServerTable > DataTable {
        width: 50;
    }
    """

    COLUMNS = ["Name", "Service", "Type", "Trigger"]
    RATIOS = [None, None, None, 1]

    def render(self) -> RenderableType:

        table = Table(expand=True)
        table.show_lines = True

        for column, ratio in zip(self.COLUMNS, self.RATIOS):
            table.add_column(column, ratio=ratio)

        for row in forge.get_servers():
            table.add_row(*row)

        return table

    # @on(Resize)
    # def _resize(self, event: Resize) -> None:
    #     self.refresh_table()
    #
    # @property
    # def table(self) -> DataTable:
    #     return self.query_one(DataTable)
    #
    # def refresh_table(self):
    #     width = self.size.width
    #     for column in self.COLUMNS:
    #         self.table.add_column(column, width=width // len(self.COLUMNS))
    #
    #     self.refresh()
    #
    # def on_mount(self) -> None:
    #     self.refresh_table()
    #
    # def compose(self) -> ComposeResult:
    #     yield DataTable(cursor_type="row")
