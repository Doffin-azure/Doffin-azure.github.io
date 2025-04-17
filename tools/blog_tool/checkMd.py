import os
import re


def replace_image_paths_in_md(file_path):
    """
    This function reads a markdown file, finds all instances of ![[xxx]]
    and replaces them with ![Image](..\\assets\\post_figure\\xxx)
    """
    # Define the regex pattern to match ![[xxx]]
    pattern = r"!\[\[(.*?)\]\]"

    # Open the file and read the content
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    # Replace all matches of the pattern
    # Use raw string (r'') for the path to avoid unicodeescape errors
    modified_content = re.sub(
        pattern, r"![Image](..\\assets\\post_figure\\\1)", content
    )

    # Save the modified content back to the file
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(modified_content)

    print(f"File '{file_path}' updated successfully!")


def update_all_md_files_in_directory(directory):
    """
    This function goes through all .md files in the given directory and updates image paths.
    """
    # Loop through all files in the directory
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                replace_image_paths_in_md(file_path)


if __name__ == "__main__":
    # Ask user to input the directory where markdown files are located
    markdown_directory = input(
        "Please enter the directory path for the markdown files: "
    )

    # Ensure the directory exists
    if os.path.isdir(markdown_directory):
        update_all_md_files_in_directory(markdown_directory)
    else:
        print(
            f"The directory '{markdown_directory}' does not exist. Please check the path and try again."
        )
