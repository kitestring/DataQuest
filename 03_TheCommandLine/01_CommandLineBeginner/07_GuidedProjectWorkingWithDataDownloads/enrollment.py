import pandas as pd
import matplotlib.pyplot as plt


def getDemographicslst():
    prefix = ['SCH_ENR', 'SCH_HBREPORTED_DIS','SCH_DISCWODIS_EXPWOE','SCH_RET_G12']     
    races = ['HI','AM','AS','HP','BL','WH','TR']
    genders = ['M','F']
       
    Demographicslst = ['TOT_ENR_M', 'TOT_ENR_F']
    
    for per in prefix:
        for race in races:
            for gender in genders:
                Demographicslst.append('%s_%s_%s' % (per, race, gender) )
    return Demographicslst

data = pd.read_csv("data/CRDC2013_14.csv", encoding="Latin-1")

data['total_enrollment'] = data['TOT_ENR_M'] + data['TOT_ENR_F']


Demographicslst = getDemographicslst()
summedDemographics = data[Demographicslst].sum()

print(summedDemographics.iloc[0:14])
summedDemographics.iloc[0:14].plot.bar()
plt.show()

all_enrollment = data['total_enrollment'].sum()
print(all_enrollment)

DemographicsByPercentage = summedDemographics / all_enrollment
print(DemographicsByPercentage.iloc[0:14])
DemographicsByPercentage.iloc[0:14].plot.bar()
plt.show()