from rich.panel import Panel
from rich.text import Text
from textual.app import ComposeResult
from textual.widget import Widget
from textual.widgets import OptionList
from textual.widgets.option_list import Option


class RunHistoryItem(Option):
    def __init__(self, history):
        self.history = history
        formatted = Text()

        for key, value in history.items():
            formatted += Text() + Text(f"{key}: ") + Text(str(value)) + Text("\n")

        super().__init__(Panel(formatted))

    def __str__(self) -> str:
        return str(self.history)


class ResultWindow(Widget):
    DEFAULT_CSS = """
    ResultWindow > OptionList {
        height: 100%;
    }
    """

    @property
    def history_list(self) -> OptionList:
        return self.query_one(OptionList)

    def compose(self) -> ComposeResult:
        yield OptionList()

    def add_history(self, history):
        self.history_list.add_option(RunHistoryItem(history))
