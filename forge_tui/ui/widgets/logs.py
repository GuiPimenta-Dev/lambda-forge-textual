from pathlib import Path
from textual.app import ComposeResult, on
from textual.widget import Widget
from textual.widgets import OptionList
from textual.widgets.option_list import Option


class SingleLog(Option):

    tall = False

    def __init__(
        self, prompt: str, id: str | None = None, disabled: bool = False
    ) -> None:
        super().__init__(prompt, id, disabled)
        self.default_prompt = prompt
        self.refresh_prompt()

    def refresh_prompt(self):
        if not self.tall:
            self.set_prompt(self.default_prompt[:10])
        else:
            self.set_prompt(self.default_prompt)

    def toggle_display(self):
        self.tall = not self.tall
        self.refresh_prompt()


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

    @on(OptionList.OptionSelected)
    def toggle_display(self, event: OptionList.OptionSelected):
        if not isinstance(event.option, SingleLog):
            return

        for option in self.log_list._options:
            if not isinstance(option, SingleLog):
                continue

            if option == event.option:
                option.toggle_display()
            else:
                option.tall = False
            option.refresh_prompt()

        self.log_list._refresh_lines()
