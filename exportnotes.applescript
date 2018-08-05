tell application "Notes"
  set ff to first folder whose name = "exporttest"
  set ns to notes of ff
  repeat with n in ns
    set b to get body of n
    set t to get name of n
    set c to t & b
    do shell script "python add_note_to_db.py " & quoted form of c
  end repeat
end tell


