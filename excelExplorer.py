import xlrd
import secretStuff
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
def sendSocialMedia():
    criteria = getCriteria()
    recipient = input("Recipient: ")
    try:
        print('\n- - - - - - -\n')
        for row in range(sheet.nrows):
            if passFilter(row, criteria):
                text = 'Name: %s \nSocial Media: %s' % (cellVal(row, g.name[0]), cellVal(row, g.social[0]))
                print('Text Message: %s \nSent to: %s\n' % (text, recipient))
                g.send_Message(text, secretStuff.phoneNums[recipient])

    except Exception:
        n = input("What is %'s phone Number?" % recipient)
        g.phoneNums[recipient] = n
        try:
            for row in range(sheet.nrows):
                if passFilter(row, criteria):
                    text = 'Name: %s \nSocial Media: %s' % (cellVal(row, g.name[0]), cellVal(row, g.social[0]))
                    g.send_Message(text, g.phoneNums[recipient])
                    print('Text Message: %s \n Sent to: %s' % (text, recipient))
        except Exception:
            print("An Error Has Been Made")



sendSocialMedia()