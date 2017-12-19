# ecosia_ashish

## Setup
1. The script requires Python3
2. Install python boto3 module:<br/>
  pip install boto3
  
## Running the script
The script <b>launch_ec2.py</b> can be run from bash giving the AWS Access Key ID, AWS Secret Access Key, AWS region and Instance Type as parameters.<br/>
 Example:<br/> python launch_ec2.py -a AWS_ACCESS_KEY_ID -s AWS_SECRET_ACCESS_KEY -i INSTANCE_TYPE -r AWS_REGION
 
 ## Help
 Run scipt with -h or --help as parameters to know the required parameters<br/>
 python launch_ec2.py -h
