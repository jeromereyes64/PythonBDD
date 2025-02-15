import os
import json
from BDD.src.api_client import APIClient

#Behave automatically calls this function once before executing any test scenario.
#The context object stores information shared across test steps and scenarios.
def before_all(context):
    """Load environment configuration before tests start."""

    # Get environment from command line argument or default to 'qa'
    context.env = os.getenv("ENV", "qa")

    # Load configuration file
    config_file = os.path.join(os.path.dirname(__file__), "../utils/config.json")

    with open(config_file, "r") as file:
        configs = json.load(file)

    # Validate environment
    if context.env not in configs:
        raise ValueError(f"Invalid environment: {context.env}. Use 'qa' or 'uat'.")

    # Store config and initialize APIClient
    context.config = configs[context.env]
    context.api_client = APIClient(base_url=context.config["base_url"], auth_token=context.config["auth_token"])
    print(context.api_client.base_url)
    print(f"Running tests in {context.env.upper()} environment.")