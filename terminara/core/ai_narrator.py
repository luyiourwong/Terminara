import dataclasses

from openai import OpenAI
from openai.resources.chat import Completions
from openai.types.chat import ChatCompletionSystemMessageParam, ChatCompletionUserMessageParam, \
    ChatCompletionAssistantMessageParam

from terminara.objects.game_state import GameState
from terminara.objects.world_settings import WorldSettings


class AiNarrator:
    def __init__(self, host: str, key: str, model: str):
        self.client = None
        self.host = host
        self.key = key
        self.model = model
        self.connect()

    def connect(self):
        self.client = OpenAI(
            api_key=self.key,
            base_url=self.host
        )

    def generate_scenario(self, last_scenario: str, current_choice: str, world_settings: WorldSettings,
                          game_state: GameState) -> str:
        if not self.client:
            return "AI is not connected."
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
                    content=f"I choose '{current_choice}', generate next scenario based on the last scenario and my choice."
                )
            ]
        )
        return response.choices[0].message.content

    def generate_choice(self, current_scenario: str, game_state: GameState):
        pass
