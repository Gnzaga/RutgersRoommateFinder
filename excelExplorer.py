import xlrd
import guide as g
file = r"/Users/Alex/PythonProjects/roomMateFinder/RU Ready to Find a Roommate? (Responses).xlsx"
wb = xlrd.open_workbook(file)
sheet = wb.sheet_by_index(0)


#cell_value is row, column
def cellVal(row,col):
    return sheet.cell_value(row,col)

def passFilter(row, criteria):
    for key, value in criteria.items():
        if cellVal(row, g.guide[key][0]).lower().find(value.lower()) == -1:
            return False
    return True



#criteria is a linked-list
def testForRoommates():
    matchCount = 0
    noMatchCount = 0
    criteria = getCriteria()
    for row in range(sheet.nrows):
        if passFilter(row, criteria):
            matchCount += 1
            print("Name: %s \nSocial: %s \nMajor: %s \nGender: %s" % (cellVal(row,g.name[0]), cellVal(row,g.social[0]), cellVal(row,g.major[0]), cellVal(row,g.sex[0])))
            print('-----------------------------')
        else:
            noMatchCount += 1
    print("Matches: %s \nNon-Matches: %d" % (matchCount, noMatchCount))

def getCriteria():
    criteria = {}
    print("Criteria for roommate search \n"
          "LEAVE BLANK IF NOT APPLICABLE \n"
          "- - - - - - - - - -")
    for key in g.critGuide:
        a = input("%s: " % (key))
        criteria[key] = a
    return criteria

testForRoommates()