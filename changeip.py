my_aws_access_key_id = "..."
my_aws_secret_access_key = "..."
my_instance_id = ".."
my_target_ip = "http://xxx/index.html"
 
# here gives you 10 seconds to put the job in nohup and log out of the box
# otherwise, the ssh pipe will be broken after the ip changed and unpredictable things will happen.
time.sleep(10)
 
# make a http request to target server
urllib2.urlopen(my_target_ip)
conn = boto.ec2.connect_to_region("us-east-1", aws_access_key_id=my_aws_access_key_id, aws_secret_access_key=my_aws_secret_access_key)
myaddress = conn.allocate_address()
time.sleep(5)
conn.associate_address(instance_id=my_instance_id, public_ip=myaddress.public_ip)
# the sleeping is actually fairly important to wait till the AWS modification takes effect.
time.sleep(20)
# make another http using the new ip
urllib2.urlopen(my_target_ip)
conn.disassociate_address(public_ip=myaddress.public_ip)
conn.release_address(allocation_id=myaddress.allocation_id)
time.sleep(20)
 
# make another http request after disassociating the Elastic IP
# actually, it won't go back to the IP before and will be given a new ip surprisingly.
urllib2.urlopen(my_target_ip)
