import os
import logging as log

from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, KeywordQueryEventListener, ItemEnterEvent, ItemEnterEventListener
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.SetUserQueryAction import SetUserQueryAction

class todointegration(Extension):
    ICON = 'images/main_icon.png'
    logger = log.getLogger(__name__)

    def __init__(self):
        super().__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())
        self.subscribe(ItemEnterEvent, ItemEnterEventListener())

    def menu(self):
        keyword = self.preferences['kw']
        items = []

        items.append(name = "Create task",
                     description = "Create a new task",
                     icon = 'TBD',
                     on_enter = SetUserQueryAction("%s create" % keyword))

        
        items.append(name = "List tasks",
                     description = "List your existing tasks",
                     icon = 'TBD',
                     on_enter = SetUserQueryAction("%s list" % keyword))
        
        items.append(name = "Update task",
                     description = "Update an existing task",
                     icon = 'TBD',
                     on_enter = SetUserQueryAction("%s update" % keyword))
        
        items.append(name = "Close task",
                     description = "Close an existing task",
                     icon = 'TBD',
                     on_enter = SetUserQueryAction("%s close" % keyword))
        
        items.append(name = "Reopen task",
                     description = "Reopen an existing task",
                     icon = 'TBD',
                     on_enter = SetUserQueryAction("%s reopen" % keyword))
        
        items.append(name = "Delete task",
                     description = "Delete an existing task",
                     icon = 'TBD',
                     on_enter = SetUserQueryAction("%s delete" % keyword))
        
        return RenderResultListAction(items)