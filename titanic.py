import pandas as pd    
import openpyxl

### Read CSV file
read_file = pd.read_csv (r'titanic.csv')

### Getting all males formated as excel sheet 
new_file1 = read_file[read_file['Sex']=='male']
new_file1 = new_file1.sort_values(by=['Name','Age'])
print ("All Males : \n",new_file1)
with pd.ExcelWriter("Males.xlsx") as writer:
    new_file1.to_excel(writer)

### Getting all females
new_file2 = read_file[read_file['Sex']=='female']
new_file2 = new_file2.sort_values(by=['Name','Age'])
print("All Females : \n",new_file2)
with pd.ExcelWriter("Females.xlsx") as writer:
    new_file2.to_excel(writer)
	
### Getting all Survivors
new_file3 = read_file[read_file['Survived']==1]
new_file3 = new_file3.sort_values(by=['Name','Age'])
print("All Survivors : \n",new_file3)
with pd.ExcelWriter("Survivors.xlsx") as writer:
    new_file3.to_excel(writer)
	
### Getting all Dead Childs
new_file4 = read_file[read_file['Survived']==0]
new_file5 = new_file4[new_file4['Age']<=17]
new_file5 = new_file5.sort_values(by=['Name','Age'])
print("All Lost Childern : \n",new_file5)
with pd.ExcelWriter("LostChild.xlsx") as writer:
    new_file5.to_excel(writer)
	
### Getting the Persentage of Survivors
X = read_file[read_file['Survived']==1]	   ### read only survivors from column Survived
X = X.shape[0]                             ### get only rows counts
print("\n Survivors : ",X)
Y = read_file['Survived']       		   ### read all from column Survived
Y = Y.shape[0]							   ### get only rows counts
print("\n All Titanic Passengers : ",Y)
Z = ( X / Y ) * 100
print ("\n Survivors Persentage : %.2f"%Z,"%")
