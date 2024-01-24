open_file = open("comments.txt", "r")
read_file = open_file.read().split('\n')
print(read_file)