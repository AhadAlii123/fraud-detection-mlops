terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "mlops_production_node" {
  ami           = "ami-0c7217cdde317cfec" # Ubuntu Server 22.04 LTS
  instance_type = "t2.medium"

  tags = {
    Name        = "Fraud-Detection-MLOps-Prod"
    Environment = "Production"
    Project     = "Fraud-Detection"
  }
}