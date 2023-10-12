def check_substring(main_string, substring):
    if substring in main_string:
        return True
    else:
        return False

# Example Usage
main_string = "Hello, this is an example string."
substring = "example"

if check_substring(main_string, substring):
    print(f"The substring '{substring}' was found in the main string.")
else:
    print(f"The substring '{substring}' was not found in the main string.")
