# Excel to HTML

## Contributors

* [Carli Martinez](https://github.com/csmartinez)

A basic one-script python project to convert excel data to HTML option values. The issue that is solved with this project is individually copying and pasting option values and titles from excel into an HTML drop down menu, a long and mundane task when you have over 100 entries to convert. This project and it's instructions require Microsoft Word 2011 for Mac.

V2 - Added optgroup labels as a mandatory input, must be same size as values and titles. Use V1 if no optgroup labels are necessary.

Update 10/2015 - No longer requires manual pasting into script, now prompts for information.

Example input:
"1,2,3,a,b,c"
"one%two%three%A%B%C"
"numbers%numbers%numbers%letters%letters%letters"

Example output:
```HTML
<optgroup label="numbers">
<option value='1'>one</option>
<option value='2'>two</option>
<option value='3'>three</option>
</optgroup>
<optgroup label="letters">
<option value='a'>A</option>
<option value='b'>B</option>
<option value='c'>C</option>
</optgroup>
```

## Instructions

 1. Copy all values or titles from excel and paste in Microsoft Word (2011)
 2. Convert the values or titles to text (Table > Convert > Convert Table to Text > (Seperate by paragraph)
 3. Find and replace paragraph marks with , for program ids and % for titles and labels
 4. Remove any extra characters at end of document, save, and hit F5
 5. Paste the corresponding strings in when prompted
 6. Verify first and last entries match with excel list. A counter is coded in to make sure the sizes match.

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
