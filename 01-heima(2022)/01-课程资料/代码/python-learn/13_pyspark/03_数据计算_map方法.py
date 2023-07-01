"""
演示RDD的map成员方法的使用
"""
from pyspark import SparkConf, SparkContext
import os
os.environ['PYSPARK_PYTHON'] = "D:/dev/python/python310/python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

# 准备一个RDD
rdd = sc.parallelize([1, 2, 3, 4, 5])
# 通过map方法将全部数据都乘以10
# def func(data):
#     return data * 10

rdd2 = rdd.map(lambda x: x * 10).map(lambda x: x + 5)

print(rdd2.collect())
# (T) -> U
# (T) -> T

# 链式调用

