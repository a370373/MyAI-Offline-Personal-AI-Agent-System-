import datetime


def run():
    now = datetime.datetime.now()

    return (
        f"目前時間：{now.strftime('%Y-%m-%d %H:%M:%S')}"
    )
