# Audio-to-MIDI transcription fixture

An eight-second, single-channel C-major scale for testing audio-to-MIDI tools. The WAV was synthesized for this project at 44,100 samples per second. Each expected note lasts one second, from C4 to C5. No third-party performance or recording is included.

## Files

| File | Purpose |
| --- | --- |
| `fixtures/C-major-eight-notes-44k1.wav` | Original synthetic input, PCM WAV |
| `fixtures/expected-notes.csv` | Ground truth: pitch, onset, and duration |
| `results/basic-pitch-browser-2026-10-24.mid` | Actual browser conversion output from Audio MIDI Tools |
| `results/basic-pitch-browser-2026-10-24.csv` | Notes independently parsed from that MIDI file |
| `scripts/compare.py` | Dependency-free comparison of expected and observed CSV |

To compare the included result, run:

```sh
python scripts/compare.py fixtures/expected-notes.csv results/basic-pitch-browser-2026-10-24.csv
```

The comparison matches by exact MIDI pitch and onset within 0.15 seconds, then checks note duration within 0.20 seconds. These are inspection tolerances, not a claimed accuracy rate. The included result has eight matched intended pitches and six additional short octave notes. The raw CSV and MIDI are supplied so the result can be checked rather than accepted on trust. Use `--strict` to make any missing, extra, or duration-mismatched note exit with failure.

You can feed the WAV to any compatible converter and export its detected notes into the CSV columns `pitch,start_seconds,duration_seconds` for comparison. The included conversion was made with the browser-local [Audio MIDI Tools WAV-to-MIDI tool](https://audiomiditools.com/wav-to-midi/); that link identifies the provenance of the result. Results from other engines, browsers, and settings may differ.

The audio and result files are the specific files used in the observed run, not a promise that rerunning a model will produce byte-identical MIDI. This is one synthetic example, not a benchmark of real singing or polyphonic music.

## License

MIT. See [LICENSE](LICENSE).
