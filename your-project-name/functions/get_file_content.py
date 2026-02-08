import os

MAX_CHARS = 10000


def get_file_content(working_directory, file_path):
    try:
        # Absolute working directory
        working_dir_abs = os.path.abspath(working_directory)

        # Construct target file path safely
        target_file = os.path.normpath(
            os.path.join(working_dir_abs, file_path)
        )

        # Validate path is inside working directory
        valid_target = (
            os.path.commonpath([working_dir_abs, target_file])
            == working_dir_abs
        )

        if not valid_target:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        # Validate file exists and is a regular file
        if not os.path.isfile(target_file):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        # Read file with truncation protection
        with open(target_file, "r", encoding="utf-8") as f:
            content = f.read(MAX_CHARS)

            # Check if file was truncated
            if f.read(1):
                content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'

        return content

    except Exception as e:
        return f"Error: {str(e)}"
