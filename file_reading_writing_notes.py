

#file object
f = open("samplefile.txt","w")
f.writelines(["line1","line2","line3","line4"])
f.flush()
f.write("\n i will use pointer")
f.flush()
f.tell()
f.seek(0)
f.tell()
f.writable() #i tell if you can write using this object or not 

f.close()
f.closed #will tell if the file is closed or not 

###### 

with open("samplefile.txt","r") as f:
    while True:
        line = f.readline()
        if line:
            print(line)
        else:
            break
    print(f.closed)
f.closed


#different modes 


# r = reading only. The file pointer is placed at the beginning of the file. This is the default mode.
# rb = reading only in binary format. The file pointer is placed at the beginning of the file. This is the default mode.
# w = writing only. Overwrites the file if the file exists. If the file does not exist, creates a new file for writing.
# wb = writing only in binary format. Overwrites the file if the file exists. If the file does not exist, creates a new file for writing.
# a = appending. The file pointer is at the end of the file if the file exists. That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.
# ab = appending in binary format. The file pointer is at the end of the file if the file exists. That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.




#############################3 pickeling ###############33
class sample_class:
    def __str__(self):
        return "i am sample class "
obj = sample_class()
import pickle
### serialisation 
with open("pickle_file.pkl","wb") as f:
    pickle.dump(obj,f)

############# de serialisation 
with open("pickle_file.pkl","rb") as f:
    fucnt = pickle.load(f)
    print(fucnt)
