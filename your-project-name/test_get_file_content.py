from functions.get_file_content import get_file_content


if __name__ == "__main__":

    print("Testing lorem.txt truncation:")
    lorem_content = get_file_content("calculator", "lorem.txt")

    print(f"Length: {len(lorem_content)}")
    print("Ends with truncation message:",
          "truncated" in lorem_content)

    print("\nmain.py:")
    print(get_file_content("calculator", "main.py"))

    print("\npkg/calculator.py:")
    print(get_file_content("calculator", "pkg/calculator.py"))

    print("\n/bin/cat:")
    print(get_file_content("calculator", "/bin/cat"))

    print("\nNon-existent file:")
    print(get_file_content("calculator", "pkg/does_not_exist.py"))
