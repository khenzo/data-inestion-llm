from pathlib import Path

APP_NAME = "DataChad"
MODEL = "gpt-3.5-turbo"
PAGE_ICON = "🤖"

DATA_PATH = Path.cwd() / "data"
DEFAULT_DATA_SOURCE = "git@github.com:gustavz/DataChad.git"

OPENAI_HELP = """
You can sign-up for OpenAI's API [here](https://openai.com/blog/openai-api).\n
Once you are logged in, you find the API keys [here](https://platform.openai.com/account/api-keys)
"""

ACTIVELOOP_HELP = """
You can create an ActiveLoops account (including 500GB of free database storage) [here](https://www.activeloop.ai/).\n
Once you are logged in, you find the API token [here](https://app.activeloop.ai/profile/gustavz/apitoken).\n
The organisation name is your username, or you can create new organisations [here](https://app.activeloop.ai/organization/new/create)
"""
