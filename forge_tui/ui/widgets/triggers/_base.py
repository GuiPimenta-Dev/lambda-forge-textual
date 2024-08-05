from typing import Dict
from textual.app import ComposeResult
from textual.widget import Widget
from textual.widgets import Input, Select, Static, TextArea
from ._result_window import ResultWindow
from ._trigger_submit import TriggerSubmit


class TriggerBaseContainer(Widget):
    pass


class TriggerBaseWidget(Static):
    DEFAULT_CSS = """
    TriggerBaseWidget {
        layout: grid;
        grid-size: 2 2;
        grid-columns: 5fr 2fr;
        height: 1fr;
    }

    TriggerBaseWidget {
        ResultWindow {
            row-span: 2;
        }

        TriggerSubmit {
            dock: bottom;
        }
    } 
    """

    def render_left(self) -> ComposeResult:
        yield from []

    def get_input_values(self) -> Dict:
        data = {}

        for widget in self.children:
            if not widget.id:
                continue

            _id = widget.id

            if isinstance(widget, Input):
                data[_id] = widget.value
            elif isinstance(widget, TextArea):
                data[_id] = widget.text
            elif isinstance(widget, Select):
                data[_id] = widget.value

        return data

    def compose(self) -> ComposeResult:
        yield from self.render_left()
        yield ResultWindow()
        yield TriggerSubmit()
