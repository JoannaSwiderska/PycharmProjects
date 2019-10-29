# Write a program to read through the mbox-short.txt
# and figure out the distribution by hour of the day for each of the messages.
# You can pull the hour out from the 'From ' line by finding the time
# and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour.



name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

counter = dict()

for line in handle:
    if not line.startswith('From '):
        continue
    wrds = line.rstrip().split()
    timer = wrds[5]
    timer_parts = timer.split(':')
    hr = timer_parts[0]
    counter[hr] = counter.get(hr, 0) + 1

counter_sort = sorted(counter.items())

for k, v in counter_sort:
    print(k, v)
