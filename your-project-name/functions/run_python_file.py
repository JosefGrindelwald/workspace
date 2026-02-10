import os
import subprocess


def run_python_file(working_directory, file_path, args=None):
    try:
        # Absolute working directory
        working_dir_abs = os.path.abspath(working_directory)

        # Build normalized target path
        absolute_file_path = os.path.normpath(
            os.path.join(working_dir_abs, file_path)
        )

        # Validate path is inside working directory
        valid_target = (
            os.path.commonpath([working_dir_abs, absolute_file_path])
            == working_dir_abs
        )

        if not valid_target:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        # Validate file exists and is regular file
        if not os.path.isfile(absolute_file_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'

        # Validate file extension
        if not absolute_file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'

        # Build command
        command = ["python", absolute_file_path]

        if args:
            command.extend(args)

        # Run subprocess
        result = subprocess.run(
            command,
            cwd=working_dir_abs,
            capture_output=True,
            text=True,
            timeout=30
        )

        output_parts = []

        # Non-zero exit code
        if result.returncode != 0:
            output_parts.append(f"Process exited with code {result.returncode}")

        # STDOUT
        if result.stdout:
            output_parts.append(f"STDOUT:\n{result.stdout}")

        # STDERR
        if result.stderr:
            output_parts.append(f"STDERR:\n{result.stderr}")

        # No output at all
        if not result.stdout and not result.stderr:
            output_parts.append("No output produced")

        return "\n".join(output_parts)

    except Exception as e:
        return f"Error: executing Python file: {e}"
