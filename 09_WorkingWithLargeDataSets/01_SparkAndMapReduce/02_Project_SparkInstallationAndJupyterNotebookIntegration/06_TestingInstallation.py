# Find path to PySpark.
import findspark
findspark.init()

# Import PySpark and initialize SparkContext object.
import pyspark
sc = pyspark.SparkContext()

# Read `recent-grads.csv` in to an RDD.
f = sc.textFile('recent-grads.csv')
data = f.map(lambda line: line.split('\n'))
print(data.take(10))