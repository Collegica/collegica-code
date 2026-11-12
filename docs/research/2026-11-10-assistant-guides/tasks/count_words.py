"""Count the words in a notice for task 2.

    python3 count_words.py <notice.md>

A word is any run of characters with at least one letter or digit, after
Markdown markup (#, *, _, >, list dashes, link targets) is removed. So the
heading and the signature count; "**Saturday**" is one word; "09:30" is one.
"""

import re
import sys
from pathlib import Path

text = Path(sys.argv[1]).read_text()
text = re.sub(r"\]\([^)]*\)", "]", text)          # link targets
text = re.sub(r"[#*_>\[\]`]", " ", text)           # markup
text = re.sub(r"^\s*[-+]\s+", " ", text, flags=re.M)  # list dashes
words = [w for w in text.split() if re.search(r"[A-Za-z0-9]", w)]
print(len(words))
