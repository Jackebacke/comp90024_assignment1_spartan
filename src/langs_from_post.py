def extract_languages(post) -> list:
    """Extracts the language(s) from a post, handling both Bluesky and Mastodon formats."""
    if isinstance(post.get("record"), dict) and "langs" in post["record"]:
        # Bluesky format
        post_langs = post["record"]["langs"]
    elif isinstance(post.get("doc"), dict) and "language" in post["doc"]:
        # Mastodon format
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
