import sys
import os
import pdb
#pdb.set_trace() #for debugging
if len(sys.argv) ==  1:
    print("Error. Not sufficient arguments")
    sys.exit(1)

if len(sys.argv) >= 1:
    file_name = "task.txt"
    option = sys.argv[1]
    try:
        if option == '-a':
            with open(file_name,'a') as f:
                f.write(sys.argv[2]+"\n")
            print("Added to the file\n")
        elif option == '-v':
            with open(file_name,'r') as f:
                for line in f:
                    print(line)
            print("File END!!")
        elif option == '-d':
            pass
        else:
            print("invalid arguments")

    except Exception as e:
        print("Error")
    #file_name = sys.argv[1]
    #if not os.path.isfile(file_name):
    #    with open(file_name,'w') as f:
    #        f.write("Written file")
        
