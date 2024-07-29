from textual.app import  ComposeResult
from textual.widgets import (
    Static,
    Pretty,
)
from textual.widgets import TabbedContent, TabPane
from api_gateway import ApiGateway


class SNS(Static):
    def compose(self) -> ComposeResult:
        yield Pretty("SNS")


class SQS(Static):
    def compose(self) -> ComposeResult:
        yield Pretty("SQS")


class S3(Static):
    def compose(self) -> ComposeResult:
        yield Pretty("S3")


class EventBridge(Static):
    def compose(self) -> ComposeResult:
        yield Pretty("EventBridge")


class Triggers(Static):
    def compose(self) -> ComposeResult:

        with TabbedContent():

            with TabPane("Api Gateway", id="api_gateway"):
                yield ApiGateway()

            with TabPane("SNS", id="sns"):
                yield SNS()

            with TabPane("SQS", id="sqs"):
                yield SQS()

            with TabPane("S3", id="s3"):
                yield S3()

            with TabPane("EventBridge", id="event_bridge"):
                yield EventBridge()
