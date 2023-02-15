'''
Due the outstanding performance of the Customer Service Represetatives (CSRs) in the marketing department, management
has decided to reward them with a 10% increase in their salary. To evaluate the impact on the budget, you have been
asked to run a report on the employee file and display the results of BEFORE AND AFTER the salary increase.

You will create a dictionary that has the full employee name as the key and ONLY their new salary as the value.

Iternate through the dictionary to print out their name and thier new salary (as in image)
'''

import csv

#open the file
csvFile = open("employee_data.csv","r")
  



#create an empty dictionary

updatedSalaryDict = {}
  


#use a loop to iterate through the csv file
reader = csv.DictReader(csvFile)
for x in reader:
    employees = [x for x in reader] #read in info for employee list

#print before
print("===BEFORE===")
for employee in employees:
    print(print ("Name: " + str(employee['First Name'] +" " + employee['Last Name']) + "\nSalary: $" + str(round(float(employee['Salary']), 2)) + "\n"))


    #check if the employee fits the search criteria 
for employee in employees:
    if employee['Department'] == 'Marketing' and employee['Title'] == 'CSR':
        updatedSalaryDict[(float(employee['Salary'])*1.1)] = f"{employee['First Name']} {employee['Last Name']}"
    else:
        updatedSalaryDict[float(employee['Salary'])] = f"{employee['First Name']} {employee['Last Name']}"

print()
print('=========================================')
print()

#iternate through the dictionary and print out the key and value as per printout
print("===AFTER===") 
for key in updatedSalaryDict: 
    print ("Name: " + str(updatedSalaryDict[key]) + "\nSalary: $" + str(round(key, 2)) + "\n")