from validate import validate_all

if __name__ == "__main__":
    error_list = validate_all()
    if error_list:
        exit(1)