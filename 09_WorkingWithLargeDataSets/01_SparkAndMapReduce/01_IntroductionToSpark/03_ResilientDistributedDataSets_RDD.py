from pyspark import SparkContext
sc =SparkContext()

raw_data = sc.textFile("daily_show.tsv")
raw_data.take(5)

