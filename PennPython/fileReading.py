def main():
    #filename
    #r means read mode
    f = open("lbd.txt", "r")
    lst_of_lines = f.readLines()
    # print(lst_of_lines[0].count(" ") + 1)

    #reading with a loop
    #for var in f:
        #print (var)

    #there is also .read()
    #x = f.read()
    #print (x)

    f.close()

    #overwrites stuff from the start
    fw = open('lbd.txt', "w") # W = write mode
    fw.write("hello")
    fw.close()

    #append mode
    fa = open("lbd.txt", "a") #A = append mode
    fa.write("founded Upenn (well kinda)") # goes to the end of whatever line is there
    fa.close()

main()
