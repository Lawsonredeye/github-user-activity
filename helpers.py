"""Helpers function for handling the number of created repos and commits
made by a user in a single repo
"""

from datetime import datetime


def push_event(event_list: list) -> int:
    """
    Handles the the total number of created repos

    Returns
        int: total number of created repo on the current day
    """
    # Getting todays date
    date = str(datetime.today())
    date = date.split(" ")[0]
    count = 0

    for event in event_list:
        day_event = event["created_at"].split("T")[0]
        if event["type"] == "PushEvent" and day_event == date:
            count += event["payload"]["size"]

    return count


def create_event(event_list: list) -> int:
    """
    Handles the the total number of created repos

    Returns
        int: total number of created repo on the current day
    """
    # Getting todays date
    date = str(datetime.today())
    date = date.split(" ")[0]
    count = 0

    for event in event_list:
        day_event = event["created_at"].split("T")[0]
        if event["type"] == "CreateEvent" and day_event == date:
            count += 1

    return count


def pull_request(event_list: list) -> str:
    """returns action performed on based on a pull_request"""
    date = str(datetime.today())
    date = date.split(" ")[0]
    count = 0

    for event in event_list:
        day_event = event["created_at"].split("T")[0]
        if event["type"] == "PullRequestEvent" and day_event == date:
            return event["payload"]["action"]
