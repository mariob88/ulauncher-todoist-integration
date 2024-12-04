import logging as log

from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.action.DoNothingAction import DoNothingAction
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem

logger = log.getLogger(__name__)

class ItemEnterEventListener(EventListener):
    def __init__(self):
        pass

    def on_event(self, event, extension):
        data = event.get_data()

    def create_task(text):
        pass

    def list_tasks():
        pass

    def update_task(id, text):
        pass

    def close_task(id):
        pass

    def reopen_task(id):
        pass

    def close_task(id):
        pass