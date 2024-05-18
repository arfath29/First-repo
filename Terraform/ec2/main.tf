provider "aws" {
  region = "ap-south-1"
}
resource "aws_instance" "ec2-in" {
  ami  ="ami-0ba259e664698cbfc"
  instance_type = "t2.micro"
   security_groups = [aws_security_group.TF_SG.name]
   key_name = "TF_key"
  tags = {
    Name="ec2-in" 
  }
}
resource "aws_security_group" "TF_SG" {
  name        = "Terraform_Sec"
  description = "Terraform_Sec"
  ingress {
    description="HTTP"
    from_port=80
    to_port=80
    protocol="tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  ingress{
    description="SSH"
    from_port=22
    to_port=22
    protocol="tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
   ingress{
    description="Custom"
    from_port=8080
    to_port=8080
    protocol="tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  tags = {
    Name="Terraform_Sec"
  }
}
resource "aws_key_pair" "TF_key" {
  key_name = "TF_key"
  public_key = tls_private_key.rsa.public_key_openssh
}
resource "tls_private_key" "rsa" {
  algorithm = "RSA"
  rsa_bits = 4096
}
resource "local_file" "TF_tls" {
  content = tls_private_key.rsa.private_key_pem
  filename = "tf_pub"
}

