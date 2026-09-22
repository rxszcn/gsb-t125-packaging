"""手工构造的 Tag 转字符串再解析回来，是不是同一个东西

跑法：PYTHONPATH=src .venv/bin/python repro/tag-roundtrip.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from packaging.tags import Tag, parse_tag

CASES = [("cp39", "abi.3", "any"), ("py3.9", "none", "any"), ("cp39", "none", "a-b"), ("cp39", "none", "")]

for case in CASES:
    tag = Tag(*case)
    s = str(tag)
    try:
        back = sorted(str(t) for t in parse_tag(s))
        print(f"Tag{case} str={s!r} parse_tag -> {back}  往返一致={back == [s]}")
    except Exception as e:
        print(f"Tag{case} str={s!r} parse_tag -> {type(e).__name__}: {e}")

try:
    print("parse_tag('cp39-a.b-any') ->", sorted(str(t) for t in parse_tag("cp39-a.b-any")))
except Exception as e:
    print("parse_tag('cp39-a.b-any') ->", type(e).__name__, e)
