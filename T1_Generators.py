import random
import string
from datetime import datetime, timedelta
import csv 

# Generate row numbering
def row_num(n):
    i = 1
    while i <= n:
        yield i
        i += 1

# Generate a random word
def random_word(length=9):
    word=''.join(random.choices(string.ascii_lowercase, k=length))
    return word

# Generate a random date
def random_date(min_year=1900, max_year=datetime.now().year):
    start = datetime(min_year, 1, 1)
    end = datetime(max_year, 12, 31)
    delta = end - start
    result=start + timedelta(days=random.randint(0, delta.days))
    return result.strftime("%Y-%m-%d 00:00:00")


# Generate a random boolean
def random_boolean():
    bool=random.choice(["True","False"])
    return bool


#####################################################
# Generate rows of data
def generate_row(rows):
    for num in row_num(rows):
        yield [
            num,
            random_word(),
            random_date(),
            random_boolean()
        ]

def generate_file(filename,rows):
    with open(filename,mode="w",newline='') as file:
            writes=csv.writer(file,quoting=csv.QUOTE_ALL)

            # Insert a header row
            writes.writerow(['id', 'word', 'date', 'boolean'])

            for row in generate_row(rows):
                writes.writerow(row)

generate_file('generated_file.csv',20)
