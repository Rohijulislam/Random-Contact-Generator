# VCF-Contact-Generator
This is a simple Python script that generates a VCF (vCard) file containing a set of random contacts. Each contact includes a first name, last name, email address, and one or more phone numbers with corresponding labels.

## Dependencies

The script relies on the following Python packages:

- `vobject`: A Python package for parsing and creating iCalendar and vCard files. You can learn more about it here: https://github.com/eventable/vobject

- `faker`: A Python package for generating realistic fake data. It is used to generate random names and email addresses for the contacts. You can find more information here: https://github.com/joke2k/faker

## Installation
1. Make sure you have Python 3.x installed on your system. If not, you can download and install Python from the official website: [Python Downloads](https://www.python.org/downloads/).

2. Clone this repository or download the script `generate_contacts.py` to your local machine.

3. Install the required Python dependencies by running the following command in your terminal:

   ```shell
   pip install vobject faker
   ```
   If you have both Python 2 and Python 3 installed, and pip is associated with Python 2, use pip3 instead:

   ```shell
   pip3 install vobject faker 
   ```
 
   **Note:** If pip or pip3 command is not recognized, make sure to install pip for your Python version.
   
## Customization
- If you want to adjust the number of contacts generated, you can modify the `range` value in the line `contacts = [generate_contact() for _ in range(5000)]`. Change `5000` to your desired number.

- To change the file name of the generated VCF file, update the `file_name` variable in the script.

- You can also modify the labels used for phone numbers by updating the `labels` list in the script. Add or remove labels as needed.

## Usage
- Open the generate_contacts.py file in a text editor.

- Customize the script if needed. For example, you can modify the number of contacts to generate by changing the value in the range() function. Save the script.

- Open your terminal or command prompt and navigate to the directory where the script is located.

- Run the script using the following command:
    ```shell
    python generate_contacts.py
   ``` 
   You can also run the script in any python IDE like VSCode.
- The script will generate a VCF file containing 5,000 contacts. The file will be saved in the same directory as the script.
- You can import the VCF file into your contact manager, phone app or simulator to add the contacts

  **Note:**  Feel free to modify the code and adapt it to your requirements. **Enjoy generating contacts!**

## Contact Information
For any questions or issues, please feel free to reach out to me 
<p left="center">
  
  <a href="https://www.linkedin.com/in/rohejul-islam-666746186/" target="blank">
  <img src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/stack-overflow.svg?&style=for-the-badge&logo=linkedin&logoColor=white" height=25>
</a> 
  
 
<a href="mailto:islamrohijulr@gmail.com">
  <img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" height=25>
</a>
  
  <a href="https://stackoverflow.com/users/rohejul islam" target="blank">
  <img src="https://img.shields.io/badge/linkedin-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white" height=25>
</a> 

</p>

