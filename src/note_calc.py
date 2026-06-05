
from interval_maps import NOTE_TO_INT, INT_TO_NOTES, INTERVAL_TO_DEGREE

def calculate_notes(base_note, intervals):
    """Get the note names for a given base note and intervals."""
    normalized_note = base_note[0].upper() + base_note[1:]
    base_value = NOTE_TO_INT.get(normalized_note)
    if base_value is None:
         raise ValueError("That's not a note bruh. A-G only.")

    for interval in intervals:
        if interval < 0 or interval > 21:
            raise ValueError(f"Invalid interval: {interval}. Must be between 0 and 21.")
        yield (base_value + interval) % 12 # return pitch classes as integers for now, will map to names later

def interval_to_degree(interval: int, quality: str, chord_intervals: list = None) -> str:
    if interval == 6:
        return "b5" if ("dim" in quality or "b5" in quality) else "#4"
    if interval == 9:
        if chord_intervals and 3 in chord_intervals and 6 in chord_intervals:
            return "bb7"
        return "6"
    return INTERVAL_TO_DEGREE.get(interval, str(interval))

def get_note_names(pitch_classes, root, quality=""):
    """Map the calculated note values back to their names ENHARMONICALLY CORRECT."""
    # Determine if the root note contains sharps or flats to guide selection of enharmonic equivalents
    use_sharps = "#" in root
    use_flats = ("b" in root or "m" in quality.lower() or "dim" in quality.lower()) and not use_sharps
    if use_flats and use_sharps:
            raise ValueError(f"Invalid root note: {root}. Cannot contain both sharps and flats.")
    # If neither sharps nor flats are present, default to natural notes, but allow for accidental selection if necessary
    for pitch in pitch_classes:
        options = INT_TO_NOTES[pitch] # for based O(1) lookup
        if use_flats:
             selection = next((note for note in options if len(note) == 1), None)
             if selection is None:
                 selection = next((note for note in options if "b" in note), options[0])
        elif use_sharps:
             selection = next((note for note in options if len(note) == 1), None)
             if selection is None:
                 selection = next((note for note in options if "#" in note), options[0])
        else:
             selection = next((note for note in options if len(note) == 1), options[0])
        
        yield selection