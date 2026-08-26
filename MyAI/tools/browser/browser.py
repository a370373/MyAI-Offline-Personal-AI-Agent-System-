from tools.browser.human import (
    human_wait,
    human_type,
    wait_page
)

from tools.browser.manager import BrowserManager
from tools.browser.page import PageController
from tools.browser.dom import DOMController


manager = BrowserManager()

page = PageController()

try:
    page.auto_connect()
except Exception as e:
    print(
        "[BROWSER INIT]",
        e
    )



def run(action="status", **kwargs):


    if action == "status":

        return {
            "running":
            manager.is_running()
        }



    elif action == "start":

        return manager.start()



    elif action == "open":

        url = kwargs.get(
            "url"
        )


        if not url:

            return {
                "success":False,
                "error":"missing url"
            }


        if page.ws is None:

            page.auto_connect()


        result = page.navigate(
            url
        )


        wait_page(
            page
        )


        return {

            "success":True,

            "action":"open",

            "url":url,

            "result":result

        }



    elif action == "read":

        dom = DOMController(
            page
        )


        return {

            "success":True,

            "text":
            dom.get_text()

        }



    elif action == "scroll":

        direction = kwargs.get(
            "direction",
            "down"
        )

        y = 800 if direction == "down" else -800


        return page.scroll(
            y
        )



    elif action == "back":

        return page.send(
            "Page.goBack"
        )



    elif action == "refresh":

        return page.send(
            "Page.reload"
        )



    elif action == "screenshot":

        return page.screenshot()



    elif action == "click":


        x = kwargs.get(
            "x"
        )

        y = kwargs.get(
            "y"
        )


        if x is None or y is None:

            return {

                "success":False,

                "error":
                "missing coordinates"

            }


        human_wait()


        return page.click(
            x,
            y
        )



    elif action == "type":


        text = kwargs.get(
            "text",
            ""
        )


        human_wait()


        return human_type(

            page,

            text

        )



    elif action == "wait":

        import time

        time.sleep(
            kwargs.get(
                "seconds",
                1
            )
        )

        return {
            "success":True,
            "action":"wait"
        }



    elif action == "press_enter":

        return page.press_enter()



    else:

        return {

            "success":False,

            "error":
            f"unknown action: {action}"

        }





def open(url):

    global page

    page = PageController()

    result = page.navigate(
        url
    )

    wait_page(
        page
    )

    return result





def info():

    return {

        "name":
        "Chromium",

        "status":
        "available"

    }





def search_google(query):

    open(
        "https://www.google.com"
    )

    human_wait()


    return {

        "status":
        "opened",

        "query":
        query

    }
