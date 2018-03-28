# Celery, Bottlepy Boilerplate

Ansible playbook to setup Celery with a http based task-runner. This wil setup following tools and libraries:

- [Bottle](https://github.com/bottlepy/bottle) for building a very basic task-runner, which acts like a producer for queueing jobs in celery worker(s)
- [Celery](http://www.celeryproject.org/), for background worker tasks
- [RabbitMQ](https://github.com/rabbitmq/rabbitmq-server) as message broker for celery
- [Flow-er](https://github.com/mher/flower) for viewing and managing celery workers


This is a good starting point for modern High performance Python web projects 

## Dependencies

- Ubuntu 16.04
- Ansible


## Installation Instructions

- Clone this repository on your workstation 
- `git clone https://github.com/cyrenity/celery-bottle-boilerplate.git`
- Change directory to playbook directory `cd celery-bottle-boilerplate/playbook`
- Create ansible inventory (inventory.txt) for your host, it should look like this
> \[app_servers\]      
> app_server   ansible_ssh_host=192.168.0.10  ansible_ssh_user=ssh_user

- Enable password less login for ssh_user@192.168.0.10 

    Run `ssh-keygen` to generate your SSH key and
    then run below command to enable password less login for your server

    `ssh-copy-id ssh_user@192.168.0.10`
    
    
- Run playbook with following arguments
> `ansible-playbook  -i inventory.txt main.yml  --ask-become-pass -e "app_name=MYAPP"`     
>  Replace MYAPP with your desired app name (NO special characters and spaces)


