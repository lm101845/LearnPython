"""
演示将RDD输出到文件中
"""

from pyspark import SparkConf, SparkContext
import os
import json
os.environ['PYSPARK_PYTHON'] = 'D:/dev/python/python310/python.exe'
os.environ['HADOOP_HOME'] = "D:/dev/hadoop-3.0.0"
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")

sc = SparkContext(conf=conf)

# 准备RDD1
rdd1 = sc.parallelize([1, 2, 3, 4, 5], numSlices=1)

# 准备RDD2
rdd2 = sc.parallelize([("Hello", 3), ("Spark", 5), ("Hi", 7)], 1)

# 准备RDD3
rdd3 = sc.parallelize([[1, 3, 5], [6, 7, 9], [11, 13, 11]], 1)

# 输出到文件中
rdd1.saveAsTextFile("D:/output1")
rdd2.saveAsTextFile("D:/output2")
rdd3.saveAsTextFile("D:/output3")
