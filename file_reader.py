def file_to_list(file):
    with open(file, "r") as text_wrapper:
        return (line.replace("\n", "") for line in text_wrapper)
