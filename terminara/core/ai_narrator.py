import dataclasses

import keyring
from openai import OpenAI
from openai.resources.chat import Completions
from openai.types.chat import ChatCompletionSystemMessageParam, ChatCompletionUserMessageParam, \
    ChatCompletionAssistantMessageParam

from terminara import SERVICE_NAME
from terminara.objects.game_state import GameState
from terminara.objects.scenario import Choices
from terminara.objects.world_settings import WorldSettings


class AiNarrator:
    def __init__(self):
        self.client = None
        self.host = keyring.get_password(SERVICE_NAME, "ai_host")
        self.key = keyring.get_password(SERVICE_NAME, "ai_key")
        self.model = keyring.get_password(SERVICE_NAME, "ai_model")
        if not self.key or not self.model:
            raise ValueError("AI API key and/or model not configured. Please set them in the main menu first.")
        self.connect()

    def connect(self):
        self.client = OpenAI(
            api_key=self.key,
            base_url=self.host or None
        )

    def generate_scenario(self, last_scenario: str, current_choice: str, world_settings: WorldSettings,
                          game_state: GameState) -> str:
        if not self.client:
            raise ConnectionError("AI client is not connected.")
        completions: Completions = self.client.chat.completions
        response = completions.create(
            model=self.model,
            messages=[
                ChatCompletionSystemMessageParam(
                    role="system",
                    content=f"""
                    You are a story teller, generate a scenario based on the scenario and choice.
                    World Settings: {world_settings.ai.system}
                    World Lores: {world_settings.ai.lore}
                    World Variables: {world_settings.variables}
                    World Items: {world_settings.items}
                    Game State: {dataclasses.asdict(game_state)}
                    {world_settings.ai.prompt}
                    Note: You only need to generate the scenario, not the choices.
                    """
                ),
                ChatCompletionUserMessageParam(
                    role="user",
                    content="Generate scenario."
                ),
                ChatCompletionAssistantMessageParam(
                    role="assistant",
                    content=f"{last_scenario}"
                ),
                ChatCompletionUserMessageParam(
                    role="user",
                    content=f"I choose '{current_choice}', generate next scenario based on the last scenario and my choice."  # noqa: E501
                )
            ]
        )
        if not response.choices or not response.choices[0].message.content:
            raise ValueError("AI did not return a valid scenario.")
        return response.choices[0].message.content

    def generate_choice(self, current_scenario: str, world_settings: WorldSettings, game_state: GameState) -> Choices:
        if not self.client:
            raise ConnectionError("AI client is not connected.")
        completions: Completions = self.client.chat.completions
        response = completions.parse(
            model=self.model,
            messages=[
                ChatCompletionSystemMessageParam(
                    role="system",
                    content=f"""
                    You are a story teller, generate choices based on the scenario.
                    World Settings: {world_settings.ai.system}
                    World Lores: {world_settings.ai.lore}
                    World Variables: {world_settings.variables}
                    World Items: {world_settings.items}
                    Game State: {dataclasses.asdict(game_state)}
                    {world_settings.ai.prompt}
                    Note: You only need to generate the choices.
                    """
                ),
                ChatCompletionUserMessageParam(
                    role="user",
                    content=f"Current scenario: '{current_scenario}', generate 1 to 4 choices based on the scenario."
                )
            ],
            response_format=Choices
        )
        if not response.choices or not response.choices[0].message.parsed:
            raise ValueError("AI did not return valid choices.")
        return response.choices[0].message.parsed
