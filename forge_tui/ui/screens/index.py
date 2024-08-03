from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import TabPane, TabbedContent

from ..widgets import ForgeHeader, ServerTable, LogStream, Triggers


class IndexScreen(Screen):
    DEFAULT_CSS = """
    IndexScreen {
        layout: grid;
        grid-size: 1 2;
        grid-rows: 4 1fr;
    }
    """

    def compose(self) -> ComposeResult:
        yield ForgeHeader()
        with TabbedContent():

            with TabPane("Server", id="server"):
                yield ServerTable()

            with TabPane("Logs", id="logs"):
                yield LogStream()

            with TabPane("Triggers", id="triggers"):
                yield Triggers()
