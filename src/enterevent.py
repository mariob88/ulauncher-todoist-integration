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
        icon_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images/main_icon.png')


        if data["action"] == "create":
            return self.create_task(td_api, data["query"][0], icon_path)

        elif data["action"] == "list":
            items = self.list_tasks(td_api)
            return RenderResultListAction(items)
        
        elif data["action"] == "update":
            id, text = data["query"][0].split(maxsplit=1)
            return self.update_task(td_api, id, text, icon_path)
        
        elif data["action"] == "close":
            self.close_task(td_api, data["query"][0], icon_path)
        
        elif data["action"] == "reopen":
            self.reopen_task(td_api, data["query"][0], icon_path)
        
        elif data["action"] == "delete":
            self.delete_task(td_api, data["query"][0], icon_path)

        else:
            return RenderResultListAction([
                ExtensionResultItem(name = "No action",
                                description = "Write a valid action",
                                icon = 'images/error.png',
                                on_enter = HideWindowAction())])

    def create_task(self, td_api, text, icon_path):
        try:
            task = td_api.add_task(content=text)
            task_id = task.id

            Notify.init("todoist-extension")
            Notify.Notification.new("New task created with ID " + task_id, "Created task: " + text, icon_path).show()

            return RenderResultListAction([
                    ExtensionResultItem(name = "Task created with ID: " + task_id,
                                    description = "Click enter to copy the ID to the clipboard.",
                                    icon = 'images/task.png',
                                    on_enter = CopyToClipboardAction(task_id))])
        except Exception:
            logger.error(task)
            return RenderResultListAction([
                    ExtensionResultItem(name = "Something went wrong",
                                    description = "Contact the administrator to check the problem",
                                    icon = 'images/error.png',
                                    on_enter = HideWindowAction())])


    def list_tasks(self, td_api):
        items = []
        try:
            tasks = td_api.get_tasks()
            
            for t in tasks:
                items.append(
                ExtensionResultItem(name = t.content,
                                    description = "Task id " + t.id,
                                    icon = 'images/task.png',
                                    on_enter = CopyToClipboardAction(t.id)))
            
            return items
        
        except Exception:
            logger.error(tasks)
            logger.error(items)
            return RenderResultListAction([
                    ExtensionResultItem(name = "Something went wrong",
                                    description = "Contact the administrator to check the problem",
                                    icon = 'images/error.png',
                                    on_enter = HideWindowAction())])

    def update_task(self, td_api, id, text, icon_path):
        
        try:    
            task = td_api.update_task(task_id=id, content=text)
            task_id = task['id']

            Notify.init("todoist-extension")
            Notify.Notification.new("Updated task with ID " + task_id, "New content: " + text, icon_path).show()

            return RenderResultListAction([
                    ExtensionResultItem(name = "Task updated with ID: " + task_id,
                                    description = "Click enter to copy the ID to the clipboard.",
                                    icon = 'images/update.png',
                                    on_enter = CopyToClipboardAction(task_id))])

        except Exception:
            logger.error(task)
            return RenderResultListAction([
                    ExtensionResultItem(name = "Something went wrong",
                                    description = "Contact the administrator to check the problem",
                                    icon = 'images/error.png',
                                    on_enter = HideWindowAction())])

    def close_task(self, td_api, id, icon_path):
        try:
            success = td_api.close_task(task_id=id)

            Notify.init("todoist-extension")
            Notify.Notification.new("Closed task", "Closed task with ID: " + id, icon_path).show()
        except Exception:
            logger.error(success)

    def reopen_task(self, td_api, id, icon_path):
        try:
            success = td_api.reopen_task(task_id=id)

            Notify.init("todoist-extension")
            Notify.Notification.new("Reopened task", "Reopened task with ID: " + id, icon_path).show()

        except Exception:
            logger.error(success)


    def delete_task(self, td_api, id, icon_path):
        try:
            success = td_api.delete_task(task_id=id)

            Notify.init("todoist-extension")
            Notify.Notification.new("Task deleted", "Deleted task with ID: " + id, icon_path).show()
        
        except Exception:
            logger.error(success)