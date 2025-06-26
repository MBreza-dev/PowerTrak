from dataclasses import dataclass
import os
from dotenv import load_dotenv

load_dotenv()

@dataclass
class Settings:
    db_url: str = os.getenv("POWERTRAK_DB_URL", "sqlite:///powertrak.db")
    rewards_enabled: bool = os.getenv("POWERTRAK_REWARDS_ENABLED", "true").lower() == "true"
    debug: bool = os.getenv("POWERTRAK_DEBUG", "false").lower() == "true"

config = Settings()
