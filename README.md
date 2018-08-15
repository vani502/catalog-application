# Item Catalog Application Project

This application provides a list of items within a variety of categories as well as provides a user registration and authentication system. Registered users will have the ability to post, edit and delete their own items.

## Getting Started

These instructions will include details of all the steps required to run a dynamic web application.

## Prerequisites

* [Python](https://www.python.org)
* [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
* [Vagrant](https://www.vagrantup.com/downloads.html)

## Directons

* Install VirtualBox
* Install Vagrant

Download the VM Configuration

* Download and unzip [FSND-Virtual-Machine.zip](https://github.com/udacity/fullstack-nanodegree-vm/archive/master.zip)
* Or you can use GitHub to fork and clone the repository https://github.com/udacity/fullstack-nanodegree-vm
* After you have downloaded the files change to the fullstack-nanodegree-vm
* Inside that directrory there is another directory called vagrant change to the vagrant directrory

Start the virtual machine

* From your terminal inside the vagrant subdirectory run the command **vagrant up** to launch your virtual machine
* When vagrant up has finished running you can then run **vagrant ssh** to log into the virtual machine
* Inside the virtual machine change to /vagrant directory by typing **cd /vagrant**

Download the application

* Download and upzip
* Place the cloned or downloaded files inside the catalog folder


## Run the application

* Type **python database_setup.py** to initialize the database
* Type **python lotsofitems.py** to populate the database
* Type **python project.py** to run the Flask web server
* In your browser visit **http://localhost:5000** to view the catalog application. You should be able to view a public version of the catalog. When logged in you can add, edit, and delete items you create.


## Running the Restaurant Menu App
Once it is up and running, type **vagrant ssh**. This will log your terminal into the virtual machine, and you'll get a Linux shell prompt. When you want to log out, type **exit** at the shell prompt.  To turn the virtual machine off (without deleting anything), type **vagrant halt**. If you do this, you'll need to run **vagrant up** again before you can log into it.
