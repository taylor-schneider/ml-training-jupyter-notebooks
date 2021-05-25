def determine_ip_address():
    # Determine the ip address of the machine
    import netifaces
    import re
    nic_uuid = netifaces.gateways()['default'][netifaces.AF_INET][1]
    nic_details = netifaces.ifaddresses(nic_uuid)
    ip_address = None
    for i, nic_detail, in nic_details.items():
        if all([key in nic_detail[0].keys() for key in ["addr", "netmask", "broadcast"]]):
            if re.match("([0-9]+\\.)+", nic_detail[0]["addr"]):
                ip_address = nic_detail[0]["addr"]
                break
    if not ip_address:
        raise Exception("Unable to determine ip address.")
    return ip_address
    

def create_spark_context(spark_app_name, docker_image, k8_master_ip):
    
    print("Setting SPARK_HOME")
    import os
    os.environ['SPARK_HOME'] = "c:\\spark\\spark-3.1.1-bin-hadoop2.7"
    print(os.environ['SPARK_HOME'])
    print("")

    print("Running findspark.init() function")
    import findspark
    findspark.init()
    import sys
    print(sys.path)
    print("")

    print("Setting PYSPARK_PYTHON")
    os.environ['PYSPARK_PYTHON'] = "/usr/bin/python3"
    print(os.environ['PYSPARK_PYTHON'])
    print("")


    print("Determine IP Of Server")
    ip_address = determine_ip_address()
    print("The ip was detected as: {0}".format(ip_address))
    print("")

    # Set some vars to specify where the kubernetes master is
    kubernetes_master_ip = k8_master_ip
    kubernetes_master_port = "6443"
    spark_master_url = "k8s://https://{0}:{1}".format(kubernetes_master_ip, kubernetes_master_port)

    print("Create SparkContext")

    # Wire up the SparkConf object
    import pyspark
    sparkConf = pyspark.SparkConf()
    sparkConf.setMaster(spark_master_url)
    sparkConf.setAppName(spark_app_name)
    sparkConf.set("spark.submit.deploy.mode", "cluster")
    sparkConf.set("spark.kubernetes.container.image", docker_image) 
    sparkConf.set("spark.kubernetes.namespace", "spark")
    sparkConf.set("spark.kubernetes.pyspark.pythonVersion", "3")
    sparkConf.set("spark.kubernetes.authenticate.driver.serviceAccountName", "spark-sa")
    sparkConf.set("spark.kubernetes.authenticate.serviceAccountName", "spark-sa")
    sparkConf.set("spark.executor.instances", "3")
    sparkConf.set("spark.executor.cores", "2")
    sparkConf.set("spark.executor.memory", "1024m")
    sparkConf.set("spark.driver.memory", "1024m")
    sparkConf.set("spark.driver.host", ip_address)
    sparkConf.getAll()

    from pyspark.sql import SparkSession
    spark = SparkSession.builder.config(conf=sparkConf).getOrCreate()
    sc = spark.sparkContext

    print("")

    sparkConf.getAll()
    
    return sc