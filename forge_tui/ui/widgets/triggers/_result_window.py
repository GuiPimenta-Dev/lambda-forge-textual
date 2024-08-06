from rich.text import Text
from textual.app import ComposeResult, on
from textual.widget import Widget
from textual.widgets import Button, OptionList
from textual.widgets.option_list import Option


class RunHistoryItem(Option):
    def __init__(self, history):
        self.history = history
        formatted = Text()

        for key, value in history.items():
            formatted += Text() + Text(f"{key}: ") + Text(str(value)) + Text("\n")

        super().__init__(formatted)

    def __str__(self) -> str:
        return str(self.history)


class RunHistoryBtn(Button):
    DEFAULT_CSS = """
    RunHistoryBtn {
        margin: 1;
        width: 100%;
    }
    """


class ResultWindow(Widget):
    DEFAULT_CSS = """
    ResultWindow {
        layout: grid;
        grid-size: 1 2;
        grid-rows: 1fr 5;
    }

    ResultWindow > OptionList {
        height: 100%;
    }
    """

    @property
    def history_list(self) -> OptionList:
        return self.query_one(OptionList)

    def compose(self) -> ComposeResult:
        yield OptionList()
        yield RunHistoryBtn("Run History")

    def add_history(self, history):
        self.history_list.add_option(RunHistoryItem(history))

    @on(RunHistoryBtn.Pressed)
    def run_history(self, event: RunHistoryBtn.Pressed):
        event.stop()

        highlighted = self.history_list.highlighted
        if highlighted is None:
            self.notify("no history selected")
            return

        history = self.history_list.get_option_at_index(highlighted)
        self.notify(f"running {history}")
