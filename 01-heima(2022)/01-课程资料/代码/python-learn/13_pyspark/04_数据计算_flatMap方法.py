"""
演示RDD的flatMap成员方法的使用
"""
from pyspark import SparkConf, SparkContext
import os
os.environ['PYSPARK_PYTHON'] = "D:/dev/python/python310/python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

# 准备一个RDD
rdd = sc.parallelize(["itheima itcast 666", "itheima itheima itcast", "python itheima"])

# 需求，将RDD数据里面的一个个单词提取出来
rdd2 = rdd.flatMap(lambda x: x.split(" "))
print(rdd2.collect())
