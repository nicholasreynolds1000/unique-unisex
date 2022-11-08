import pandas as pd

#Reading the text from one sample year into a DataFrame
df = pd.read_csv('names/yob1940.txt', sep=',', header=None, dtype='object')
#Defining the total number of unique names issued to both sexes allowing for each unique name to appear once for each sex
total_names = (len(df[0]))
#Defining the total number of unique names if duplicates are removed
repeat_names = (total_names-len(df[0].drop_duplicates()))
#Calculating unique unisex name percentage (UNP) by dividing the number of unique names that appear in both sexes by the total number of unique names excluding repeats for each sex and multiplying by 100
ratio = repeat_names / len(df[0].drop_duplicates()) * 100
#Rounding the output to one decimal place
output = round(ratio, 1)
#Printing an f string with the UNP for the year
print(f'In 1940 about {output} percent of unique US baby names were applied to both sexes.')

df = pd.read_csv('names/yob1950.txt', sep=',', header=None, dtype='object')
total_names = (len(df[0]))
repeat_names = (total_names-len(df[0].drop_duplicates()))
ratio = repeat_names / len(df[0].drop_duplicates()) * 100
output = round(ratio, 1)
print(f'In 1950 about {output} percent of unique US baby names were applied to both sexes.')

df = pd.read_csv('names/yob1960.txt', sep=',', header=None, dtype='object')
total_names = (len(df[0]))
repeat_names = (total_names-len(df[0].drop_duplicates()))
ratio = repeat_names / len(df[0].drop_duplicates()) * 100
output = round(ratio, 1)
print(f'In 1960 about {output} percent of unique US baby names were applied to both sexes.')

df = pd.read_csv('names/yob1970.txt', sep=',', header=None, dtype='object')
total_names = (len(df[0]))
repeat_names = (total_names-len(df[0].drop_duplicates()))
ratio = repeat_names / len(df[0].drop_duplicates()) * 100
output = round(ratio, 1)
print(f'In 1970 about {output} percent of unique US baby names were applied to both sexes.')

df = pd.read_csv('names/yob1980.txt', sep=',', header=None, dtype='object')
total_names = (len(df[0]))
repeat_names = (total_names-len(df[0].drop_duplicates()))
ratio = repeat_names / len(df[0].drop_duplicates()) * 100
output = round(ratio, 1)
print(f'In 1980 about {output} percent of unique US baby names were applied to both sexes.')

df = pd.read_csv('names/yob1990.txt', sep=',', header=None, dtype='object')
total_names = (len(df[0]))
repeat_names = (total_names-len(df[0].drop_duplicates()))
ratio = repeat_names / len(df[0].drop_duplicates()) * 100
output = round(ratio, 1)
print(f'In 1990 about {output} percent of unique US baby names were applied to both sexes.')

df = pd.read_csv('names/yob2000.txt', sep=',', header=None, dtype='object')
total_names = (len(df[0]))
repeat_names = (total_names-len(df[0].drop_duplicates()))
ratio = repeat_names / len(df[0].drop_duplicates()) * 100
output = round(ratio, 1)
print(f'In 2000 about {output} percent of unique US baby names were applied to both sexes.')

df = pd.read_csv('names/yob2010.txt', sep=',', header=None, dtype='object')
total_names = (len(df[0]))
repeat_names = (total_names-len(df[0].drop_duplicates()))
ratio = repeat_names / len(df[0].drop_duplicates()) * 100
output = round(ratio, 1)
print(f'In 2010 about {output} percent of unique US baby names were applied to both sexes.')

df = pd.read_csv('names/yob2020.txt', sep=',', header=None, dtype='object')
total_names = (len(df[0]))
repeat_names = (total_names-len(df[0].drop_duplicates()))
ratio = repeat_names / len(df[0].drop_duplicates()) * 100
output = round(ratio, 1)
print(f'In 2020 about {output} percent of unique US baby names were applied to both sexes.')
