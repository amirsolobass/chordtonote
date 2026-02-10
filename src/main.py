import argparse
from root_extraction import extract_root_regex
from note_calc import *
from interval_maps import (TRIADS, SEVEN_CHORDS, NINE_CHORDS, ELEVEN_CHORDS, THIRTEEN_CHORDS)



def main():
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(prog="chordtonote",
        description="Convert chord names to their note values.",
        usage="%(prog)s [options] <chord>",
        )
    # Add arguments
    parser.add_argument("chord", type=str, help="The chord name to convert (e.g., Cmaj7, D#m, F#dim).")
    parser.add_argument("-v", "--version", help="Display the program's version.")
    # Parse arguments
    args = parser.parse_args()

    # merge all chord types into one dictionary for easy lookup
    chord_master_map = {**TRIADS, **SEVEN_CHORDS, **NINE_CHORDS, **ELEVEN_CHORDS, **THIRTEEN_CHORDS}
    chord_master_map[""] = chord_master_map["major"]  # default to major if no type specified
    
    # quality aliases
    quality_aliases = {
        "min": "minor",
        "m": "minor",
        "": "major",
        "MAJ": "major",
    }
    
    try:
        #extract root note and chord quality
        root, quality, slash_notes = extract_root_regex(args.chord)
        quality = quality.lower()
        quality = quality_aliases.get(quality, quality)
        if quality not in chord_master_map:
            raise ValueError(f"Unknown chord quality: {quality}")
        intervals = chord_master_map.get(quality)
        if intervals is None:
            raise ValueError(f"{args.chord} is not a chord bruh.")
        
        # calculate note values and map to names
        pitch_classes = list(calculate_notes(root, intervals))
        note_names = list(get_note_names(pitch_classes, root, quality))

        if slash_notes:
            # add bass note and reorder
            bass_pitch = list(calculate_notes(slash_notes, [0]))[0]
            if bass_pitch not in pitch_classes:
                pitch_classes.append(bass_pitch)
            # sort pitches starting from bass
            sorted_pitches = sorted(pitch_classes, key=lambda x: (x - bass_pitch) % 12)
            note_names = list(get_note_names(sorted_pitches, root, quality))

        # Output results
        chord_name = f"{root}{quality}"
        if slash_notes:
            chord_name += f"/{slash_notes}"
        print(f"Chord: {chord_name}")
        print(f"Notes: {' '.join(note_names)}")

    except ValueError as e:
        print(f"Error: {e}")





if __name__ == "__main__":
    main()
