# Data  Munging
#     List all of the files in the current 
#     directory (the home directory), including 
#     the file names, permissions, formats, and sizes.
ls -l
# output:
total 6672                                                                      
#-rwxr-xr-x 1 dq dq 2051577 Nov  2 17:10 Hud_2005.csv                            
#-rwxr-xr-x 1 dq dq 1874334 Nov  2 17:10 Hud_2007.csv                            
#-rwxr-xr-x 1 dq dq 2902856 Nov  2 17:10 Hud_2013.csv


# Data Exploration
#     Use the head command to display the first 10 rows of each of the 3 CSV files.
head -n10 *.csv



# Filtering
#     Create the file combined_hud.csv and append the header row from one of the datasets.
#     Select all non-header rows from Hud_2005.csv and append to combined_hud.csv.
#     Display the first 10 rows in combined_hud.csv to verify your work.
head -n1 Hud_2005.csv > combined_hud.csv
wc -l Hud_2005.csv
# outputs:
# 46854 Hud_2005.csv
tail -46853 Hud_2005.csv >> combined_hud.csv
head combined_hud.csv



# Consolidatin datasets
#     Append the remaining datasets in the order of the years they describe.
#     Select all non-header rows from Hud_2007.csv and append to combined_hud.csv.
#     Select all non-header rows from Hud_2013.csv and append to combined_hud.csv.
#     Display the last 10 rows of combined_hud.csv and verify that they match the last 10 rows of Hud_2013.csv.
wc -l Hud_2007.csv
# output
# 42730 Hud_2007.csv
tail -42729 Hud_2007 >> combined_hud.csv
wc -l Hud_2013.csv
# output
# 64536 Hud_2013.csv
tail -64535 Hud_2013.csv >> combined_hud.csv
head combined_hud.csv
head Hud_2013.csv



#Counting
#     Count and display the number of lines in combined_hud.csv containing 1980-1989.
grep '1980-1989' combined_hud.csv | wc -l
# output:
# 19711
