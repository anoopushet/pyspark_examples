from pyspark.sql import SparkSession
from pyspark.sql.types import StructType,StructField,StringType,IntegerType

schema = StructType([
    StructField("First Name",StringType(),True),
    StructField("Middle Name",StringType(),True),
    StructField("Last Name",StringType(),True)
])

spark = SparkSession.builder.appName("assignement").master("local").getOrCreate()

emptyrdd = spark.sparkContext.emptyRDD()