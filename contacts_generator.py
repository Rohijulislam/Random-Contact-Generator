import random
import string
import vobject
import json
import xml.etree.ElementTree as ET
import configparser
import os
import csv
from faker import Faker
import random
from datetime import date, timedelta

# Constants for defining minimum and maximum ages
MIN_AGE = 18
MAX_AGE = 80

fake = Faker()

def generate_contact():
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = f'{first_name.lower()}.{last_name.lower()}@example.com'
    # Generate a random birthdate within the age range
    birthdate = fake.date_of_birth(tzinfo=None, minimum_age=MIN_AGE, maximum_age=MAX_AGE)


    # Generate a random number of phone numbers for each contact (between 1 and 3)
    num_phone_numbers = random.randint(1, 3)
    phone_numbers = ["".join(random.choices(string.digits, k=10)) for _ in range(num_phone_numbers)]
    
    # Generate random labels for each phone number
    labels = ['Phone', 'Home', 'Work']
    phone_number_labels = random.choices(labels, k=num_phone_numbers)

    return {
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'birthday':  birthdate.strftime('%Y-%m-%d'),
        'phone_numbers': phone_numbers,
        'phone_number_labels': phone_number_labels
    }

def generate_vcf_contacts(contacts, file_path):
    vcf_contacts = [vobject.vCard() for _ in range(len(contacts))]

    for i, contact in enumerate(contacts):
        vcf_contacts[i].add('fn').value = f"{contact['first_name']} {contact['last_name']}"
        vcf_contacts[i].add('n').value = vobject.vcard.Name(family=contact['last_name'], given=contact['first_name'])
        vcf_contacts[i].add('email').value = contact['email']
        vcf_contacts[i].add('bday').value = contact['birthday']

        for j, phone_number in enumerate(contact['phone_numbers']):
            tel_prop = vcf_contacts[i].add('tel')
            tel_prop.value = phone_number
            tel_prop.type_param = [contact['phone_number_labels'][j]]

    with open(file_path, 'w') as vcf_file:
        vcf_file.write('\n'.join([contact.serialize() for contact in vcf_contacts]))

def generate_json_contacts(contacts, file_path):
    with open(file_path, 'w') as json_file:
        json.dump(contacts, json_file, indent=4)

def generate_xml_contacts(contacts, file_path):
    root = ET.Element("contacts")
    for contact in contacts:
        contact_element = ET.SubElement(root, "contact")
        for key, value in contact.items():
            field_element = ET.SubElement(contact_element, key)
            field_element.text = str(value)
    tree = ET.ElementTree(root)
    tree.write(file_path)


def generate_cfg_contacts(contacts, file_path):
    config = configparser.ConfigParser()
    for i, contact in enumerate(contacts, start=1):
        section_name = f"Contact{i}"
        config[section_name] = contact
    with open(file_path, 'w') as cfg_file:
        config.write(cfg_file)




def generate_csv_contacts(contacts, file_path):
    """
    Generates CSV contact file.

    Args:
        contacts (list): List of contact data.
        file_path (str): File path to save the CSV file.
    """
    # Define the CSV file header
    fieldnames = ['First Name', 'Last Name', 'Email', 'Phone']

    # Write contacts to the CSV file
    with open(file_path, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        
        # Write the header row
        writer.writerow(fieldnames)

        # Write each contact as a row
        for contact in contacts:
            row = [contact['first_name'], contact['last_name'], contact['email'], contact['phone_numbers']], contact['birthday']
            writer.writerow(row)


# Generate 5,000 contacts
contacts = [generate_contact() for _ in range(5000)]

# Specify the file name and the directory where you want to save the contact files
current_directory = os.path.dirname(__file__)
file_name = "contacts"
output_directory = os.path.join(current_directory, "output")

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# Generate VCF contacts and save to file
vcf_file_path = os.path.join(output_directory, file_name + ".vcf")
generate_vcf_contacts(contacts, vcf_file_path)

# Generate JSON contacts and save to file
json_file_path = os.path.join(output_directory, file_name + ".json")
generate_json_contacts(contacts, json_file_path)

# Generate XML contacts and save to file
xml_file_path = os.path.join(output_directory, file_name + ".xml")
generate_xml_contacts(contacts, xml_file_path)

# Generate CFG contacts and save to file
cfg_file_path = os.path.join(output_directory, file_name + ".cfg")
generate_cfg_contacts(contacts, cfg_file_path)

# Generate CSV contacts and save to file
csv_file_path = os.path.join(output_directory, file_name + ".csv")
generate_csv_contacts(contacts, csv_file_path)
