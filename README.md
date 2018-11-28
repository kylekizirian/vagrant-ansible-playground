# vagrant-ansible-playground

Playground for learning Vagrant and Ansible

## Requirements

Install [Vagrant](https://www.vagrantup.com/) and [Ansible](https://www.ansible.com/)

## To Start GUI on VM

```bash
git clone https://github.com/kylekizirian/vagrant-ansible-playground.git
cd vagrant-ansible-playground
vagrant up
```

In VirtualBox window, log on with

username: vagrant
password: vagrant

and run

```bash
startx
```

## To Run Python Script in VM

```bash
git clone https://github.com/kylekizirian/vagrant-ansible-playground.git
cd vagrant-ansible-playground
vagrant up
vagrant ssh
python3 monte-carlo-sim/monte_carlo_sim.py
logout
```

## Resources

Browsing through [Full Stack Python](https://www.fullstackpython.com/) guides on
[configuration management](https://www.fullstackpython.com/configuration-management.html)
and [Ansible](https://www.fullstackpython.com/ansible.html)
