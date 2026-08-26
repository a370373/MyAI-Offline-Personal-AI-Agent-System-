import time


_session = {
    "last_task": None,
    "last_result": None,
    "last_observation": None,
    "pending": None
}


def save_session(
    task=None,
    result=None,
    observation=None,
    pending=None
):

    global _session

    _session = {
        "last_task": task,
        "last_result": result,
        "last_observation": observation,
        "pending": pending,
        "time": time.time()
    }


def get_session():

    return _session


def clear_session():

    global _session

    _session = {
        "last_task": None,
        "last_result": None,
        "last_observation": None,
        "pending": None
    }
