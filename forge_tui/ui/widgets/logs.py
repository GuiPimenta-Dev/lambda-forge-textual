from collections.abc import Callable
import json
from pathlib import Path
from rich.text import Text
from rich.style import Style
from textual.app import ComposeResult, on
from textual.widget import Widget
from textual.widgets import OptionList
from textual.widgets.option_list import Option


class SingleLog(Option):

    tall = False

    def __init__(
        self,
        prompt: str,
        get_rich_style: Callable[[str], Style],
        id: str | None = None,
        disabled: bool = False,
    ) -> None:
        super().__init__(prompt, id, disabled)
        self.default_prompt = prompt
        self.get_rich_style = get_rich_style
        self.refresh_prompt()

    def refresh_prompt(self):
        try:
            json_string = self.default_prompt
            data = json.loads(json_string)
            if not self.tall:
                method = data["httpMethod"]
                resource = data["resource"]
                path = data["path"]

                method = Text(method, style="b green")
                method.pad(1)

                resource = (
                    Text() + Text(" resource:", style="dim white") + Text(resource)
                )
                resource.pad(1)

                path = Text() + Text(" path:", style="dim white") + Text(path)
                path.pad(1)

                text = Text() + method + resource + path

            else:
                formatted_json_string = json.dumps(data, indent=4)
                text = Text(formatted_json_string)

            self.set_prompt(text)

        except:
            data = self.default_prompt
            if not self.tall:
                self.set_prompt(data[:10])
            else:
                self.set_prompt(data)

    def toggle_display(self):
        self.tall = not self.tall
        self.refresh_prompt()


class LogStream(Widget):
    DEFAULT_CSS = """
    LogStream {
        height: 1fr;
    }
    """

    COMPONENT_CLASSES = {"log-method-get"}

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
                self.log_list.add_option(
                    SingleLog(line.strip(), self.get_component_rich_style)
                )

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
