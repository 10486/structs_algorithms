def main(filename:str):
    with open(filename,'r') as f:
        for line in f.readlines():
            
            string, start, length = line.split()
            start = int(start)
            length = int(length)

            end = start + length
            new_string = ""
            for i in range(start, end):
                new_string += string[i]
            print(new_string)
