output = open("sample_3.txt", "w")
for line_2 in sorted([line for line in open("sample_2.txt", "r").readlines()]):
    output.writelines(line_2)
output.flush()
