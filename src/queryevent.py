import logging as log
import re
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.action.ExtensionCustomAction import ExtensionCustomAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem

logger = log.getLogger(__name__)

class KeywordQueryEventListener(EventListener):

    def __init__(self):
        pass

    def on_event(self, event, extension):
        items = []
        query = event.get_argument() or ""

        if not query:
            return extension.menu()
        
        logger.info(query)

        query_list = query.split(maxsplit=1)
        action = query_list.pop(0)

        data = {"action": action, "query": query_list}

        if action == "create":

            return RenderResultListAction([
                ExtensionResultItem(name = "Create task",
                                description = "Write a text for the new task and click enter.",
                                icon = 'images/create.png',
                                on_enter = ExtensionCustomAction(data, keep_app_open=False))])

        elif action == "list":

            return RenderResultListAction([
                ExtensionResultItem(name = "List tasks",
                                description = "Click enter to see a list of your tasks.",
                                icon = 'images/list.png',
                                on_enter = ExtensionCustomAction(data, keep_app_open=True))])

        elif action == "update":

            return RenderResultListAction([
                ExtensionResultItem(name = "Update a task",
                                description = "Write the ID of the task to edit and a text to overwrite, then click enter.",
                                icon = 'images/update.png',
                                on_enter = ExtensionCustomAction(data, keep_app_open=False))])

        elif action == "close":

            return RenderResultListAction([
                ExtensionResultItem(name = "Close a task",
                                description = "Write the ID of the task to close and click enter",
                                icon = 'images/close.png',
                                on_enter = ExtensionCustomAction(data, keep_app_open=False))])
        
        elif action == "reopen":
            
            return RenderResultListAction([
                ExtensionResultItem(name = "Reopen a task",
                                description = "Write the ID of the closed task to reopen and click enter",
                                icon = 'images/task.png',
                                on_enter = ExtensionCustomAction(data, keep_app_open=False))])

        elif action == "delete":

            return RenderResultListAction([
                ExtensionResultItem(name = "Reopen a task",
                                description = "Write the ID of the task to delete and click enter",
                                icon = 'images/delete.png',
                                on_enter = ExtensionCustomAction(data, keep_app_open=False))])
                
        else:

            return RenderResultListAction([
                ExtensionResultItem(name = "No action",
                                description = "Write a valid action",
                                icon = 'images/error.png',
                                on_enter = HideWindowAction())])