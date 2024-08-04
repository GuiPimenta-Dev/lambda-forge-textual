from textual.app import ComposeResult
from textual.widgets import Static
from ._result_window import ResultWindow


class TriggerBaseWidget(Static):
    DEFAULT_CSS = """
    TriggerBaseWidget {
        layout: grid;
        grid-size: 2;
        grid-columns: 5fr 2fr;
    }
    """

    def render_left(self) -> ComposeResult:
        yield from []

    def compose(self) -> ComposeResult:
        yield from self.render_left()
        yield ResultWindow()
