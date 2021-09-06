import pandas as pd    
import openpyxl

### Read CSV file
read_file = pd.read_csv (r'titanic.csv')

### Getting all males formated as excel sheet 
new_file1 = read_file[read_file['Sex']=='male']
new_file1 = new_file1.sort_values(by=['Name','Age'])
with pd.ExcelWriter("Males.xlsx") as writer:
    new_file1.to_excel(writer)

### Getting all females
new_file2 = read_file[read_file['Sex']=='female']
new_file2 = new_file2.sort_values(by=['Name','Age'])
with pd.ExcelWriter("Females.xlsx") as writer:
    new_file2.to_excel(writer)
	
### Getting all Survivors
new_file3 = read_file[read_file['Survived']==1]
new_file3 = new_file3.sort_values(by=['Name','Age'])
with pd.ExcelWriter("Survivors.xlsx") as writer:
    new_file3.to_excel(writer)
	
### Getting all Dead Childs
new_file4 = read_file[read_file['Survived']==0]
new_file5 = new_file4[new_file4['Age']<=17]
new_file5 = new_file5.sort_values(by=['Name','Age'])
with pd.ExcelWriter("LostChild.xlsx") as writer:
    new_file5.to_excel(writer)