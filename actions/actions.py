
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionSaveName(Action):

    def name(self) -> Text:
        return "action_save_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            name = \
            next(tracker.get_latest_entity_values("name"))
            dispatcher.utter_message(text=f"Twoja firma nazywa się, {name}!")
            return []
