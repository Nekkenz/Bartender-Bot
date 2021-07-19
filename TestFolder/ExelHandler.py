import pandas as pd
xls = pd.ExcelFile('E:\Python_Projects\Bartender\Bartender\Drinks\DrinkList.xlsx')

# Iterate through Mixers and get pump numbers
Pumps = pd.read_excel(xls, 'Pumps')
df2 = pd.DataFrame(Pumps)

print(df2)
dfcleaned = df2.fillna(0)
print(dfcleaned)
activeMixers = []
for i in dfcleaned.iteritems():
	name = str(i[0])
	if  name != 'Mixers':
		if i[1][0] == 0.0:
			dfcleaned = dfcleaned.drop(name, axis=1)
		else:
			activeMixers.append([i[0], i[1][0]])
			print("+++++", i[1][0], i[0])


print("*******", activeMixers)

# Iterate through list of drinks and mixers and remove 
Drinks = pd.read_excel(xls, 'Drinks')
df1 = pd.DataFrame(Drinks)
dfcleaned2 = df1.fillna(0)
allMixers = []
for i in dfcleaned2.iteritems():
	name = str(i[0])
	if  name != 'Drinks':
		allMixers.append(i[0])
	print("[[[[[[[[[", i[0][1])

dropList = []
for i in activeMixers:
	for j in allMixers:
		if i == j:
			break
		else:
			dropList.append(j)

# Iterate and delete rows with invalid mixer
dfcleaned2 = dfcleaned2[dfcleaned2.Water == 0]
# Iterate and delete column with invalid mixer
dfcleaned2 = dfcleaned2.drop('Water', axis=1)
# Find row where water is greater than 0.0
# dfcleaned.loc[dfcleaned2['Water'] > 0.0])
iter = 0
for i in dfcleaned2.iteritems():
	name = str(i[0])
	if  name != 'Drinks':
		if i[1][0] != 0:
			print("+++++", i[1][0], i[0])
			iter += 1
print(dfcleaned2)

	
#for i in df2:
#	print("-----\n", i)
#print(df.head(0))

#for i in df2.itertuples():
#	if i[2] != 0.0:
#		print("-----\n", i[1], i[2])
