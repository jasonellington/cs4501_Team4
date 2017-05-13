from pyspark import SparkContext
from itertools import *
from functools import partial

sc = SparkContext("spark://spark-master:7077", "PopularItems")

data = sc.textFile("/app/access.log", 2)

distinct_data = data.distinct()

pairs = distinct_data.map(lambda line: line.split("\t"))
pairs_by_user = pairs.groupByKey()
reduced_pairs = pairs_by_user.flatMapValues(partial(combinations, r=2))

key_tup = reduced_pairs.groupBy(lambda tup: tup[1])

pages = key_tup.map(lambda pair: (pair[0], 1))
count = pages.reduceByKey(lambda x, y: int(x)+int(y))

output = count.collect()
print("reduced_pairs:")
for x, y in output:
    print("x: %s y: %s" % (x, y))

sc.stop()
