from core.computer.vision_agent import capture_screen, analyze_screen
from core.computer.action_planner import create_action
from tools.browser.browser import run


def computer_use(target):

    print("[Computer Use]")
    
    screen = capture_screen()

    vision = analyze_screen(
        screen
    )

    action = create_action(
        target
    )


    if not action:
        return {
            "success":False,
            "reason":"找不到操作"
        }


    result = run(
        action=action["action"],
        x=action.get("x"),
        y=action.get("y")
    )


    return {
        "success":True,
        "action":action,
        "result":result
    }
