# CTN v1.0

A simple command-line tool to convert chord names to their constituent notes. Perfect for musicians, students, and developers learning music theory.

## Motivation

I recently got into live coding music with [strudel.cc](https://strudel.cc/), a pattern-based sequencer that works with pitch classes and note numbers rather than traditional note names (well, at least it's easier that way). When I wanted to voice specific chords, I kept having to look up which numbers corresponded to which notes — and I couldn't find a simple tool that did the conversion cleanly from a chord name. So I built one.

## Features

- **Wide Chord Support**: Handles major, minor, seventh, ninth, eleventh, thirteenth chords, augmented, diminished, suspended, and power chords.
- **Accidentals**: Supports sharps (#) and flats (b) in root notes.
- **Slash Chords**: Includes bass notes (e.g., Gm/E).
- **Case-Insensitive**: Accepts chords in any case (e.g., "Cm7", "cm7").
- **Enharmonic Equivalents**: Automatically selects appropriate note names based on chord type.

## Quick Start

1. Clone the repository:
   ```bash
   git clone https://github.com/amirsolobass/chordtonote.git
   cd chordtonote
   ```

2. Ensure Python 3.8+ is installed.

3. Run directly (no dependencies required):
   ```bash
   python3 src/main.py "C"
   ```

## Usage

```bash
python3 src/main.py <chord>
```

### Examples

- Basic chords:
  ```bash
  $ python3 src/main.py "C"
  Chord: C
  Notes: C E G

  $ python3 src/main.py "Cm"
  Chord: Cm
  Notes: C Eb G
  ```

- Seventh chords:
  ```bash
  $ python3 src/main.py "C7"
  Chord: C7
  Notes: C E G Bb

  $ python3 src/main.py "Cm7"
  Chord: Cm7
  Notes: C Eb G Bb
  ```

- Sharp/flat roots:
  ```bash
  $ python3 src/main.py "F#"
  Chord: F#
  Notes: F# A# C#

  $ python3 src/main.py "Bb"
  Chord: Bb
  Notes: Bb D F
  ```

- Slash chords:
  ```bash
  $ python3 src/main.py "Gm/E"
  Chord: Gminor/E
  Notes: E G Bb D
  ```

- Case-insensitive:
  ```bash
  $ python3 src/main.py "bdIm"
  Chord: bdim
  Notes: B D F
  ```

## Supported Chords

- **Triads**: major, minor, dim, aug, sus2, sus4, 5 (power)
- **Seventh Chords**: maj7, m7, 7, m7b5, dim7, aug7, augmaj7, mmaj7, 7sus4, 7sus2
- **Extended Chords**: maj9, m9, 9, m9b5, aug9, augmaj9, mmaj9
- **Eleventh & Thirteenth**: maj11, m11, 11, m11b5, aug11, augmaj11, mmaj11, maj13, m13, 13, m13b5, aug13, augmaj13, mmaj13

## Development

Run tests:
```bash
python3 src/test_chordtonote.py
```

## Contributing

Feel free to contribute as you wish, please fork the repository and open a pull request to the `main` branch

## License

MIT License
