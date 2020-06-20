import scipy.stats

print("What do you wish to calculate?")
print("1. \tPath total, Variance, SD")
print("2. \tZ score with specified time\n")
choice = input("1 or 2?\t\t")
finished = False
while finished == False:
    if choice == "1":
        n_activity = int(input("how many activities? "))

        dict_activity = {}
        path_total=0
        variance_path=0
        path_stack = []

        def input_analyzer():
            global input_stack
            to_string = ""
            tm_string = ""
            tp_string = ""
            input_stack = []
            index_stack=[]
            first_comma = True
            a= list(input\
                    ("write value of to, tm, tp, in order and separated by dash(-): "))
            for j in a:
                if j == "-" and first_comma == True:
                    to_list = a[:a.index(j):]
                    index_stack.append(a.index(j))
                    for k in range(len(to_list)):
                        to_string += to_list[k]
                    input_stack.append(to_string)
                    a.remove(j)
                    first_comma = False
                elif j == "-" and first_comma == False:
                    tm_list = a[index_stack[0]:a.index(j):]
                    for k in range(len(tm_list)):
                        tm_string += tm_list[k]
                    input_stack.append(tm_string)
                    tp_list = a[a.index(j)+1::]
                    for l in range(len(tp_list)):
                        tp_string += tp_list[l]
                    input_stack.append(tp_string)
            if len(input_stack) == 3:
                print(input_stack)
            elif len(input_stack) != 3:
                print("please check the input is in correct order and form: ")
                input_analyzer()
            
        for i in range(1,n_activity+1):
            input_analyzer()
            for j in range(3):
                if input_stack[j].isdigit(): 
                    if float(input_stack[j]) == int(float(input_stack[j])):
                        input_stack[j] = int(float(input_stack[j]))
                    else:
                        input_stack[j] = float(input_stack[j])
                else:
                    print("please type in numbers: ")
                    input_analyzer()
            dict_activity["to"+str(i)] = input_stack[0]
            dict_activity["tm"+str(i)] = input_stack[1]
            dict_activity["tp"+str(i)] = input_stack[2]
                
            path_stack.append(str(input_stack[0])+"-"+\
                              str(input_stack[1])+"-"+\
                              str(input_stack[2]))

        for i in range(1, n_activity+1):
            sum_activity=(dict_activity["to"+str(i)] + dict_activity["tm"+str(i)]*4 + \
                          dict_activity["tp"+str(i)])/6
            path_total += sum_activity

        for i in range (1, n_activity+1):
            variance_activity = ((dict_activity["tp"+str(i)] -\
                                  dict_activity["to"+str(i)])**2)/36
            variance_path += variance_activity

        SD_path = (variance_path)**(1/2)
        print("\nActivity path:")
        for i in range (n_activity):
            print(str(path_stack[i])+"\t\t", end="")
        print("\n\npath_total (path mean):", path_total)
        print("variance:", variance_path)
        print("SD:", SD_path)

        proceed = input("Do you wish to proceed and get Z score of specified time? (y/n): ")
        q = True
        while q == True:
            if proceed == "y" or proceed =="Y":
                
                specific_event = float(input("What is specified time? "))
                Z = (specific_event - path_total)/SD_path
                print("\nZ score:", Z)
                prob=scipy.stats.norm(0,1).cdf(Z)
                print("probability of project taking "+ str(specific_event) + " is " + str(prob))
                q = False
                finished = True
            elif proceed == 'n' or proceed =="N":
                q =  False
                finished = True
            else:
                proceed = input("please check the input again (y/n): ")
        

    elif choice == "2":
        specific_event = float(input("What is specified time? "))
        path_total = float(input("What is the path total (path mean)? "))
        SD_path = float(input("What is the variance? "))**(1/2)
        Z = (specific_event - path_total)/SD_path
        print("Z score:", Z)
        prob=scipy.stats.norm(0,1).cdf(Z)
        print("probability of project taking less than "+ str(specific_event) + " is " + str(prob))
        finished = True

    else:
        choice = input("please check the input again (1/2): ")
        

