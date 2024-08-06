from textual import work
from textual.screen import Screen


class LoadingScreen(Screen):

    async def on_mount(self):
        self.init_forge()
        self.push_main_screen()

    @work
    async def init_forge(self):
        from time import sleep

        sleep(5)

    def push_main_screen(self):
        self.app.pop_screen()
        self.app.push_screen("index")
