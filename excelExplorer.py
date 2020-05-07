import xlrd
import guide as g
file = r"C:\Users\alexm\Downloads\RU Ready to Find a Roommate_ (Responses) (1).xlsx"
wb = xlrd.open_workbook(file)
sheet = wb.sheet_by_index(0)


#cell_value is row, column
def cellVal(row,col):
    return sheet.cell_value(row,col)
def passFilter(row):
    if cellVal(row,g.sex[0]).lower() == 'female':
        return False
    if cellVal(row,g.residential[0]).lower().find("honor") == -1:
        return False
#   for n in g.negatives:
#        if cellVal(row,g.guests[0]).lower().find(n) > 0:
#            return False
    return True





def tester():
    matchCount = 0
    noMatchCount = 0
    for row in range(sheet.nrows):
        if passFilter(row):
            matchCount += 1
            print("Name: %s \nSocial: %s \nMajor: %s" % (cellVal(row,g.name[0]), cellVal(row,g.social[0]), cellVal(row,g.major[0])))
            print('-----------------------------')
        else:
            noMatchCount += 1
    print("Matches: %s \nNon-Matches: %d" % (matchCount, noMatchCount))

tester()