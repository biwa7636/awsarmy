import sys
import boto.ec2
import time

# soldier_v0.1
my_ami_image_id = 'ami-xxxx'     # Ubuntu Server 12.04 LTS (PV)
my_instance_type = 't1.micro'         
my_security_groups = ['launch-wizard-1']
my_aws_access_key_id = ''
my_aws_secret_access_key = ''

script_soldier = """#!/usr/bin/python
import urllib2
import imp
import time
import json
import zlib
opener_army = urllib2.build_opener()
opener_army.addheaders = [('User-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36')]

# Commander API Server End Points 
host = "http://xx.xxx.xxx.xx:5000"
host_distributefunction = host + "/distributefunction"
host_distributeinput = host + "/distributeinput"
host_contribute = host + "/contribute"
host_terminate = host + "/terminate"

# 1. Retrieve environment and function from Commander
myfunction_text = opener_army.open(host_distributefunction).read()
exec myfunction_text

while(1):
    # 2. Retrieve input from Commander and generate result
    myinput = opener_army.open(host_distributeinput).read().strip()
    if 'stop' in myinput:
        break
    myoutput = myfunction(myinput)
    myoutput = json.loads(myoutput)
    # 3. Send the result back to commander
    result = {'myinput':myinput, 'myoutput': myoutput}
    data = zlib.compress(json.dumps(result))
    opener_army.open(host_contribute, data)

# 4. Terminate myself or send the terminate request to commander using instance ip or id
# More Info: (http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AESDG-chapter-instancedata.html)
instance_id = opener_army.open('http://169.254.169.254/latest/meta-data/instance-id').read().strip()
opener_army.open(host_terminate + "/" + instance_id)
"""

def awsTerminate(instance_id):
    try:
        conn = boto.ec2.connect_to_region('us-west-1', aws_access_key_id=my_aws_access_key_id, aws_secret_access_key=my_aws_secret_access_key)
        conn.terminate_instances(instance_ids=[instance_id])
        print 'Terminated Success'
        return 0
    except:
        print sys.exc_info()
        return 1


def awsScale(instance_number):
    try:
        conn = boto.ec2.connect_to_region(region_name='us-west-1', \
                                          aws_access_key_id=my_aws_access_key_id, \
                                          aws_secret_access_key=my_aws_secret_access_key)

        reservation = conn.run_instances(image_id=my_ami_image_id, \
                                         min_count=instance_number, \
                                         max_count=instance_number, \
                                         key_name='soldier', \
                                         instance_type=my_instance_type,  \
                                         security_groups=my_security_groups, \
                                         user_data=script_soldier)
        time.sleep(10)
        for idx, instance in enumerate(reservation.instances):
            instance.add_tag('Name', 'soldier' + str(idx))
        print 'Start Instances'
    except:
        print sys.exc_info()
        pass

