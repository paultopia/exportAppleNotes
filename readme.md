applescript plus python script to get contents of apple notes and dump into a database.

only extracts plain text of notes---strips formatting and loses attachments. 

apple notes are formatted in html natively, this script uses beautifulsoup to get rid of html code and extract text.

if you want to export all notes, just run `osascript exportnotes.applescript`

If you want to export a folder, run the apple script with that name. replace references to "exporttest" with the name of the folder you want to export.

If you want to export to a text file instead of a database (with double line breaks between notes) replace references to the python script in your chosen applescript file with put_notes_in_text_file.py 
