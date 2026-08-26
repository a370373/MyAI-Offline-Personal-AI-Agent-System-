from pathlib import Path

p = Path("core/action_controller.py")

text = p.read_text()

if "[DEBUG execute_actions input]" not in text:
    text = text.replace(
        "def execute_actions(actions, browser=None):",
        "def execute_actions(actions, browser=None):\n\n    print('[DEBUG execute_actions input]', actions)",
        1
    )

if "[DEBUG execute_actions output]" not in text:
    text = text.replace(
        "    return results",
        "    print('[DEBUG execute_actions output]', results)\n\n    return results",
        1
    )

p.write_text(text)

print("[OK] debug added")
