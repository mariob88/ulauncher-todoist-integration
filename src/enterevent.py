import logging as log
from gi.repository import Notify
import todoist_api_python.api as td
import os

from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction
from ulauncher.api.shared.action.OpenUrlAction import OpenUrlAction
from ulauncher.api.shared.action.CopyToClipboardAction import CopyToClipboardAction
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem

logger = log.getLogger(__name__)

class ItemEnterEventListener(EventListener):
    def __init__(self):
        pass

    def on_event(self, event, extension):
        data = event.get_data()
        td_api = td.TodoistAPI(extension.preferences["todoist_api_token"])

        if data["action"] == "create":
            return self.create_task(td_api, data["query"][0])

        elif data["action"] == "list":
            items = self.list_tasks(td_api)
            return RenderResultListAction(items)
        
        elif data["action"] == "udpate":
            id, text = data["query"].split(maxsplit=1)
            items = self.update_task(td_api, id, text)
            return items
        
        elif data["action"] == "close":
            items = self.close_task(td_api, data["query"][0])
            return items
        
        elif data["action"] == "reopen":
            items = self.reopen_task(td_api, data["query"][0])
            return items
        
        elif data["action"] == "delete":
            items = self.delete_task(td_api, data["query"][0])
            return items
        
        else:
            return RenderResultListAction([
                ExtensionResultItem(name = "No action",
                                description = "Write a valid action",
                                icon = 'images/error.png',
                                on_enter = HideWindowAction())])

    def create_task(self, td_api, text):
        icon_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images/main_icon.png')

        task = td_api.add_task(content=text)
        task_id = task.id

        Notify.init("todoist-extension")
        Notify.Notification.new("New task created with ID " + task.id, "Created task: " + text, icon_path).show()

        return RenderResultListAction([
                ExtensionResultItem(name = "Task created with ID: " + task_id,
                                description = "Click enter to copy the ID to the clipboard.",
                                icon = 'images/task.png',
                                on_enter = CopyToClipboardAction(task_id))])

    def list_tasks(self, td_api):
        items = []
        tasks = td_api.get_tasks()

        logger.info(tasks)
        
        for t in tasks:
            items.append(
            ExtensionResultItem(name = t.content,
                                description = "Task id " + t.id,
                                icon = 'images/task.png',
                                on_enter = OpenUrlAction(t.url)))
        
        logger.info(items)

        return items

    def update_task(self, td_api, id, text):
        pass

    def close_task(self, td_api, id):
        pass

    def reopen_task(self, td_api, id):
        pass

    def delete_task(self, td_api, id):
        pass