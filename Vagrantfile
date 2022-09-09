# Vagrant.configure("2") do |config|
#   # Provisioning Using VmWareFusion
#   config.vm.define "game" do |game|
#     game.vm.box = "spox/ubuntu-arm"
#     game.vm.network "private_network", ip: "192.168.56.20"
#     game.vm.provider "vmware_fusion" do |vb|
#       config.vm.synced_folder "app/", "/home/vagrant/app" 
#     end
#     game.vm.provision "shell", inline: <<-SHELL
#       systemctl disable apt-daily.service
#       systemctl disable apt-daily.timer
#       sudo apt remove unattended-upgrades -y
#     SHELL
#     game.vm.provision "shell", path: "env/script.sh"
#   end




Vagrant.configure("2") do |config|
  # Provisioning Using VirtualBox
  config.vm.define "game" do |game|
    game.vm.box = "generic/ubuntu2010"
    game.vm.network "private_network", ip: "192.168.56.20"
    game.vm.provider "virtualbox" do |vb|
      config.vm.synced_folder "app/", "/home/vagrant/app" 
    end
    game.vm.provision "shell", path: "env/script.sh"
  end