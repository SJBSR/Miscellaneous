import boto3


def get_ec2_clinet() -> boto3.client:
    """
    Creates and returns and EC2 client using Boto3.
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

    def create_instance(ec2_client, ami_id: str = "ami-025ca978d4c1d9825", ami_amount: int = 1) -> None:
      """
      Create one EC2 instance based on the specified AMI ID.

      Args:
      ec2_client: The EC2 client object used to interact with AWS EC2.
      ami_type (str): The type of AMI to launch. Defaults to "amazon linux 2023".
      ami_mount (int): The number of instances to create Defaults to 1.

      Returns:
      None
      """

    
    return
    create_instance(client, "ami-0dbc5a419290457bc") # Call to create Amazon Linux 2023 AMI ID