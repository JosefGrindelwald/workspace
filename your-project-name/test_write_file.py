from functions.write_file import write_file


if __name__ == "__main__":

    print("Overwrite existing file:")
    print(
        write_file(
            "calculator",
            "lorem.txt",
            "wait, this isn't lorem ipsum"
        )
    )

    print("\nWrite new file in subdirectory:")
    print(
        write_file(
            "calculator",
            "pkg/morelorem.txt",
            "lorem ipsum dolor sit amet"
        )
    )

    print("\nAttempt to write outside working directory:")
    print(
        write_file(
            "calculator",
            "/tmp/temp.txt",
            "this should not be allowed"
        )
    )
