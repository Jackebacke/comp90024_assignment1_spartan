import json
from collections import Counter


def get_langs(path):
    langs = Counter()
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            if not line.strip():  # Skip empty lines
                continue

            try:  # Handle potential JSON decoding errors
                post = json.loads(line)
                langs.update(langs_from_post(post))
            except json.JSONDecodeError:
                continue

    return langs


def langs_from_post(post) -> list:
    if (
        isinstance(post.get("record"), dict) and "langs" in post["record"]
    ):  # Bluesky format
        post_langs = post["record"]["langs"]
    elif (
        isinstance(post.get("doc"), dict) and "language" in post["doc"]
    ):  # Mastodon format
        post_langs = post["doc"]["language"]
    else:
        return ["<Missing>"]

    if post_langs is None:
        return ["<None>"]
    if isinstance(post_langs, list):
        if not post_langs:  # Empty list case
            return ["<empty_list>"]
        else:
            return post_langs
    elif isinstance(post_langs, str):
        return [post_langs]
    return []


if __name__ == "__main__":
    # path = "comp90024_assignment1_spartan/mastodon-small.ndjson"
    # path = "comp90024_assignment1_spartan/mastodon-medium.ndjson"
    # path = "comp90024_assignment1_spartan/bluesky-small.ndjson"
    path = "comp90024_assignment1_spartan/bluesky-medium.ndjson"
    langs = get_langs(path)
    print(f"Languages found: {langs}")
