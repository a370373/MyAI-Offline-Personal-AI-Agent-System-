from pathlib import Path

p = Path("core/agent_core.py")

lines = p.read_text(encoding="utf-8").splitlines()


inserted = False


for i, line in enumerate(lines):

    if "reflection = check_result" in line:

        indent = len(line) - len(line.lstrip())

        space = " " * indent


        debug = [
            "",
            space + 'print("\\n[DEBUG RESULT]")',
            space + 'print(result)',
            ""
        ]


        lines[i:i] = debug

        inserted = True

        break



if inserted:
    print("[OK] result debug inserted")
else:
    print("[WARN] reflection location not found")



for i, line in enumerate(lines):

    if '"dom_after_action"' in line:

        indent = len(line) - len(line.lstrip())

        space = " " * indent


        debug = [
            "",
            space + 'print("\\n[DEBUG DOM STATE]")',
            space + 'print(dom_state)',
            ""
        ]


        lines[i:i] = debug

        print("[OK] DOM debug inserted")

        break


p.write_text(
    "\n".join(lines)+"\n",
    encoding="utf-8"
)

print("[DONE]")

