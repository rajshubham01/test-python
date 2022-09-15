import re

text = """ Hi, today is 14-Apr-2021, yesterday was 13-Apr-2021 and tomorrow will be 15-Apr-2021.
My schedule is free on 26-04-2021, 06.05.21 and 16/Jun/2021.
You can reach out to me at abnavemangesh@local.com or local_1@local.com & support@local.co.in
you can also call me at one of the following no's +603-007 1212, +6099.100 3344, 017-99988800. """

pattern = re.compile(r'\w+@[]')