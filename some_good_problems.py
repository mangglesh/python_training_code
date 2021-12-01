sum([int(line) for line in open("sample.txt").readlines()])

sorted_list = [str(i)+"\n" for i in sorted([int(line) for line in open("sample.txt").readlines()])]
open("sample.txt","w").writelines(sorted_list)


