from textual.app import ComposeResult
from textual.widgets import Input, TextArea

from forge_tui.ui.widgets.text_area_theme import get_text_area
from ._base import TriggerBaseWidget, TriggerBaseContainer


class SQSContainer(TriggerBaseContainer):
    DEFAULT_CSS = """
    SQSContainer {
        layout: grid;
        grid-size: 1 2;
        grid-rows: 5 10;
        grid-columns: 1fr 1fr;
    }
    """

    def compose(self) -> ComposeResult:
        yield Input(id="queue_url")
        yield get_text_area("message")


class SQS(TriggerBaseWidget):
    def render_left(self) -> ComposeResult:
        yield SQSContainer()
