import os

def create_folders_from_file(file_path, main_folder):
    # Create the main folder if it doesn't exist
    if not os.path.exists(main_folder):
        os.makedirs(main_folder)

    # Read the text file and create folders
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            # Remove newline characters and any leading/trailing whitespace
            folder_name = line.strip()

            # Create the folder
            folder_path = os.path.join(main_folder, folder_name)
            os.makedirs(folder_path, exist_ok=True)
            print(f"Folder '{folder_name}' created at '{folder_path}'.")

if __name__ == "__main__":
    # Specify the name of the text file containing topics
    topics_file_name = "topics.txt"
    
    # Specify the name of the main folder
    main_folder = "Tailwind-CSS"

    # Get the full path to the text file
    script_dir = os.path.dirname(os.path.realpath(__file__))
    topics_file_path = os.path.join(script_dir, topics_file_name)

    # Call the function to create folders
    create_folders_from_file(topics_file_path, main_folder)
