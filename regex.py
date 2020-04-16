#!/usr/bin/python3
#regex test program for phone numbers

import re

phonenumregex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d)')
mo = phonenumregex.search('my number is 415-555-4242.')
print('phone number: '+mo.group(1)+'  '+mo.group(2))
