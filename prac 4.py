STATE_NAMES = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA" : "Western Australia", "ACT":"Australian Capital Territory", "VIC":"Victoria", "TAS":"Tasmania"}
for key,val in STATE_NAMES.items():
    print("{:4} is {}".format(key, val))