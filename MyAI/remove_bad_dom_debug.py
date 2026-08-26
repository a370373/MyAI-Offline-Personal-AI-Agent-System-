from pathlib import Path

p = Path("core/agent_core.py")

code = p.read_text(encoding="utf-8")


bad = '''
print("\\n[DEBUG DOM STATE]")
print(dom_state)
'''


if bad in code:
    code = code.replace(bad, "")
    print("[OK] removed bad DOM debug")
else:
    print("[WARN] bad debug not found")


p.write_text(
    code,
    encoding="utf-8"
)

print("[DONE]")
