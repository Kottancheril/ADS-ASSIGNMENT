import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



def plot_import_per(x):
    
    ''' 
    This function reads an Excel file containing agricultural import percentage data for different countries,
    plots a line chart for the import percentage of each country, and displays the chart 
    '''
   
    # Line plot
    plt.figure(figsize = (15, 10))
    
    # Plot the import percentage for different countries
    plt.plot(import_per["Time"], import_per["Australia"], label = "Australia")
    plt.plot(import_per["Time"], import_per["China"], label = "China")
    plt.plot(import_per["Time"], import_per["India"], label = "India")
    plt.plot(import_per["Time"], import_per["New Zealand"], label = "New Zealand")
    plt.plot(import_per["Time"], import_per["USA"], label = "USA")
    plt.plot(import_per["Time"], import_per["UAE"], label = "UAE")
    plt.plot(import_per["Time"], import_per["UK"], label = "UK")

    # Set labels and show the legend
    plt.xlabel("Year", fontsize = 12)
    plt.ylabel("Import Percentage", fontsize = 12)
    plt.title("Agricultural Raw Material Import Percentage")
    plt.legend()
    plt.savefig('line_plot.png')
    plt.show()
    
    return

# Read file into dataframe 
import_per = pd.read_excel(r"C:\Users\liyak\Downloads\AGRICULTURE_IMPORT_%.xlsx")
 
 
plot_import_per(import_per)


def plot_employee_distribution(data):
    
    '''
    This function takes a pandas dataframe containing employee data, groups the data by education field,
    calculates the sum of employee count for each group, and plots a pie chart to display the distribution
    of employees in different education fields
    '''
    
    # Group the data by 'EducationField' column
    mode = data.groupby('EducationField', as_index = True)

    # Calculate the sum of 'EmployeeCount' for each group
    count = mode['EmployeeCount'].agg(np.sum)

    # Plotting a pie chart for the distribution of employees in different fields
    labels = ['Life Sciences', 'Other', 'Medical', 'Marketing', 'Technical Degree', 'Human Resources']
    plt.pie(count, labels=labels, autopct = '%.2f%%')
    plt.title("Distribution of Employees by Education Field")
    plt.savefig('pie_chart.png')
    plt.show()
    
    return


Attrition = pd.read_csv(r"C:\Users\liyak\Downloads\HR-Employee-Attrition.csv")

plot_employee_distribution(Attrition)


   
def plot_working_years(data):
    
    ''' 
    This function takes a pandas dataframe containing employee data,
    plots a horizontal bar chart to display 'YearsAtCompany' vs 'Age'
    '''
    
    # Plotting a horizontal bar chart for 'YearsAtCompany' vs 'Age'
    plt.figure(figsize = (10,7))
    plt.barh(data['Age'], data['YearsAtCompany'], color = 'slateblue')
    plt.xlabel("Years at Company", fontsize = 12)
    plt.ylabel("Age", fontsize = 12)
    plt.title("Years at Company vs Age")
    plt.savefig('bar_plot.png')
    plt.show()
    
    return

plot_working_years(Attrition)