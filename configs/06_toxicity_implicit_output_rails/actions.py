from typing import Optional
import re

from nemoguardrails.actions import action


@action(is_system_action=True)
async def check_safety(context: Optional[dict] = None):
    bot_response = context.get("bot_message")

    from huggingface_hub import InferenceClient

    client = InferenceClient(
        "https://celupbwqxzji9ssy.us-east-1.aws.endpoints.huggingface.cloud",
    )

    response = client.chat_completion(
        messages=[{"role": "user", "content": bot_response}],
        max_tokens=50,
        stream=False,
    )

    decision = response.choices[0].message.content

    if decision == 'safe':
        return True
    else:
        return False
