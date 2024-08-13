from PIL import Image, ImageDraw, ImageFont
import csv
import os

class Generator_Image():
  def __init__(self, dirname, image_dir, data_path, output_dir, type):
      self.dirname = dirname
      self.image_dir = image_dir
      self.data_path = data_path
      self.output_dir = output_dir
      self.type = type

  # import data file
  def get_data_from_csv(filename):
    data = []
    try:
      with open(filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=';')  # Specify the delimiter as semicolon
        for row in reader:
          data.append(row)
    except FileNotFoundError:
      print(f"Error: CSV file not found: {filename}")
    return data
  
  def add_text_to_image(image_path, data_row, output_dir):
    j = 0
    k = 1
    l = 2
    m = 3
    try:
      # Open the image
      image = Image.open(image_path)
      draw = ImageDraw.Draw(image)
      # Assuming font path is correct

      # Define text positions (adjust as needed)
      name_pos = (80, 120)
      role_pos = (80, 170)
      email_pos = (113, 460)
      number_pos = (113, 532)

      # Extract data from the row (assuming name, ID, and Exp are in specific columns)
      name, role, email, number = data_row[j], data_row[k], data_row[l], data_row[m]  # Adjust column indices (j, k, l)
    
      # Add text elements
      draw.text(name_pos, name, fill='orange', font=ImageFont.truetype('./OpenSans-Bold.ttf', size=40))
      draw.text(role_pos, role, fill='orange', font=ImageFont.truetype('./OpenSans-Regular.ttf', size=32))
      draw.text(email_pos, email, fill='orange', font=ImageFont.truetype('./OpenSans-Regular.ttf', size=32))
      draw.text(number_pos, number, fill='orange', font=ImageFont.truetype('./OpenSans-Regular.ttf', size=32))

      # Create a temporary file to avoid overwriting (using 'with' for automatic closing)
      base_filename = f"{data_row[0]}"

      if os.path.exists(os.path.join(output_dir, f"{base_filename}.jpg")):
          print(f"Warning: Filename conflict detected for {name}.jpg. Skipping creation.")
          return  # Exit the function if conflict is found
      else:
        # Generate final filename based on data (assuming name is in the first column)
        final_filename = f"{data_row[0]+'_'+data_row[1]}.jpg"  # Adjust if name is in a different column
        image.save(os.path.join(output_dir, final_filename))
        print(f"\nYour ID Card for {name} successfully created: {final_filename}")

    except FileNotFoundError:
      print(f"Error: Image file not found: {image_path}")
    except Exception as e:
      print(f"An error occurred: {e}")
      
  def process_image(self):
      output_row = 0
      
      # Get data from CSV
      data = Generator_Image.get_data_from_csv(data_path)
      data = data[1:]
      # Process only the first row
      if data:  # Check if data is not empty
          image_path = os.path.join(image_dir, os.listdir(image_dir)[0])  # Assuming first image
          Generator_Image.add_text_to_image(image_path, data[0], output_dir)
      else:
          print("Data duplicated detected")
      
      image_path = os.path.join(image_dir, os.listdir(image_dir)[0])

      for i, image_filename in enumerate(os.listdir(image_dir)):
        if self.type == '1':
          for data_row in data:
            output_row += 1
            Generator_Image.add_text_to_image(image_path, data_row, output_dir)  # Process each data row with the image
            print("Single: ", data[i])
        elif self.type == '2':
          output_row += 1
          Generator_Image.add_text_to_image(image_path, data[i], output_dir)
          print("Multi: ", data[i])

      # Loop through images and data
      a = 1
      for i, image_filename in enumerate(os.listdir(image_dir)):
        image_path = os.path.join(image_dir, image_filename)
        Generator_Image.add_text_to_image(image_path, data[i], output_dir)
        print("Looped: ", data[i])
        
      print("total generated membership: ", output_row)


if __name__ == "__main__":
    # Replace with your actual directory paths
    type = input("Enter type of membership (single/multi): ")
    dirname = os.path.dirname(__file__)
    data_path = os.path.join(dirname, './data/small_data.csv')
    # data_path = os.path.join(dirname, './data/data.csv')

    if type == '2':
      image_dir = os.path.join(dirname, './input/multi/')
      output_dir = os.path.join(dirname, './output/multi/')
    elif type == '1':
      image_dir = os.path.join(dirname, './input/single/')
      output_dir = os.path.join(dirname, './output/single/')

    processor = Generator_Image(dirname, image_dir, data_path, output_dir, type)
    processor.process_image()

