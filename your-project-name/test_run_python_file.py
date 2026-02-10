from functions.run_python_file import run_python_file


if __name__ == "__main__":

    print("Run main.py (no args):")
    print(run_python_file("calculator", "main.py"))

    print("\nRun main.py with calculation:")
    print(run_python_file("calculator", "main.py", ["3 + 5"]))

    print("\nRun tests.py:")
    print(run_python_file("calculator", "tests.py"))

    print("\nAttempt path escape:")
    print(run_python_file("calculator", "../main.py"))

    print("\nNonexistent file:")
    print(run_python_file("calculator", "nonexistent.py"))

    print("\nNon-python file:")
    print(run_python_file("calculator", "lorem.txt"))
