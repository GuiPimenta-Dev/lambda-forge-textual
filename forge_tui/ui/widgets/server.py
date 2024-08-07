from rich.text import Text
from rich.console import RenderableType
from textual.binding import Binding
from textual.widget import Widget
from rich.table import Table
from forge_tui.api import Forge

# from textual.app import ComposeResult, on
# from textual.events import Resize
# from textual.widgets import DataTable

forge = Forge()


class ServerTable(Widget, can_focus=True):
    DEFAULT_CSS = """
    ServerTable {
        height: auto;
    }
    """
    COMPONENT_CLASSES = {
        "table-header",
        "table-border",
        "row-name",
        "row-service",
        "row-type",
        "row-trigger",
    }

    COLUMNS = ["Name", "Service", "Type", "Trigger"]
    RATIOS = [None, None, None, 1]
    BINDINGS = [
        Binding("r", "refresh_servers", "Refresh Servers"),
    ]

    def render(self) -> RenderableType:
        table = Table(expand=True)
        table.show_lines = True
        table.border_style = self.get_component_rich_style("table-border")

        for column, ratio in zip(self.COLUMNS, self.RATIOS):
            table.add_column(
                column,
                ratio=ratio,
                header_style=self.get_component_rich_style("table-header"),
            )

        for row in forge.get_servers():
            row = [
                Text(row[0] or "", style=self.get_component_rich_style("row-name")),
                Text(row[1] or "", style=self.get_component_rich_style("row-service")),
                Text(row[2] or "", style=self.get_component_rich_style("row-type")),
                Text(row[3] or "", style=self.get_component_rich_style("row-trigger")),
            ]
            table.add_row(*row)

        return table

    def on_show(self):
        self.focus()

    def action_refresh_servers(self):
        self.refresh()

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
