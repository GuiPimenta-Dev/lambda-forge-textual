from textual.app import ComposeResult
from textual.screen import Screen
from ..widgets import ForgeHeader


class IndexScreen(Screen):
    DEFAULT_CSS = """
    Index {
        layout: grid;
        grid-size: 1 2;
        grid-rows: 4 1fr;
    }
    """

    def compose(self) -> ComposeResult:
        yield ForgeHeader()
