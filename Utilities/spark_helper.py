import os
import netifaces
import re
import pyspark


def determine_ip_address():
    # Determine the ip address of the machine

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


def get_filesystem_root():
    if os.name == 'nt':
        return os .path.abspath('.').split(os.path.sep)[0] + os.path.sep
    else:
        return '/'

    
def link_data_dir_to_root(data_dir):
    data_dir = os.path.abspath(data_dir)
    for filename in os.listdir(data_dir):
        # Check if file is linked
        if not os.path.exists("/{0}".format(filename)):
            src = os.path.join(data_dir, filename)
            dest = os.path.join(get_filesystem_root(), filename)
            print("Creating Symlink: {0} -> {1}".format(src, dest))
            os.symlink(src, dest)

            
def unlink_data_dir_from_root(data_dir):
    data_dir = os.path.abspath(data_dir)
    for filename in os.listdir(data_dir):
        # Check if file is linked
        if os.path.exists("/{0}".format(filename)):
            src = os.path.join(data_dir, filename)
            dest = os.path.join(get_filesystem_root(), filename)
            if os.path.islink(dest):
                print("Removing Symlink: {0} -> {1}".format(src, dest))
                os.unlink(dest)

                
def create_spark_context(spark_master_url, spark_app_name, docker_image, ip_address=None):
    
    if ip_address is None:
        print("Determining IP Of Server")
        ip_address = determine_ip_address()
        print("The ip was detected as: {0}".format(ip_address))
        print("")
    
    print("Creating SparkConf Object")
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
    sparkConf.set("spark.executor.memory", "4096m")
    sparkConf.set("spark.executor.memoryOverhead", "1024m")
    sparkConf.set("spark.driver.memory", "1024m")
    sparkConf.set("spark.driver.host", ip_address)
    sparkConf.set("spark.files.overwrite", "true")
    sparkConf.set("spark.files.useFetchCache", "false")
    return sparkConf


def create_spark_session(spark_app_name, docker_image, k8_master_ip, spark_context=None):
    
    print("Setting SPARK_HOME")
    import os
    if os.name == 'nt':		# running on windows
        os.environ['SPARK_HOME'] = "c:\\spark\\spark-3.1.1-bin-hadoop2.7"
    else:
        os.environ['SPARK_HOME'] = "/opt/spark"
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

    print("Configuring URL for kubernetes master")
    kubernetes_master_ip = k8_master_ip
    kubernetes_master_port = "6443"
    spark_master_url = "k8s://https://{0}:{1}".format(kubernetes_master_ip, kubernetes_master_port)
    print(spark_master_url)
    print("")

    sparkConf = create_spark_context(spark_master_url, spark_app_name, docker_image)
    
    import pprint
    for item in sparkConf.getAll():
        print(item)
    print("")
    
    print("Creating SparkSession Object")
    from pyspark.sql import SparkSession
    spark_session = SparkSession.builder.config(conf=sparkConf).getOrCreate()
    print("")   

    print("Done!") 
    return spark_session