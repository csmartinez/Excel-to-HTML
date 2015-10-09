# Excel to HTML

## Contributors

* [Carli Martinez](https://github.com/csmartinez)

A basic one-script python project to convert excel data to HTML option values. The issue that is solved with this project is individually copying and pasting option values and titles from excel into HTML format, a long and mundane task when you have over 100 entries to convert. This script and it's instructions require Microsoft Word 2011 for Mac.

Example input:
"1,2,3","one,two,three"

Example output:
"<option value='1'>one</option>
<option value='2'>two</option>
<option value='3'>three</option>"

## Instructions

 1. Copy all values or titles from excel and paste in Microsoft Word (2011)
 2. Convert the values or titles to text (Table > Convert > Convert Table to Text > (Seperate by paragraph)
 3. Find and replace paragraph marks with , for program ids and % for titles
 4. Remove any extra characters at end of document
 5. After doing this for both values and titles, paste the two strings into the argument of print statement, save file and press F5
 6. Verify first and last entries match with excel list

## Requirements

* Python 3.5
* IDLE


## Run the App

- open in IDLE
- save file
- hit F5


## Contribute

- Issue Tracker: github.com/csmartinez/Basic-Python-Projects/issues
- Source Code: github.com/csmartinez/Basic-Python-Projects
