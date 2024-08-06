from textual.app import ComposeResult
from textual.widgets import Input, TextArea
from ._base import TriggerBaseWidget, TriggerBaseContainer


class EventBridgeContainer(TriggerBaseContainer):
    DEFAULT_CSS = """
    EventBridgeContainer {
        layout: grid;
        grid-size: 1 2;
        grid-rows: 5 10;
    }
    """

    def compose(self) -> ComposeResult:
        yield Input(id="bus_name")
        yield TextArea.code_editor(text="{}", language="json", id="message")


class EventBridge(TriggerBaseWidget):
    def render_left(self) -> ComposeResult:
        yield EventBridgeContainer()
