from jinja2 import Template
import re

def changedocx_to_jinja(template: str, data: dict) -> str:
    # 1. Normalize fancy quotes → normal quotes
    template = template.replace("“", '"').replace("”", '"')

    # 2. Convert IF with conditions like [Customer_Type=="Individual"]
    def if_replacer(match):
        condition = match.group(1).strip()
        # if it's equality, make sure the right-hand side is quoted
        if "==" in condition:
            left, right = condition.split("==", 1)
            left = left.strip()
            right = right.strip().strip('"').strip("'")
            return f"{{% if {left} == '{right}' %}}"
        return f"{{% if {condition} %}}"

    jinja_text = re.sub(
        r"If\s+\[([^\]]+)\]",
        if_replacer,
        template,
        flags=re.IGNORECASE
    )

    # 3. Convert ELSE
    jinja_text = re.sub(r"\bElse\b", r"{% else %}", jinja_text, flags=re.IGNORECASE)

    # 4. Convert END IF
    jinja_text = re.sub(r"End If", r"{% endif %}", jinja_text, flags=re.IGNORECASE)

    # 5. Convert FOR loops
    jinja_text = re.sub(
        r"For\s+\[([A-Za-z0-9_]+)\s+in\s+([A-Za-z0-9_\.]+)\]",
        r"{% for \1 in \2 %}",
        jinja_text,
        flags=re.IGNORECASE
    )
    jinja_text = re.sub(r"End For", r"{% endfor %}", jinja_text, flags=re.IGNORECASE)

    # 6. Convert placeholders [Something] → {{ Something }}
    jinja_text = re.sub(r"\[([A-Za-z0-9_\.]+)\]", r"{{ \1 }}", jinja_text)

    # 7. Render with Jinja2
    return Template(jinja_text).render(data)