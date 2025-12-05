import boto3


def get_ec2_client() -> boto3.client:
    """
    Creates and returns an EC2 client using Boto3.
    Returns:
    boto3.client: The EC2 client.
    """
    return boto3.client("ec2")

def create_amazon_linux_2023_instance(client: boto3.client) -> None:
    """
    Creates an Amazon Linux 2023 instance.

    Args:
    client (boto3.client): The EC2 client used to create the instance.

    Returns:
    None
    """
    def create_instance(ec2_client, ami_id: str = "ami-025ca978d4c1d9825", instance_count: int = 1) -> None:
        """
        Create EC2 instance(s) based on the specified AMI ID.

        Args:
        ec2_client: The EC2 client object used to interact with AWS EC2.
        ami_id (str): The AMI ID to launch. Defaults to "ami-025ca978d4c1d9825".
        instance_count (int): The number of instances to create. Defaults to 1.

        Returns:
        None
        """
        try:
            response = ec2_client.run_instances(
                ImageId=ami_id,
                MinCount=instance_count,
                MaxCount=instance_count,
                InstanceType='t2.micro'    # You may want to make this configurable
            )
            instance_ids = [instance['InstanceId'] for instance in response['Instances']]
            print(f"Successfully created {len(instance_ids)} instance(s): {instance_ids}")
        except Exception as e:
            print(f"Error creating instance: {e}")
    
    create_instance(client, "ami-0dbc5a419290457bc")  # Call to create Amazon Linux 2023 AMI ID

# Example usage:
if __name__ == "__main__":
    ec2_client = get_ec2_client()
    create_amazon_linux_2023_instance(ec2_client)