# Welcome To GAMENAMEHERE!

* In order to play this game you will need to have Vagrant installed on your machine. A full list of requirements can be found below:

-Vagrant (in order to launch the game)
  You can install vagrant **[HERE] (https://www.vagrantup.com/downloads)** using brew or the download link! 
-VirtualBox (if you are using a Windows or an Intel/AMD based Mac)
-VMWareFusion (If you are using an M1 arm based Mac)

## Instructions


**If You are using an M1/M2 ARM based Mac please do the following FIRST!!!! If not IGNORE THIS STEP**
1. Open the vagrantfile in your editor of choice.
2. Uncomment the Vagrant.Configure lines of code from lines 1 to 16.
3. Comment out the Vagrant.Configure lines from lines 21 to 32.

1. After you have Vagrant and VirtualBox or VMWare installed, you will need to open a terminal or powershell window. 
2. CD in to wherever you have saved this repository.
3. Run the command `vagrant up`
4. Wait for Vagrant to finish setting up the environment.
5. Use the command `vagrant ssh`
6. CD in to the app folder (It will be the only folder you can CD down into when you SSH in to vagrant)
7. Run the command `python3 game.py`
8. Enjoy the game!

