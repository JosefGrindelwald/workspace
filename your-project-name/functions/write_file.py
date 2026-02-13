import os
from google.genai import types

def write_file(working_directory, file_path, content):
    try:
        # Absolute working directory
        working_dir_abs = os.path.abspath(working_directory)

        # Build and normalize target file path
        target_file = os.path.normpath(
            os.path.join(working_dir_abs, file_path)
        )

        # Ensure target path is inside working directory
        valid_target = (
            os.path.commonpath([working_dir_abs, target_file])
            == working_dir_abs
        )

        if not valid_target:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        # Prevent writing to a directory
        if os.path.isdir(target_file):
            return f'Error: Cannot write to "{file_path}" as it is a directory'

        # Ensure parent directories exist
        parent_dir = os.path.dirname(target_file)
        if parent_dir:
            os.makedirs(parent_dir, exist_ok=True)

        # Write content to file (overwrite)
        with open(target_file, "w", encoding="utf-8") as f:
            f.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f"Error: {str(e)}"

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes or overwrites a file with specified content relative to the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file relative to the working directory",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Content to write to the file",
            ),
        },
        required=["file_path", "content"],
    ),
)

