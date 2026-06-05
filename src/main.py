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
    parser.add_argument("-n", "--numbers", action="store_true", help="Output notes as pitch classes (0-11) instead of note names.")
    parser.add_argument("-d", "--degrees", action="store_true", help="Output chord degrees (1, b3, 5, b7, etc.) instead of note names.")
    parser.add_argument("-v", "--version", action="version", version="CTN v1.0")
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
        final_pitches = pitch_classes

        if slash_notes:
            # add bass note and reorder
            bass_pitch = list(calculate_notes(slash_notes, [0]))[0]
            if bass_pitch not in pitch_classes:
                pitch_classes.append(bass_pitch)
            # sort pitches starting from bass
            sorted_pitches = sorted(pitch_classes, key=lambda x: (x - bass_pitch) % 12)
            note_names = list(get_note_names(sorted_pitches, root, quality))
            final_pitches = sorted_pitches

        # Output results
        chord_name = f"{root}{quality}"
        if slash_notes:
            chord_name += f"/{slash_notes}"
        print(f"Chord: {chord_name}")
        if args.degrees:
            degree_intervals = list(intervals)
            if slash_notes:
                root_pc = list(calculate_notes(root, [0]))[0]
                bass_iv = (bass_pitch - root_pc) % 12
                if not any(i % 12 == bass_iv for i in degree_intervals):
                    degree_intervals.append(bass_iv)
                degree_intervals.sort(key=lambda x: (x % 12 - bass_iv) % 12)
            print(f"Notes: {' '.join(interval_to_degree(i, quality, degree_intervals) for i in degree_intervals)}")
        elif args.numbers:
            print(f"Notes: {' '.join(str(p) for p in final_pitches)}")
        else:
            print(f"Notes: {' '.join(note_names)}")

    except ValueError as e:
        print(f"Error: {e}")





if __name__ == "__main__":
    main()
