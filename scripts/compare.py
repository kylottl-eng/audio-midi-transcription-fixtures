"""Compare expected and observed MIDI-note CSV files without dependencies."""

import argparse
import csv
from pathlib import Path


def read_notes(path):
    with Path(path).open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        required = {"pitch", "start_seconds", "duration_seconds"}
        if not required.issubset(reader.fieldnames or []):
            raise ValueError(f"{path}: required columns are {sorted(required)}")
        return [
            {
                "pitch": int(row["pitch"]),
                "start": float(row["start_seconds"]),
                "duration": float(row["duration_seconds"]),
            }
            for row in reader
        ]


def compare(expected, observed, onset_tolerance, duration_tolerance):
    unused = set(range(len(observed)))
    matches = []
    missing = []
    for target in expected:
        candidates = [
            index for index in unused
            if observed[index]["pitch"] == target["pitch"]
            and abs(observed[index]["start"] - target["start"]) <= onset_tolerance
        ]
        if not candidates:
            missing.append(target)
            continue
        chosen = min(candidates, key=lambda index: abs(observed[index]["start"] - target["start"]))
        unused.remove(chosen)
        found = observed[chosen]
        matches.append((target, found))
    duration_outside = [
        (target, found) for target, found in matches
        if abs(found["duration"] - target["duration"]) > duration_tolerance
    ]
    return matches, missing, [observed[index] for index in sorted(unused)], duration_outside


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("expected", help="CSV with ground-truth pitch and timing")
    parser.add_argument("observed", help="CSV with converter-output pitch and timing")
    parser.add_argument("--onset-tolerance", type=float, default=0.15, help="seconds; default 0.15")
    parser.add_argument("--duration-tolerance", type=float, default=0.20, help="seconds; default 0.20")
    parser.add_argument("--strict", action="store_true", help="fail if any note is missing, extra, or outside duration tolerance")
    args = parser.parse_args()
    if args.onset_tolerance < 0 or args.duration_tolerance < 0:
        parser.error("tolerances must be non-negative")

    expected = read_notes(args.expected)
    observed = read_notes(args.observed)
    matched, missing, extra, duration_outside = compare(
        expected, observed, args.onset_tolerance, args.duration_tolerance
    )
    print(f"Expected notes: {len(expected)}")
    print(f"Observed notes: {len(observed)}")
    print(f"Matched pitch/onset: {len(matched)}")
    print(f"Missing: {len(missing)}")
    print(f"Extra: {len(extra)}")
    print(f"Matched notes outside duration tolerance: {len(duration_outside)}")
    for note in extra:
        print(f"  extra pitch={note['pitch']} onset={note['start']:.3f}s duration={note['duration']:.3f}s")
    if args.strict and (missing or extra or duration_outside):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
