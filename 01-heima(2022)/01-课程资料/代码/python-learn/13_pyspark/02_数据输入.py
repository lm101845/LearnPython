"""
演示通过PySpark代码加载数据，即数据输入
"""
from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

# # 通过parallelize方法将Python对象加载到Spark内，成为RDD对象
# rdd1 = sc.parallelize([1, 2, 3, 4, 5])
# rdd2 = sc.parallelize((1, 2, 3, 4, 5))
# rdd3 = sc.parallelize("abcdefg")
# rdd4 = sc.parallelize({1, 2, 3, 4, 5})
# rdd5 = sc.parallelize({"key1": "value1", "key2": "value2"})
#
# # 如果要查看RDD里面有什么内容，需要用collect()方法
# print(rdd1.collect())
# print(rdd2.collect())
# print(rdd3.collect())
# print(rdd4.collect())
# print(rdd5.collect())

# 用过textFile方法，读取文件数据加载到Spark内，成为RDD对象
rdd = sc.textFile("D:/hello.txt")
print(rdd.collect())
rdd.map()
sc.stop()
