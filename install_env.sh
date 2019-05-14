#!/usr/bin/env bash

check_ubuntu_version() {
    YEAR="18"
    MONTH="04"

    version=$(lsb_release -r | awk '{ print $2 }')

    yrelease=$( echo "$version" | cut -d. -f1 )
    mrelease=$( echo "$version" | cut -d. -f2 )    

    if [ "$yrelease" -eq "$YEAR" ]; then
        if [ "$mrelease" -ge "$MONTH" ]; then
            return 1
        else
            return 0
        fi
    else
        if [ "$yrelease" -gt "$YEAR" ]; then
            return 1
        else
            return 0
        fi
    fi
}

install_python36_ubuntu18() {
    sudo apt-get install -y python3 python3-dev python3-pip
}

install_python36_ubuntu16() {
    sudo add-apt-repository -y ppa:deadsnakes/ppa
    sudo apt-get update
    sudo apt-get install -y python3.6 python3.6-dev python3-pip

    sudo apt-get install -y virtualenv

    virtualenv pyenv --python=python3.6
}


install_main() {
    check_ubuntu_version
    local is_ubuntu1804=$?
    if [ "$is_ubuntu1804" -eq 1 ]; then
        install_python36_ubuntu18
    else
        install_python36_ubuntu16
    fi
    
    if [ "$is_ubuntu1804" -eq 1 ]; then
        pip3 install -r requirements.txt
    else
        source pyenv/bin/activate
        pyenv/bin/pip install -r requirements.txt
    fi    
}

install_main