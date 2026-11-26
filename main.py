"""Fortune Cookie Funnies for Engineers — make.fun entry.

Writes one fortune-cookie line for a software engineer to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
"""

import os

# Skeleton: three punchlines stacked on one guardrail pattern —
# the classic fortune-cookie "lucky numbers" opener, escalating
# 418 (teapot) -> 429 (too many requests) -> the port you left
# open in prod. The twist: your "lucky" numbers are all error
# codes and your own open port — the cookie is cursing you.
JOKE = "Your lucky numbers are 418, 429, and the port you left open in prod. Good luck — you'll need it."


def main() -> None:
    if not 1 <= len(JOKE) <= 120:
        raise ValueError(f"joke must be 1-120 characters, got {len(JOKE)}")
    if "\n" in JOKE:
        raise ValueError("joke must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)
    print(JOKE)


if __name__ == "__main__":
    main()
