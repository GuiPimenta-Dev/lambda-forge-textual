from textual.app import ComposeResult
from textual.widgets import Input, TextArea
from ._base import TriggerBaseWidget, TriggerBaseContainer


class SQSContainer(TriggerBaseContainer):
    DEFAULT_CSS = """
    SQSContainer {
        layout: grid;
        grid-size: 1 3;
        grid-rows: 5 10 auto;
        grid-columns: 1fr 1fr;
    }
    """

    def compose(self) -> ComposeResult:
        yield Input(id="queue_url")
        yield TextArea.code_editor(text="{}", language="json", id="message")


class SQS(TriggerBaseWidget):
    def render_left(self) -> ComposeResult:
        yield SQSContainer()
