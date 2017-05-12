from pyspark import SparkContext
import itertools

sc = SparkContext("spark://spark-master:7077", "PopularItems")

data = sc.textFile("/app/access.log", 2)     # each worker loads a piece of the data file

pairs = data.map(lambda line: line.split("\t"))   # tell each worker to split each line of it's partition
pages = pairs.map(lambda pair: (pair[0], pair[1]))      # re-layout the data to ignore the user id
pairs_by_user = pages.reduceByKey()
reduced_pairs = combinations((pairs_by_user), 2)     # shuffle the data so that each key is only on one worker
                                                  # and then reduce all the values by adding them together

output = reduced_pairs.collect()                          # bring the data back to the master node so we can print it out
for user_id, items in output:
    print ("page_id %s count %d" % (user_id, items))
print ("Popular items done")

sc.stop()
