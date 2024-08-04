from pathlib import Path
from textual.app import ComposeResult
from textual.widget import Widget
from textual.widgets import OptionList
from textual.widgets.option_list import Option


class SingleLog(Option):

    tall = False

    def toggle_display(self):
        self.tall = not self.tall


class LogStream(Widget):
    DEFAULT_CSS = """
    LogStream {
        height: 1fr;
    }
    """

    def __init__(self, log_path: Path):
        super().__init__()
        self.log_path = log_path

    def compose(self) -> ComposeResult:
        yield OptionList()

    @property
    def log_list(self) -> OptionList:
        return self.query_one(OptionList)

    def on_mount(self):
        with open(self.log_path, "r") as f:
            for line in f.readlines():
                self.log_list.add_option(SingleLog(line.strip()))
