the_file = None
the_tries = 5
while the_tries > 0:
    try:
        print("Enter the file Absolute path")
        print(f"you have {the_tries} left ")
        print(r"Example >-D:\videos")
        the_file_and_path = input("Enter the file name ").strip()
        the_file = open(the_file_and_path, 'r')
        print(the_file.read())
        break
    except FileNotFoundError:
            print("file not found")
            the_tries -= 1
    except:
        print("Error happen")
    finally:
        if the_file is not None:
            the_file.close()
            print("file closed")
else:
    print("your tries is finished")
