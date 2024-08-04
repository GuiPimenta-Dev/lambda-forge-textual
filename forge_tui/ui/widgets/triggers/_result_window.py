from textual.app import ComposeResult
from textual.widget import Widget
from textual.widgets import OptionList, Static


class ResultWindow(Widget):
    DEFAULT_CSS = """
    ResultWindow {
        layout: grid;
        grid-size: 1 2;
    }
    """

    def compose(self) -> ComposeResult:
        yield OptionList()
        yield Static()
