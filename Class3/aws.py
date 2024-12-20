import boto3
import schedule
import time

# Specify your AWS region
region = 'us-east-1'

# Create a boto3 EC2 client with the specified region
ec2 = boto3.client('ec2', region_name=region)

# List of EC2 instance IDs to manage
INSTANCE_IDS = ['i-07f9e2f84c3123ad1', 'i-005c8f93b58c11b7e']  # Replace with your actual EC2 instance IDs

def start_instances():
    """Starts the specified EC2 instances."""
    print("Starting EC2 instances...")
    ec2.start_instances(InstanceIds=INSTANCE_IDS)
    print(f"Instances {INSTANCE_IDS} started successfully!")

def stop_instances():
    """Stops the specified EC2 instances."""
    print("Stopping EC2 instances...")
    ec2.stop_instances(InstanceIds=INSTANCE_IDS)
    print(f"Instances {INSTANCE_IDS} stopped successfully!")

# Schedule the start and stop tasks
schedule.every().day.at("03:05").do(start_instances)  # Schedules start at 8:00 AM
schedule.every().day.at("03:03").do(stop_instances)   # Schedules stop at 6:00 PM

# Run the scheduling loop
print("Scheduler is running. Press Ctrl+C to exit.")
while True:
    schedule.run_pending()
    time.sleep(60)  # Check every minute