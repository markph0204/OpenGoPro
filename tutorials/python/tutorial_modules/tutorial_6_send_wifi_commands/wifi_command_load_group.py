# wifi_command_load_group.py/Open GoPro, Version 1.0 (C) Copyright 2021 GoPro, Inc. (http://gopro.com/OpenGoPro).
# This copyright was auto-generated on Thu, May  6, 2021 11:38:50 AM

import json
import logging
import argparse

import requests

from tutorial_modules import GOPRO_BASE_URL

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def parse_arguments() -> None:
    parser = argparse.ArgumentParser(description="Load the video preset group.")
    parser.parse_args()
    return


def main():
    parse_arguments()

    # Build the HTTP GET request
    url = GOPRO_BASE_URL + "/gopro/camera/presets/set_group?id=1000"
    logger.info(f"Loading the video preset group: sending {url}")

    # Send the GET request and retrieve the response
    response = requests.get(url)
    # Check for errors (if an error is found, an exception will be raised)
    response.raise_for_status()
    logger.info("Command sent successfully")
    # Log response as json
    logger.info(f"Response: {json.dumps(response.json(), indent=4)}")


if __name__ == "__main__":
    main()