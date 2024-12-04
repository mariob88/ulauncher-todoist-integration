import logging as log

from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from .queryevent import KeywordQueryEventListener
# from .enterevent import ItemEnterEventListener
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.SetUserQueryAction import SetUserQueryAction

logger = log.getLogger(__name__)

class todointegration(Extension):
    ICON = 'images/main_icon.png'

    def __init__(self):
        super().__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())
        #self.subscribe(ItemEnterEvent, ItemEnterEventListener())

    def menu(self):
        keyword = self.preferences['kw']
        items = []

        items.append(
            ExtensionResultItem(name = "Create task",
                                description = "Create a new task",
                                icon = 'TBD',
                                on_enter = SetUserQueryAction("%s create" % keyword)))

        
        items.append(
            ExtensionResultItem(name = "List tasks",
                                description = "List your existing tasks",
                                icon = 'TBD',
                                on_enter = SetUserQueryAction("%s list" % keyword)))
        
        items.append(
            ExtensionResultItem(name = "Update task",
                                description = "Update an existing task",
                                icon = 'TBD',
                                on_enter = SetUserQueryAction("%s update" % keyword)))
        
        items.append(
            ExtensionResultItem(name = "Close task",
                                description = "Close an existing task",
                                icon = 'TBD',
                                on_enter = SetUserQueryAction("%s close" % keyword)))
        
        items.append(
            ExtensionResultItem(name = "Reopen task",
                                description = "Reopen an existing task",
                                icon = 'TBD',
                                on_enter = SetUserQueryAction("%s reopen" % keyword)))
        
        items.append(
            ExtensionResultItem(name = "Delete task",
                                description = "Delete an existing task",
                                icon = 'TBD',
                                on_enter = SetUserQueryAction("%s delete" % keyword)))
        
        return RenderResultListAction(items)