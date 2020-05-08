import os
guide = {'name':[1],'sex':[2],'campus':[3],'major':[4],'social':[5],
                    'residential':[6],'clean':[7,8],'sleep':[9,10],'roommate':[11,12],
                    'likes':[13],'studying':[14],'committed':[15],'guests':[16],
                    'party':[17],'goHome':[18],'other':[19]}

critGuide = ['sex', 'major', 'residential']
name = guide['name']
sex = guide['sex']
campus = guide['campus']
major = guide['major']
social = guide['social']
residential = guide['residential']
clean = guide['clean']
sleep = guide['sleep']
roommate = guide['roommate']
likes = guide['likes']
studying = guide['studying']
committed = guide['committed']
guests = guide['guests']
party = guide['party']
goHome = guide['goHome']
other = guide['other']

negatives = ['no', 'guess', 'sometimes','depend', 'occasionally']



cmd = """osascript<<END
tell application "Messages"
send "%s" to buddy "%d" of (service 1)
end tell
END"""

def send_Message(text, phone):
    os.system(cmd % (text, phone))