from pyspark import SparkContext
sc =SparkContext()

raw_data = sc.textFile("daily_show.tsv")

daily_show = raw_data.map(lambda line: line.split('\t'))

def filter_year(line):
    if line[0] == 'YEAR':
        return False
    else:
        return True

filtered_daily_show = daily_show.filter(lambda line: filter_year(line))

filtered_daily_show.filter(lambda line: line[1] != '') \
                   .map(lambda line: (line[1].lower(), 1)) \
                   .reduceByKey(lambda x,y: x+y) \
                   .take(5)