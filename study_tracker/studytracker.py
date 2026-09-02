from pathlib import Path
log_file = Path(__file__).parent / "study_log.txt"

print("===Study Tracker===")
print("1. Security Fundamentals")
print("2. Web Programming")
print("3. Cisco Network Academy stuff")



choice = int(input("Choose a course: "))
# Choosing which course here allows for the program to start making the file for the notes, making it more easier for it to be organized
print("You Selected:",choice)
if choice == 1:
   course = "Security Fundamentals"
   print("Course:", course)

elif choice == 2:
    course = "Web Programming"
    print("Course:", course)

elif choice == 3:
    course = "Cisco Network Academy stuff"
    print("Course:", course)

else:
    print("invalid choice. gg")

from datetime import date
today = date.today()

topic = input("What Did You Study?")

notes = input("What did you learn? ")
# now after collecting all the info we need like what class it is, the topic, and what was learned we are now gonna get python to put it into a file for us
print("Alright so we're working on:",topic)
with open(log_file, "a") as file:
    file.write("Date:" + str(today) +"\n")
    file.write("Course:"+ course + "\n")
    file.write("Topic:"+ topic + "\n")
    file.write("Notes:" + notes + "\n")
    file.write("--------------------------" + "\n\n")
