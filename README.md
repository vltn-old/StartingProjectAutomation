### Install:

You need to copy the github repo and install the requested python librairies.

```bash
git clone "https://github.com/vltn17/Starting-project-automation.git"
cd Starting-project-automation

pip install PyGithub
```

### Setup:

You need to these functions to begin.

```bash
createProject --setPath
createProject --setLoginInfos
```

### Use in cmd:

To use this script with cmd call you need to create (for windows) a .cmd script that run the python script. Do not miss to add your .cmd script to your path.


Exemple:

createProject.cmd
```bash
@echo off

python <the path to the python script .py> %1 %2 %3
```

!!! Module symbols with number are very important. There pass argument to the python script.