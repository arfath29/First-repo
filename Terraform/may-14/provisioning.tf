provider "aws" {
  region = "ap-south-1" 
}
resource "aws_key_pair" "dove-key" {
  key_name = "dovekey"
  public_key = file("dovekey.pub")
}
resource "aws_instance" "my-inst" {
  ami           = "ami-0cc9838aa7ab1dce7"
  instance_type = "t2.micro" 
  key_name = aws_key_pair.dove-key.key_name
  vpc_security_group_ids = ["sg-021d61866a0bb012a"]
  

  tags = {
    Name = "provision"
  }
  
  provisioner "file" {
    source = "web.sh"
    destination = "/tmp/web.sh"
  }

  provisioner "remote-exec" {
    inline = [ 
      "chmod u+x /tmp/web.sh",
      "sudo /tmp/web.sh"
    ]
  }
    connection {
      user        = "ec2-user"
      private_key = file("dovekey") 
      host        = self.public_ip
  }
}


output "public_ip" {
    value = aws_instance.my-inst.public_ip
  }
output "private_ip" {
    value = aws_instance.my-inst.private_ip
  }
