# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "ubuntu14.04"
  config.vm.network :forwarded_port, guest: 8000, host: 8000
  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "ansible/site.yml"
  end
end

