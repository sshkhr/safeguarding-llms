from typing import Optional
import re

from nemoguardrails.actions import action


@action(is_system_action=True)
async def check_email(context: Optional[dict] = None):
    bot_response = context.get("bot_message")

    # Regular expression pattern to match an email address
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    
    # Search for the pattern in the given text
    match = re.search(email_pattern, bot_response)
    
    # Return True if a match is found, else False
    return match is not None