# Audio MIDI Tools transcription fixtures

Downloadable, unedited MIDI outputs from the browser-local [MP3 to MIDI tool](https://audiomiditools.com/mp3-to-midi/) and the general [Audio to MIDI tool](https://audiomiditools.com/). This repository includes a synthetic scale with a known answer and three conversions of real CC0 music. The files let you inspect what the tool actually returned; they are not accuracy scores.

## Three real-song MIDI downloads

These `.mid` files were downloaded after selecting the complete source recording in the live browser tool on 2026-10-25. An independent MIDI parser read each saved file. The source recordings are linked below; audio is not copied into this repository.

| Downloaded result | CC0 input and creator | Input | Parsed output |
| --- | --- | --- | --- |
| [Get Ready](results/real-songs/get-ready-komiku-from-mp3.mid) | [Get Ready — Loyalty Freak Music / Komiku](https://opengameart.org/content/get-ready) | MP3, 75 s | One note-bearing track; 2,343 note events |
| [Done (Rock and Jazz)](results/real-songs/done-rock-and-jazz-pro-sensory-from-mp3.mid) | [Done (Rock and Jazz) — Pro Sensory / Alex McCulloch](https://opengameart.org/content/done-rock-and-jazz) | MP3, 136 s | One note-bearing track; 5,051 note events |
| [Rock Theme 3](results/real-songs/rock-theme-3-umplix-from-wav.mid) | [Rock Theme 3 — Umplix](https://opengameart.org/content/rock-theme-3) | WAV, 69 s | One note-bearing track; 1,344 note events |

The [manifest](results/real-songs/manifest.csv) records each output's byte size and SHA-256 hash so you can verify a download. The creator of Rock Theme 3 also supplies an original MIDI with a separate drum part. Our downloaded conversion has **one ordinary note track**, not separate drum and instrument tracks. At its opening the converted pitches include 43, 55 and 62; we cannot attribute any one pitch to an individual drum hit. Drum sounds can appear as pitched note events in this tool's output.

These files contain estimated note events, not the original audio or an instrument-by-instrument arrangement. We have no aligned ground-truth score for the real recordings, so short or dense note events are inspection targets, not confirmed false positives. Do not calculate an error rate from the note counts in this table. The tool cannot separate stems or produce a multi-track transcription.

## Synthetic scale with a known answer

The original eight-second, single-channel [C-major WAV](fixtures/C-major-eight-notes-44k1.wav) contains eight one-second notes from C4 through C5. Its [expected notes](fixtures/expected-notes.csv), [downloaded MIDI](results/basic-pitch-browser-2026-10-24.mid), and [independently parsed note CSV](results/basic-pitch-browser-2026-10-24.csv) are supplied for a checkable comparison. The WAV was synthesized for this project; it is not a human recording.

Run the dependency-free comparison script:

```sh
python scripts/compare.py fixtures/expected-notes.csv results/basic-pitch-browser-2026-10-24.csv
```

It matches exact pitch with onset within 0.15 seconds and duration within 0.20 seconds. Those are inspection tolerances, not a general accuracy rate. This one output had eight matched intended pitches and six additional short octave notes. Use `--strict` to make missing, extra or duration-mismatched notes fail the check.

To repeat a real-song conversion, download the recording from its linked CC0 source page, select it in the relevant tool above, download the MIDI, and inspect the notes in your MIDI editor. A repeat run, another browser or another device may produce a different file. See [PROVENANCE.md](PROVENANCE.md) for the source and scope of these results.

## License

The original script and documentation are MIT licensed; see [LICENSE](LICENSE). The three real-song inputs are marked CC0 on their linked source pages, and the conversion outputs in `results/real-songs/` are shared under CC0 as derived test artifacts. Creators are credited here even where attribution is not required. No non-CC0 third-party recording or its derived MIDI is included.
