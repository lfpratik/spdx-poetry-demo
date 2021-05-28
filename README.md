# spdx-poetry-demo

### Steps to follow

###### Clone Project

    https client: 
    <your_workspace_dir>$ git clone https://github.com/lfpratik/spdx-poetry-demo.git
    
    ssh client: 
    <your_workspace_dir>$ git clone git@github.com:lfpratik/spdx-poetry-demo.git

###### Goto project dir
    cd spdx-poetry-demo

###### install prerequisite 
    curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

    source ~/.bashrc | source ~/.bash_profile   # if you are using bash
    source ~/.zshrc                             # if you are using zsh
    poetry --version | poetry -V                # Poetry version 1.1.6

###### Create a virtul env for project
    spdx-poetry-demo$ poetry shell

###### Install requirements
    (spdx-poetry-demo) spdx-poetry-demo$ poetry install     # first step 
    (spdx-poetry-demo) spdx-poetry-demo$ poetry update      # run this if any issue occured
