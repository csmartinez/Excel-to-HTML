# "Excel to HTML" By Carli Martinez
# 1. Copy ids and program titles seperately from excel and paste in Microsoft Word (2011)
# 2. Convert the ids or titles to text (Table > Convert > Convert Table to Text > (Seperate by paragraph)
# 3. Find and replace paragraph marks with , for program ids and % for titles
# 4. Remove any extra characters at end of document
# 5. Paste as two strings into arguement of print statement below and press F5

# number of IDs must have same length as number of titles to ensure they match up
# check last values from excel list to make sure output is correct

def excel_to_html(programs, titles):
    print("")
    programs = programs.split(",")
    titles = titles.split("%")

    if len(programs) == len(titles):
        for program, title in zip(programs, titles):
            print("<option value='" + program + "'>" + title + "</option>")
        return("")
    else:
        return("Error : Check length")

x = input("Please enter ids: \n")
y = input("Please enter titles: \n")
print(excel_to_html(x,y))

