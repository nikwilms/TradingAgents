import os
from pathlib import Path

# Load environment variables from .env file
try:
    from dotenv import load_dotenv

    # Find the .env file in the project root
    project_root = Path(__file__).parent.parent
    env_file = project_root / ".env"

    if env_file.exists():
        load_dotenv(env_file)
        print(f"✅ Loaded environment variables from {env_file}")
    else:
        print(f"⚠️  No .env file found at {env_file}")

except ImportError:
    print("⚠️  python-dotenv not installed. Run: pip install python-dotenv")


# Validate required API keys
def validate_api_keys():
    """Validate that required API keys are present"""
    missing_keys = []

    if not os.getenv("OPENAI_API_KEY"):
        missing_keys.append("OPENAI_API_KEY")

    if not os.getenv("FINNHUB_API_KEY"):
        missing_keys.append("FINNHUB_API_KEY")

    if missing_keys:
        print(f"❌ Missing required API keys: {', '.join(missing_keys)}")
        print("   Please add them to your .env file or set as environment variables")
        return False

    print("✅ All required API keys are present")
    return True


# Run validation
validate_api_keys()

DEFAULT_CONFIG = {
    "project_dir": os.path.abspath(os.path.join(os.path.dirname(__file__), ".")),
    "data_dir": "/Users/yluo/Documents/Code/ScAI/FR1-data",
    "data_cache_dir": os.path.join(
        os.path.abspath(os.path.join(os.path.dirname(__file__), ".")),
        "dataflows/data_cache",
    ),
    # LLM settings
    "deep_think_llm": "o4-mini",
    "quick_think_llm": "gpt-4o-mini",
    # Debate and discussion settings
    "max_debate_rounds": 1,
    "max_risk_discuss_rounds": 1,
    "max_recur_limit": 100,
    # Tool settings
    "online_tools": True,
}
