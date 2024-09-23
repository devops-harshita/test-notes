#!/bin/bash

# Update the package index
sudo yum update -y

# Install Python
sudo yum install -y python3 python3-pip

# Verify Python installation
python3 --version
pip3 --version

# Install AWS CLI
sudo yum install -y aws-cli

# Verify AWS CLI installation
aws --version

# Install Terraform
TERRAFORM_VERSION="1.5.5"  # Specify the desired Terraform version
TERRAFORM_ZIP="terraform_${TERRAFORM_VERSION}_linux_amd64.zip"

# Download Terraform
curl -LO "https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/${TERRAFORM_ZIP}"

# Unzip and install Terraform
sudo unzip $TERRAFORM_ZIP -d /usr/local/bin/
sudo chmod +x /usr/local/bin/terraform

# Verify Terraform installation
terraform --version

# Clean up
rm $TERRAFORM_ZIP

echo "Installation complete!"
