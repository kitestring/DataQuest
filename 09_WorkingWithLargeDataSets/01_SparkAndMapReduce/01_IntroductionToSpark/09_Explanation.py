from pyspark import SparkContext
sc =SparkContext()

raw_data = sc.textFile("daily_show.tsv")

daily_show = raw_data.map(lambda line: line.split('\t'))
daily_show.take(5)

tally = daily_show.map(lambda x: (x[0], 1)).reduceByKey(lambda x,y: x+y)

tally.take(tally.count())

print(tally)