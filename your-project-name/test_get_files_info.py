from functions.get_files_info import get_files_info


if __name__ == "__main__":

    print("Result for current directory:")
    result = get_files_info("calculator", ".")
    print("  " + result.replace("\n", "\n  "))

    print("\nResult for 'pkg' directory:")
    result = get_files_info("calculator", "pkg")
    print("  " + result.replace("\n", "\n  "))

    print("\nResult for '/bin' directory:")
    result = get_files_info("calculator", "/bin")
    print("  " + result.replace("\n", "\n  "))

    print("\nResult for '../' directory:")
    result = get_files_info("calculator", "../")
    print("  " + result.replace("\n", "\n  "))
