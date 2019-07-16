with open('E:\\swaraj\\python\\RTE_TC_0001.arxml', 'r') as file1:
    with open('C:\\Users\\swaraj_somala\\Documents\\23_05\\configuration_expectedop\\configurations_2\\RTE_TC_0001.arxml', 'r') as file2:
        same = set(file1).intersection(file2)

same.discard('\n')
print(same)
