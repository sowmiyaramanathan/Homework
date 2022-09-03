months_per_year = 12    #initializing total months per year to get monthly sales and calculate monthly salary
salary_per_month = []   #initializing a list to store salary for each month
max_salary = 25000      #initializing maximum salary the salesman can earn

for sale in range(months_per_year):     #using for loop 12 times(for all months per year) to get number of sales each month and calculate respective salaries for the same month
    base_salary = 10000               #initializing base salary inside for as for each month the base salary is the same
    print("Enter the total sale for month", sale+1)     #printing to indicate the user to enter input
    phones_sold = int(input())                          #reading total number of phones sold in each month
    for sold in range(phones_sold):                     #using for loop for the number of phones sold
        base_salary += 1000                             #adding 1000 for each phone sold to the base salary
    if(phones_sold > 10):                                  #using if to check if the salesman sold more than 10 phones
        base_salary += 1500                             #adding 1500 to the base salary for each phone if sold above 10
    elif(phones_sold > 5):                                 #using elif to check if th e salesman sold more then 5 phones
        base_salary += 500                              #adding 500 to the base salary for each phone if sold above 5
    monthly_salary = base_salary                        #initializing monthly salary as base salary
    if(monthly_salary > max_salary):             #using if to check whether monthly salary is higher than maximum salary
        monthly_salary = max_salary              #assigning maximum salary as monthly salary
        salary_per_month.append(monthly_salary)      #adding maximum salary to the monthly salary list
    else:                              #using else to indicate that the monthly salary is not higher than maximum salary
        salary_per_month.append(monthly_salary)  #adding monthly salary to the monthly salary list

for salary in range(months_per_year):    #using for loop 12 times(for all months per year) to print the monthly salaries
    print("Salary for month ", salary+1, " : Rs. ", salary_per_month[salary])   #printing monthly salary for each month

sum_of_monthly_salaries = sum(salary_per_month)                          #calculating sum of monthly salaries
average_of_monthly_per_year = round(sum_of_monthly_salaries / months_per_year)  #calculating average of monthly salary per year
print("Average salary per year : Rs. ", average_of_monthly_per_year)     #printing average of monthly salary per year



#test case 1 with positive inputs
#Enter the total sale for month 1
#2
#Enter the total sale for month 2
#10
#Enter the total sale for month 3
#5
#Enter the total sale for month 4
#3
#Enter the total sale for month 5
#12
#Enter the total sale for month 6
#7
#Enter the total sale for month 7
#0
#Enter the total sale for month 8
#0
#Enter the total sale for month 9
#3
#Enter the total sale for month 10
#25
#Enter the total sale for month 11
#13
#Enter the total sale for month 12
#6
#Salary for month  1  : Rs.  12000
#Salary for month  2  : Rs.  20500
#Salary for month  3  : Rs.  15000
#Salary for month  4  : Rs.  13000
#Salary for month  5  : Rs.  23500
#Salary for month  6  : Rs.  17500
#Salary for month  7  : Rs.  10000
#Salary for month  8  : Rs.  10000
#Salary for month  9  : Rs.  13000
#Salary for month  10  : Rs.  25000
#Salary for month  11  : Rs.  24500
#Salary for month  12  : Rs.  16500
#Average salary per year : Rs.  16708

#test case 2 with negative inputs
#Enter the total sale for month 1
#0
#Enter the total sale for month 2
#-9
#Enter the total sale for month 3
#0
#Enter the total sale for month 4
#5
#Enter the total sale for month 5
#0
#Enter the total sale for month 6
#0
#Enter the total sale for month 7
#-98
#Enter the total sale for month 8
#2
#Enter the total sale for month 9
#2
#Enter the total sale for month 10
#0
#Enter the total sale for month 11
#0
#Enter the total sale for month 12
#0
#Salary for month  1  : Rs.  10000
#Salary for month  2  : Rs.  10000
#Salary for month  3  : Rs.  10000
#Salary for month  4  : Rs.  15000
#Salary for month  5  : Rs.  10000
#Salary for month  6  : Rs.  10000
#Salary for month  7  : Rs.  10000
#Salary for month  8  : Rs.  12000
#Salary for month  9  : Rs.  12000
#Salary for month  10  : Rs.  10000
#Salary for month  11  : Rs.  10000
#Salary for month  12  : Rs.  10000
#Average salary per year : Rs.  10750
