def main(string: str, start: int, length: int):
    end = start + length
    new_string = ""
    for i in range(start, end):
        new_string += string[i]
    return new_string
