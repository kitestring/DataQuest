import pandas as pd

data = pd.read_csv("data/CRDC2013_14.csv", encoding="Latin-1")

# Determines how many schools are of a given type
school_type_cols = ['JJ', 'SCH_STATUS_MAGNET']
print(school_type_cols[0],"= Juvenile justice facility, or youth prison")
print(data[school_type_cols[0]].value_counts())
print('\n' + school_type_cols[1], "= magnet school, an advanced school for students who achieve high score")
print(data[school_type_cols[1]].value_counts())

print('\n******\n')
gender_cols = ['TOT_ENR_M', 'TOT_ENR_F']
print(gender_cols[0], "= Total males enrolled")
print(gender_cols[1], "= Total females enrolled")

print('\nPiviot Table counting # of males and females enrolled for schools thare are and are not Juvenile justice facilities')
JJ_summary = pd.pivot_table(data, values=gender_cols, index=school_type_cols[0], aggfunc="sum")
print(JJ_summary)
JJ_m_f_ratio = JJ_summary['TOT_ENR_M']['YES'] / JJ_summary['TOT_ENR_F']['YES']

SCH_STATUS_MAGNET_summary = pd.pivot_table(data, values=gender_cols, index=school_type_cols[1], aggfunc="sum")
print('\nPiviot Table counting # of males and females enrolled for schools thare are and are not Magnet Schools')
print(SCH_STATUS_MAGNET_summary)
SCH_STATUS_MAGNET_m_f_ratio = SCH_STATUS_MAGNET_summary['TOT_ENR_M']['YES'] / SCH_STATUS_MAGNET_summary['TOT_ENR_F']['YES']

print('''
***Data Discusstion***
Maginet schools (MS) have a smaller ratio of males to females  
as compared to Juvenile justice facility, or youth prison (JJ)
\t- MS m/f ratio = %f
\t- JJ m/f ratio = %f''' % (JJ_m_f_ratio, SCH_STATUS_MAGNET_m_f_ratio))