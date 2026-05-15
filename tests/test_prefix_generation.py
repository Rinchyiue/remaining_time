def generate_prefixes(events):
    prefixes = []

    for i in range(1, len(events) + 1):
        prefixes.append(events[:i])

    return prefixes


def test_prefix_generation():
    events = ["A", "B", "C"]

    prefixes = generate_prefixes(events)

    assert prefixes == [
        ["A"],
        ["A", "B"],
        ["A", "B", "C"]
    ]
