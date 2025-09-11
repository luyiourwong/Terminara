from openai import OpenAI

from terminara.objects.game_state import GameState
from terminara.objects.scenario import Choice


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

    def generate_response(self, prompt: str):
        if not self.client:
            return "AI is not connected."
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content

    def generate_scenario(self, last_scenario: str, current_choice: Choice, game_state: GameState):
        pass

    def generate_choice(self, current_scenario: str, game_state: GameState):
        pass
