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
        query = event.get_argument() or ""

        if not query:
            return extension.menu()
        
        logger.info(query)

        query_list = query.split()
        action = query_list[0]

        if action == "create":
            logger.info(action)

        elif action == "list":
            logger.info(action)

        elif action == "update":
            logger.info(action)

        elif action == "close":
            logger.info(action)

        elif action == "reopen":
            logger.info(action)

        elif action == "delete":
            logger.info(action)