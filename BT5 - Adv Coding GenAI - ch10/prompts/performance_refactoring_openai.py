import inspect
from openai import OpenAI

from ch10.app import get_euclidean_dist   # FIX TÊN

SURROUND = """You are provided with:
1. A Python function implementation enclosed with {{{ FUNCTION }}}
2. Lines to be refactored enclosed with {{{ OLD }}}
3. A library to be used in the new code enclosed with {{{ LIBRARY }}}."""

SINGLE_TASK = """Your task is to return ONLY the refactored code.
Do not explain anything.
Do not include extra text."""

LINES = """dist_2 = 0
for i in range(len(a)):
    for j in range(len(a[i])):
        dist_2 += (a[i][j] - b[i][j]) ** 2
return np.sqrt(dist_2)
"""


def get_user_prompt(func: callable, library: str, lines: str) -> str:
    return f"""
FUNCTION: {{{{{{ {inspect.getsource(func)} }}}}}}

OLD: {{{{{{ {lines} }}}}}}

LIBRARY: {{{{{{ {library} }}}}}}

REFACTORED:
"""


if __name__ == "__main__":
    client = OpenAI()

    system_prompt = f"{SURROUND} {SINGLE_TASK}"
    user_prompt = get_user_prompt(get_euclidean_dist, "NumPy", LINES)

    completion = client.chat.completions.create(
        model="gpt-4.1-mini",   # FIX MODEL
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
    )

    print("Refactored Code:\n", completion.choices[0].message.content)