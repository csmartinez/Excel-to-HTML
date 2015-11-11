# "Excel to HTML" By Carli Martinez
# 1. Copy ids, program titles, and optgroup titles seperately from excel and paste in Microsoft Word (2011)
# 2. Convert the ids or titles to text (Table > Convert > Convert Table to Text > (Seperate by paragraph)
# 3. Find and replace paragraph marks with , for program ids and % for titles
# 4. Remove any extra characters at end of document
# 5. Paste as two strings into arguement of print statement below and press F5

# number of IDs must have same length as number of titles to ensure they match up
# check last values from excel list to make sure output is correct

def excel_to_html(programs, titles,campuses):
    print("")
    campuses = campuses.split("%")
    programs = programs.split(",")
    titles = titles.split("%")
    campus_list = []

    if len(programs) == len(titles) == len(campuses):
        for program, title, campus in zip(programs, titles, campuses):
            if campus not in campus_list:
                campus_list.append(campus)
                print("</optgroup>")
                print("<optgroup label='" + campus + "'>")
                print('<option value="' + program + '">' + title + '</option>')
            else:
                print('<option value="' + program + '">' + title + '</option>')
        print("</optgroup>")
                
        return("")
    else:
        print("Programs : " + str(len(programs)))
        print("Titles : " + str(len(titles)))
        print("Campuses : " + str(len(campuses)))
        return("Error : Check length")

p = input("Program ids: \n")
t = input("Program titles: \n")
c = input("Campus titles: \n")
print(excel_to_html(p,t,c))
