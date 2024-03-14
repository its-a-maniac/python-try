Practical No. 1
Aim: Installing and setting environment variables for Working with Apache Hadoop.
Theory: Apache Hadoop is an open-source software framework used to store, manage and 
process large datasets for various big data computing applications running under clustered 
systems. It is Java-based and uses Hadoop Distributed File System (HDFS) to store its data and 
process data using MapReduce.
Implementation:
# Installing Java 
1. In Ubuntu, open the terminal and enter the following command:
$ sudo apt install default-jdk default-jre -y
2. Verify the installation via
$ java -version
# Create new user Hadoop and configure password-less SSH
1. Create the new user
$ sudo adduser hadoop
2. Add the hadoop user to the sudo group.
$ sudo usermod -aG sudo hadoop
3. Log out of the current user and switch to the newly created Hadoop user
4. In terminal, install openssh client and server
$ apt install openssh-server openssh-client -y
5. Generate public and private key pairs.
$ ssh-keygen -t rsa
6. Add the generated public key from id_rsa.pub to authorized_keys.
$ sudo cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
7. Change the permissions of the authorized_keys file.
$ sudo chmod 640 ~/.ssh/authorized_keys
8. Verify if the password-less SSH is functional.
$ ssh localhos