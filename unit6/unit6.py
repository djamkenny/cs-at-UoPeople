#Consider that you are working as Data Analyst in an organization. The HR department needs you to carry out following operation on existing list of 10 employees name (you can assume 10 names in a list here). 

#Split the list into two sub-list namely subList1 and subList2, each containing 5 names.
list_employee = [
        'Derrick',
        'Enoch',
        'Maureen',
        'Edwin',
        'Sedem',
        'Jessica',
        'Bridget',
        'Joy',
        'John',
        'Doe'
        ]
#split the list into two
subList1 = list_employee[:5]
subList2 = list_employee[5:]
    

#A new employee (assume the name “Kriti Brown”) joins, and you must add that name in subList2.
subList2.append('Kriti Brown')

#Remove the second employee's name from subList1. 
subList1.pop(1)

#Merge both the lists.
merged_list = subList1 + subList2

#list of the salary foe employees
salary_list = [50000, 60000, 55000, 65000, 70000, 55000, 60000, 75000, 80000, 60000]

#a rise of 4% to every employee
salary_lists = [salary * 1.04 for salary in salary_list]

#Sort the SalaryList and show top 3 salaries.
salary_lists.sort(reverse=True)

#show the top 3 salaries
top_3_salaries = salary_list[:3]


#print the results
print("subList1:", subList1)
print("subList2:", subList2)
print("Merged List:", merged_list)
print("Updated Salary List:", salary_list)
print("Top 3 Salaries:", top_3_salaries)




#Explanation:

#We start with a list of 10 employees (employee_list).

#We split this list into two sub-lists: subList1 (the first 5 employees) and subList2 (the last 5 employees).

#A new employee, "Kriti Brown," joins the organization and is added to subList2.

#We remove the second employee, "Jane," from subList1.

#We merge both sub-lists into a single list, merged_list.

#We have a list of salaries (salary_list) for the employees.

#We give each employee a 4% raise, resulting in updated_salary_list.

#The salaries are sorted in descending order to find the top 3 salaries.

#The code then prints the results: subList1, subList2, the merged list, updated salaries, and the top 3 salaries.
