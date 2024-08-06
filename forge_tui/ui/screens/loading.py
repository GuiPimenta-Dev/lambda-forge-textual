from textual import work
from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import LoadingIndicator


class LoadingScreen(Screen):

    async def on_mount(self):
        self.is_syntesis_complete = False
        self.init_forge()
        self.set_interval(0.1, self.check_for_synthesis)

    @work(thread=True)
    async def init_forge(self):
        from time import sleep

        sleep(2)
        self.is_syntesis_complete = True

    def check_for_synthesis(self):
        if self.is_syntesis_complete:
            self.dismiss_screen()

    def dismiss_screen(self):
        self.app.pop_screen()
        self.app.push_screen("index")

    def compose(self) -> ComposeResult:
        yield LoadingIndicator()
