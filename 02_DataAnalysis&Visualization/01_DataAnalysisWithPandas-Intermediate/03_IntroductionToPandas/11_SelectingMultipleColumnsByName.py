import pandas

food_info = pandas.read_csv('food_info.csv')

food_info_columns = ['Selenium_(mcg)', 'Thiamin_(mg)']

selenium_thiamin = food_info[food_info_columns]

print(selenium_thiamin)