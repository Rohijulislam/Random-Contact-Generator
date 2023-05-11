import random
import string
import vobject
import os

from faker import Faker

fake = Faker()

def generate_contact():
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = f'{first_name.lower()}.{last_name.lower()}@example.com'
    
    # Generate a random number of phone numbers for each contact (between 1 and 3)
    num_phone_numbers = random.randint(1, 3)
    phone_numbers = ["".join(random.choices(string.digits, k=10)) for _ in range(num_phone_numbers)]
    
    # Generate random labels for each phone number
    labels = ['Phone', 'Home', 'Work']
    phone_number_labels = random.choices(labels, k=num_phone_numbers)

    vcard = vobject.vCard()
    vcard.add('fn').value = f'{first_name} {last_name}'
    vcard.add('n').value = vobject.vcard.Name(family=last_name, given=first_name)
    vcard.add('email').value = email

    # Add phone numbers with corresponding labels
    for i in range(num_phone_numbers):
        tel_prop = vcard.add('tel')
        tel_prop.value = phone_numbers[i]
        tel_prop.type_param = [phone_number_labels[i]]

    return vcard.serialize()

# Generate 5,000 contacts
contacts = [generate_contact() for _ in range(5000)]

# Get the directory where the Python file is located
current_directory = os.path.dirname(__file__)
print(current_directory)

# Specify the file name and the directory where you want to save the VCF file
file_name = "contacts.vcf"
file_path = os.path.join(current_directory, file_name)

# Save contacts to the VCF file
with open(file_path, 'w') as vcf_file:
    vcf_file.write('\n'.join(contacts))
