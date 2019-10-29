# Write a program to read through the mbox-short.txt
# and figure out who has sent the greatest number of mail messages.
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times
# they appear in the file. After the dictionary is produced,
# the program reads through the dictionary using a maximum loop to find the most prolific committer.


name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

counter = dict()


for line in handle:
    if not line.startswith('From '):
        continue
    wrds = line.rstrip().split()
    sender = wrds[1]
    counter[sender] = counter.get(sender, 0) + 1

maxcounter = 0
maxsender = None

for key, value in counter.items():
    if maxcounter < 1 or maxcounter < value:
        maxcounter = value
        maxsender = key

print(maxsender, maxcounter)

