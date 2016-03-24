import string
import urllib
import os
import argparse

# Each of these collections contains the acceptable choices the user may input for questions asked. It is used as error-checking to prevent incorrect
# input from being accepted.
valid_gender = {"male", "female", "m", "f"}
phone = ''
male_reasons = {"1", "2", "3", "4"}
female_reasons = {"1", "2", "3", "4"}
male_endings = {"1", "2", "3", "4"}
female_endings = {"1", "2"}

# This section of the code is to provide for command line input from the user using the arguments created below. They will enter -g with a gender option,
# -n with a phone number, etc., and the program will then parse the arguments
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-g', dest='gender', action='store')
    parser.add_argument('-n', dest='number', action='store')
    parser.add_argument('-r', dest='reason', action='store')
    parser.add_argument('-e', dest='ending', action='store')
    parser.add_argument('-o', dest='output', action='store')
    args = parser.parse_args()

    # Depending on whether the user is male or female, the program retrieves the mp3 slices to go at the beginning of the voicemail.
    if args.gender == "male" or args.gender == "m":
        urllib.urlretrieve("http://www-scf.usc.edu/~chiso/oldspice/m-b1-hello.mp3", "hello.mp3")
        urllib.urlretrieve("http://www-scf.usc.edu/~chiso/oldspice/m-b2-have_dailed.mp3", "dialed.mp3")

    if args.gender == "female" or args.gender == "f":
        urllib.urlretrieve("http://www-scf.usc.edu/~chiso/oldspice/f-b1-hello_caller.mp3", "hello.mp3")
        urllib.urlretrieve("http://www-scf.usc.edu/~chiso/oldspice/f-b2-lady_at.mp3", "dialed.mp3")

            
    # Depending on the reason and ending the user chose, the program downloads the according mp3 files.
    if args.gender == "male" or args.gender == "m":
            if args.reason == "1":
                 urllib.urlretrieve("http://www-scf.usc.edu/~chiso/oldspice/m-r1-building.mp3", "reason.mp3")
            if args.reason == "2":
                 urllib.urlretrieve("http://www-scf.usc.edu/~chiso/oldspice/m-r2-cracking_walnuts.mp3", "reason.mp3")
            if args.reason == "3":
                 urllib.urlretrieve("http://www-scf.usc.edu/~chiso/oldspice/m-r3-polishing_monocole.mp3", "reason.mp3")
            if args.reason == "4":
                 urllib.urlretrieve("http://www-scf.usc.edu/~chiso/oldspice/m-r4-ripping_weights.mp3", "reason.mp3")
            if args.ending == "1":
                 urllib.urlretrieve("http://www-scf.usc.edu/~chiso/oldspice/m-e1-horse.mp3", "end.mp3")
            if args.ending == "2":
               urllib.urlretrieve("http://www-scf.usc.edu/~chiso/oldspice/m-e2-jingle.mp3", "end.mp3")
            if args.ending == "3":
                urllib.urlretrieve("http://www-scf.usc.edu/~chiso/oldspice/m-e3-on_phone.mp3", "end.mp3")
            if args.ending == "4":
                urllib.urlretrieve("http://www-scf.usc.edu/~chiso/oldspice/m-e4-swan_dive.mp3", "end.mp3")
    else:
            if args.reason == "1":
                urllib.urlretrieve("http://www-scf.usc.edu/~chiso/oldspice/f-r1-ingesting_old_spice.mp3", "reason.mp3")
            if args.reason == "2":
                urllib.urlretrieve("http://www-scf.usc.edu/~chiso/oldspice/f-r2-listening_to_reading.mp3", "reason.mp3")
            if args.reason == "3":
                urllib.urlretrieve("http://www-scf.usc.edu/~chiso/oldspice/f-r3-lobster_dinner.mp3", "reason.mp3")
            if args.reason == "4":
                urllib.urlretrieve("http://www-scf.usc.edu/~chiso/oldspice/f-r4-moon_kiss.mp3", "reason.mp3")
            if args.ending == "1":
                urllib.urlretrieve("http://www-scf.usc.edu/~chiso/oldspice/f-e1-she_will_get_back_to_you.mp3", "end.mp3")
            if args.ending == "2":
                urllib.urlretrieve("http://www-scf.usc.edu/~chiso/oldspice/f-e2-thanks_for_calling.mp3", "end.mp3")

    if os.name == "nt":
        os.system("copy /b hello.mp3 + dialed.mp3 + reason.mp3 + end.mp3 " + str(args.output) + ".mp3")
    else:
        os.system("cat hello.mp3 dialed.mp3 reason.mp3 end.mp3 > " + str(args.output) + ".mp3")

    
# This emcompassing while loop contains all the questions/choices for the user to input regarding how they want to customize their voicemail message.
# This loop will be broken out of when the user sees a summary of the information they entered and accepts it. If they reject it, the program returns
# to the top of the loop and executes again.
while True:
    while True:
            gender = raw_input("What gender would you like this voicemail to be? Enter 'male', 'female', 'm' or 'f':\n")
            if gender in valid_gender:
                    break

    while True:
            p = str(raw_input("What is your phone number?\n:"))
            for n in p:
                # Finds the digit values in the phone number entered and saves them, since the user may have entered a phone number with parentheses in the format.
                    if n in string.digits:
                            phone += n
            # The phone number must be ten digits, or it is incorrect and the program will ask for another entry.
            if len(phone) == 10:
                    break
            else:
                phone = ''

    # If the user wants a male voicemail, these are the reasons they have to choose from.
    if gender == "male" or gender == "m":
        while True:
            malereason = raw_input("What reason would you like to include in your voicemail?\n (1) Building\n (2) Cracking Walnuts\n (3) Polishing Monocole\n (4) Ripping Weights\n Enter your choice (1-4):\n")
            if malereason in male_reasons:
                break

    # If the user wants a female voicemail, these are the reasons they have to choose from.
    if gender == "female" or gender == "f":
        while True:
            femalereason = raw_input("What reason would you like to include in your voicemail?\n (1) Ingesting Old Spice\n (2) Listening to Reading\n (3) Lobster Dinner\n (4) Moon Kiss\n Enter your choice (1-4):\n")
            if femalereason in female_reasons:
                break

    # The ending choices for male voicemail.
    if gender == "male" or gender == "m":
        while True:
            maleend = raw_input("What ending would you like to include in your voicemail?\n (1) Horse\n (2) Jingle\n (3) On Phone\n (4) Swan Dive\n Enter your choice (1-4):\n")
            if maleend in male_endings:
                break

    # The ending choices for female voicemail.
    if gender == "female" or gender == "f":
        while True:
            femaleend = raw_input("What ending would you like to include in your voicemail?\n (1) She will get back to you\n (2) Thanks for calling\n Enter your choice (1-2):\n")
            if femaleend in female_endings:
                break

    # Depending on the user's input choices, this prints a summary of the user's entered gender, phone number, reason, and ending.         
    print("SUMMARY")
    print("Gender: " + gender)
    print("Phone: " + phone)
    if gender == "male" or gender == "m":
        if malereason == "1":
            print("Reason: Buildings")
        if malereason == "2":
            print("Reason: Cracking Walnuts")
        if malereason == "3":
            print("Reason: Polishing Monocoles")
        if malereason == "4":
            print("Reason: Ripping Weights")
        if maleend == "1":
            print("Ending: Horse")
        if maleend == "2":
            print("Ending: Jingle")
        if maleend == "3":
            print("Ending: On Phone")
        if maleend == "4":
            print("Ending: Swan Dive")
    else:
        if femalereason == "1":
            print("Reason: Ingesting Old Spice")
        if femalereason == "2":
            print("Reason: Listening to Reading")
        if femalereason == "3":
            print("Reason: Lobster Dinner")
        if femalereason == "4":
            print("Reason: Moon Kiss")
        if femaleend == "1":
            print("Ending: She will get back to you")
        if femaleend == "2":
            print("Ending: Thanks for calling")

    # If the user rejects the input, the program goes back to the top of the encompassing while loop. If they accept, it breaks out of the loop.
    accept = raw_input("If you don't accept this information, enter 'no'. Enter anything else if you do and wish to continue:\n")
    if accept == "no":
        phone = ''
        continue
    else:
        break

# Depending on whether the user is male or female, the program retrieves the mp3 slices to go at the beginning of the voicemail.
if gender == "male" or gender == "m":
    urllib.urlretrieve("http://www-scf.usc.edu/~chiso/oldspice/m-b1-hello.mp3", "hello.mp3")
    urllib.urlretrieve("http://www-scf.usc.edu/~chiso/oldspice/m-b2-have_dailed.mp3", "dialed.mp3")

if gender == "female" or gender == "f":
    urllib.urlretrieve("http://www-scf.usc.edu/~chiso/oldspice/f-b1-hello_caller.mp3", "hello.mp3")
    urllib.urlretrieve("http://www-scf.usc.edu/~chiso/oldspice/f-b2-lady_at.mp3", "dialed.mp3")

# This double while loop retrieves all the mp3 slices needed to read the phone number correctly. The inner while loop checks the current digit against
# each value from 0-9 until the correct one is reached and saves the matching mp3 file, and the outher while loop increments which digit of the phone
# number is currently being looked at.
p = 0
while p < 10:
    i = 0
    while i < 10:
        if int(phone[p]) == i:
            urllib.urlretrieve("http://www-scf.usc.edu/~chiso/oldspice/" + str(i) + ".mp3", str(p) + ".mp3")
            p = p + 1
            break
        else:
            i = i + 1
        
# Depending on the reason and ending the user chose, the program downloads the according mp3 files.
if gender == "male" or gender == "m":
        if malereason == "1":
             urllib.urlretrieve("http://www-scf.usc.edu/~chiso/oldspice/m-r1-building.mp3", "reason.mp3")
        if malereason == "2":
             urllib.urlretrieve("http://www-scf.usc.edu/~chiso/oldspice/m-r2-cracking_walnuts.mp3", "reason.mp3")
        if malereason == "3":
             urllib.urlretrieve("http://www-scf.usc.edu/~chiso/oldspice/m-r3-polishing_monocole.mp3", "reason.mp3")
        if malereason == "4":
             urllib.urlretrieve("http://www-scf.usc.edu/~chiso/oldspice/m-r4-ripping_weights.mp3", "reason.mp3")
        if maleend == "1":
             urllib.urlretrieve("http://www-scf.usc.edu/~chiso/oldspice/m-e1-horse.mp3", "end.mp3")
        if maleend == "2":
           urllib.urlretrieve("http://www-scf.usc.edu/~chiso/oldspice/m-e2-jingle.mp3", "end.mp3")
        if maleend == "3":
            urllib.urlretrieve("http://www-scf.usc.edu/~chiso/oldspice/m-e3-on_phone.mp3", "end.mp3")
        if maleend == "4":
            urllib.urlretrieve("http://www-scf.usc.edu/~chiso/oldspice/m-e4-swan_dive.mp3", "end.mp3")
else:
        if femalereason == "1":
            urllib.urlretrieve("http://www-scf.usc.edu/~chiso/oldspice/f-r1-ingesting_old_spice.mp3", "reason.mp3")
        if femalereason == "2":
            urllib.urlretrieve("http://www-scf.usc.edu/~chiso/oldspice/f-r2-listening_to_reading.mp3", "reason.mp3")
        if femalereason == "3":
            urllib.urlretrieve("http://www-scf.usc.edu/~chiso/oldspice/f-r3-lobster_dinner.mp3", "reason.mp3")
        if femalereason == "4":
            urllib.urlretrieve("http://www-scf.usc.edu/~chiso/oldspice/f-r4-moon_kiss.mp3", "reason.mp3")
        if femaleend == "1":
            urllib.urlretrieve("http://www-scf.usc.edu/~chiso/oldspice/f-e1-she_will_get_back_to_you.mp3", "end.mp3")
        if femaleend == "2":
            urllib.urlretrieve("http://www-scf.usc.edu/~chiso/oldspice/f-e2-thanks_for_calling.mp3", "end.mp3")

# Asks the user what they want to name the output mp3 and txt files generated.
voicemail = str(raw_input("What would you like to name your voicemail mp3 file? You don't need to include .mp3 extension.\n"))
output = str(raw_input("What would you like to name your output file listing the sliced mp3 files used? You don't need to include .txt extension.\n"))

# Detects what OS system the user is on, and depending on that, calls the according external command to combine all the mp3 files needed.
if os.name == "nt":
    os.system("copy /b hello.mp3 + dialed.mp3 + 0.mp3 + 1.mp3 + 2.mp3 + 3.mp3 + 4.mp3 + 5.mp3 + 6.mp3 + 7.mp3 + 8.mp3 + 9.mp3 + reason.mp3 + end.mp3 " + voicemail + ".mp3")
else:
    os.system("cat hello.mp3 dialed.mp3 0.mp3 1.mp3 2.mp3 3.mp3 4.mp3 5.mp3 6.mp3 7.mp3 8.mp3 9.mp3 reason.mp3 end.mp3 > " + voicemail + ".mp3")

# Writes to an external txt file, listing the mp3 files used.
logfile = open(output + '.txt', 'w')
logfile.write('hello.mp3 dialed.mp3 0.mp3 1.mp3 2.mp3 3.mp3 4.mp3 5.mp3 6.mp3 7.mp3 8.mp3 9.mp3 reason.mp3 end.mp3')
logfile.close()

print("Your new voicemail message has been created and is called " + voicemail + ".mp3")
print("The names of the mp3s used to make your voicemail have been outputted to file " + output + ".txt")
        
