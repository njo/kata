import json
import re
import sys

debug = False  # toggle debug to print broken lines

#  All the individual fields we care about
last = r'(?P<lastname>[A-z]+)'
first = r'(?P<firstname>[A-z]+(\s\w\.)?)'
phone = r'(?P<phonenumber>.+)'
color = r'(?P<color>[A-z ]+)'
zipcode = r'(?P<zipcode>\d{5})'
delim = r',\s+'

#  Build the known csv formats from the fields
patterns = map(re.compile, [
    # Lastname, Firstname, (703)-742-0996, Blue, 10013
    delim.join([last, first, phone, color, zipcode + "$"]),
    # Firstname Lastname, Red, 11237, 703 955 0373
    delim.join([first + " " + last, color, zipcode, phone]),
    # Firstname, Lastname, 10013, 646 111 0101, Green
    delim.join([first, last, zipcode, phone, color])
])


class Rolodex():
    """Parses and stores contact records from csv."""

    def __init__(self):  # noqa
        self.errors = []     # Store the entry number of any records failed to be parsed
        self.entries = []    # Correctly parsed entries (unsorted)
        self.processed = 0   # Number of raw records we've processed

    def insert(self, line):
        """
        Insert a new contact into this Rolodex.

        @param line: csv input string matching one of the known patterns.
        """
        self.processed += 1
        data = {}
        for pattern in patterns:
            m = pattern.match(line)
            if not m:
                continue

            phone = re.sub("[^0-9]", "", m.group("phonenumber"))
            if len(phone) == 10:
                data["phonenumber"] = "{}-{}-{}".format(phone[:3], phone[3:6], phone[6:])
            elif len(phone) == 7:
                data["phonenumber"] = "{}-{}".format(phone[:3], phone[3:7])
            else:
                break   # Invalid phone number

            for field in ["lastname", "firstname", "color", "zipcode"]:
                data[field] = m.group(field)

        if data:
            self.entries.append(data)
        else:
            if debug:
                print >> sys.stderr, line
            self.errors.append(self.processed - 1)

    def export(self):
        """Export this object's errors and entries as a dict."""
        self.entries.sort(key=lambda d: d["lastname"] + d["firstname"])
        return {
            "entries": self.entries,
            "errors": self.errors
        }

    def export_json(self, indent=2):
        """Export this object's errors and entries as json formatted string."""
        return json.dumps(self.export(), indent=indent, sort_keys=True)


if __name__ == "__main__":
    """
    Parse a csv rolodex and export the data as json to a file.

    Reads either the lines from files passed as args or stdin.
    """

    import fileinput

    rolodex = Rolodex()

    for line in fileinput.input():
        rolodex.insert(line)

    with open('result.out', 'w') as f:
        f.write(rolodex.export_json())
