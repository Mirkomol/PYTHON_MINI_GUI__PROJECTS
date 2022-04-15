from prettytable import PrettyTable

myTable= PrettyTable(["Student_Name", "Class", "Section","Percentage"])

myTable.add_row(["Leonard","X", "B","75.5 %"])
myTable.add_row(["Johnny","Q", "B","75.5 %"])
myTable.add_row(["Mirkamol","J", "B","75.5 %"])
myTable.add_row(["Joe","X", "B","75.5 %"])
myTable.add_row(["DiBar","X", "B","75.5 %"])

print(myTable)