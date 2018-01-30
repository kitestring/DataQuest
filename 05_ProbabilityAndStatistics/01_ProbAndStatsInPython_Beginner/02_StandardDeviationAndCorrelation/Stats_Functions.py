import pandas as pd

def std_dev(data_list):
    data_series = pd.Series(data_list)
    series_mean = data_series.mean()
    variance_unsummed = [(i-series_mean) **2 for i in data_series]
    return (sum(variance_unsummed)/len(variance_unsummed)) ** 0.5

def within_percentage(sd_list, NoOfSDs):
    new_SD_list = [SD for SD in sd_list if SD <= NoOfSDs and SD >= -NoOfSDs]
    return len(new_SD_list) / len(sd_list)