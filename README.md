# Membership Card Generator
This Python program generates membership cards by overlaying text onto images. It uses data from a CSV file and allows for customization of the text's position, font, and color.

## Features
Customizable Text Overlay: Add names, roles, emails, and numbers to images in customizable positions.

Batch Processing: Generate multiple membership cards at once, either with a single image for all cards or different images for each card.

## Requirements

Python 3.x

Pillow (Python Imaging Library)

## Installation
Clone the repository:

```git clone https://github.com/HundredMinus1/membership-card-generator.git```

Navigate to the project directory:

```cd image-generator```

Install the required Python packages:

`pip install -r requirements.txt`

### Prepare your CSV file containing the membership data. The file should have the following columns:

`Name`

`Role`

``Email``

``Number``

Single image mode: ./input/single/

Multiple images mode: ./input/multi/

**Run the script:**

python membership_card_generator.py

Enter the type of membership cards you want to generate:

`1` for using a single image for all cards.

`2` for using different images for each card.
### The generated membership cards will be saved in the corresponding output folder:

Single image mode: ./output/single/

Multiple images mode: ./output/multi/

## Customization 
Font and Text Properties: Adjust the font type and size in the add_text_to_image method by modifying the ImageFont.truetype path and size parameters.

Text Positions: Modify the **name_pos**, **role_pos**, **email_pos**, and **number_pos** variables in the **add_text_to_image** method to change where the text appears on the image.

Output Filenames: The output filenames are generated using the name and role fields. You can modify this behavior in the add_text_to_image method.

## License
This project is licensed under the MIT License. See the [LICENSE](https://github.com/git/git-scm.com/blob/main/MIT-LICENSE.txt) file for details.
