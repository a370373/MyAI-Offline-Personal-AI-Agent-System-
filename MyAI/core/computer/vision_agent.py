from tools.browser.browser import run


def capture_screen():

    result = run(
        action="screenshot"
    )

    return result


def analyze_screen(image):

    # V1 先假裝 Vision
    # 後面接 OCR / VL 模型

    return {
        "elements": [],
        "message": "vision not connected"
    }
