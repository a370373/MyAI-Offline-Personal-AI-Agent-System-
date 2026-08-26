from pathlib import Path

p = Path("core/agent_core.py")

lines = p.read_text(encoding="utf-8").splitlines()

remove_keywords = [
    '[DEBUG DOM STATE]',
    'print(dom_state)'
]

new_lines = []

removed = 0

for line in lines:
    if any(k in line for k in remove_keywords):
        removed += 1
        continue

    new_lines.append(line)


p.write_text(
    "\n".join(new_lines) + "\n",
    encoding="utf-8"
)

print(f"[OK] removed {removed} debug lines")
