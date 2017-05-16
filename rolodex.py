import json
import re

# All the CSV formats we know about
patterns = map(re.compile, [
    # Lastname, Firstname, (703)-742-0996, Blue, 10013
    r'(?P<lastname>[A-z]+),\s+(?P<firstname>[A-z]+(\s\w\.)?),\s+(?P<phonenumber>.+),\s+(?P<color>[A-z ]+),\s+(?P<zipcode>\d{5})',
    # Firstname Lastname, Red, 11237, 703 955 0373
    r'(?P<firstname>[A-z]+(\s\w\.)?)\s+(?P<lastname>[A-z]+),\s+(?P<color>[A-z ]+),\s+(?P<zipcode>\d{5}),\s+(?P<phonenumber>.+)',
    # Firstname, Lastname, 10013, 646 111 0101, Green
    r'(?P<firstname>[A-z]+(\s\w\.)?),\s+(?P<lastname>[A-z]+),\s+(?P<zipcode>\d{5}),\s+(?P<phonenumber>.+),\s+(?P<color>[A-z ]+)',
])


class Rolodex():
    """Parses and stores contact records from csv."""

    errors = []     # Store the entry number of any records failed to be parsed
    entries = []    # Correctly parsed entries (unsorted)
    processed = 0   # Number of raw records we've processed

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
            if len(phone) != 10:  # The instructions mention 7 digits but all the examples are 10 so I went with that
                break

            data["phonenumber"] = "{}-{}-{}".format(phone[:3], phone[3:6], phone[6:])

            for field in ["lastname", "firstname", "color", "zipcode"]:
                data[field] = m.group(field)

        if data:
            self.entries.append(data)
        else:
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
    import fileinput

    rolodex = Rolodex()

    for line in fileinput.input():
        rolodex.insert(line)

    with open('result.out', 'w') as f:
        f.write(rolodex.export_json())
