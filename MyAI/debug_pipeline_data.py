from pathlib import Path

p = Path("core/agent_core.py")

code = p.read_text(encoding="utf-8")


target = """
reflection = check_result(
            result
        )
"""


replace = """
print("\\n[DEBUG RESULT]")
print(result)

reflection = check_result(
            result
        )
"""


if target in code:
    code = code.replace(
        target,
        replace,
        1
    )
    print("[OK] result debug added")
else:
    print("[WARN] result pattern not found")


target2 = """
print(observation)
"""


replace2 = """
print("\\n[DEBUG OBSERVATION]")
print(observation)
"""


if target2 in code:
    code = code.replace(
        target2,
        replace2,
        1
    )
    print("[OK] observation debug added")
else:
    print("[WARN] observation print not found")


p.write_text(
    code,
    encoding="utf-8"
)

print("[DONE]")
