tell application "Notes"
  repeat with n in notes
    set b to get body of n
    set t to get name of n
    set c to t & b
    do shell script "python add_note_to_db.py " & quoted form of c
  end repeat
end tell


