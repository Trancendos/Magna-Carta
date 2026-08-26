import re
with open("scripts/capital_governance_check.py", "r") as f:
    content = f.read()

new_content = content.replace(
    'f"progression_gates: gate {gid!r}.requires must be a mapping, got {type(requires).__name__}"',
    'f"progression_gates: gate {gid!r}.requires must be a mapping, "\n                f"got {type(requires).__name__}"'
)

with open("scripts/capital_governance_check.py", "w") as f:
    f.write(new_content)
