from textual.app import ComposeResult
from textual.widget import Widget
from textual.widgets import OptionList, Static
from textual.widgets.option_list import Option


class RunHistoryItem(Option):
    def __init__(self, history):
        super().__init__(str(history))
        self.history = history


class ResultWindow(Widget):
    DEFAULT_CSS = """
    ResultWindow {
        layout: grid;
        grid-size: 1 2;
    }

    ResultWindow > OptionList, Static {
        height: 100%;
    }
    """

    @property
    def history_list(self) -> OptionList:
        return self.query_one(OptionList)

    def compose(self) -> ComposeResult:
        yield OptionList()
        yield Static()

    def add_history(self, history):
        self.history_list.add_option(RunHistoryItem(history))
