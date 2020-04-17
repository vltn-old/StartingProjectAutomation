import sys, os;
from github import Github;

# Created by Valentin Le Lièvre
# Portfolio: valentin-lelievre.com

# How to use:
#   _ type "createProject" in cmd and add the name of the project in one word
#   _ you can type --help for more infos about the usage of that script (exemple: createProject --help)

def createProject(arguments):
    email = getGithubLogin(arguments)[0][:-len("\n")];
    mdp = getGithubLogin(arguments)[1][:-len("\n")];

    normalPath = getPath(arguments)[0][:-len("\n")];
    testPath = getPath(arguments)[1][:-len("\n")];


    if email == "False" or email == "False" or email == "False" or email == "False":
        return False;

    path = "";

    projectName = arguments[1];

    if "--test" in arguments:
        print('Selected normal project folder');
        path = testPath;
    else:
        print('Selected test project folder');
        path = normalPath;

    print();

    print('Going to ' + path);
    os.chdir(path);

    print();

    print('Creating new project folder.');
    os.system('createFolder ' + projectName);
    
    print();
    
    print('Going to ' + projectName + 'folder');
    os.chdir(projectName);

    print();

    print('Creating README.md file');
    os.system('createFile README.md');

    print();

    print('Do git init');
    os.system('git init');

    print();

    print('Connecting to github and get user infos');
    github = Github(email, mdp);
    user = github.get_user();

    repository = user.create_repo(projectName);
    login = user.login;

    print();

    print('Configurating user identification to github for the project.');
    os.system('git config user.email "' + email + '"');

    print('Add github remote to the project');
    os.system('git remote add origin https://github.com/' + login + '/' + projectName + '.git');

    print();

    print('Do the innitial commit');
    os.system('git add .');
    os.system('git commit -m "Initial commit"');
    os.system('git push -u origin master');



def getGithubLogin(arguments):
    try:
        file = open(arguments[0][:-len("Create project/createProject.py")] + "githubLogin.txt", "r");
        fileData = file.readlines();

        return fileData;
    except:
        print('!!! You miss to set your github login data.');
        print('Call createProject --setLoginInfos to fix this error');
        print('See "createProject --help" for more infos.');
        print();

        return "False";

def getPath(arguments):
    try:
        file = open(arguments[0][:-len("Create project/createProject.py")] + "path.txt", "r");
        fileData = file.readlines();

        return fileData;
    except:
        print('!!! You miss to set your path data.');
        print('Call createProject --setPath to fix this error');
        print('See "createProject --help" for more infos.');
        print();

        return "False";



def setPath(arguments):
    print("What is your common project path ?");
    normalPath = input();

    print();

    print("What is your test project path ?");
    testPath = input();

    file = open(arguments[0][:-len("Create project/createProject.py")] + "path.txt","a+");
    file.write(normalPath + "\n");
    file.write(testPath + "\n");
    file.close();

def setLoginInfos(arguments):
    print("What is your github account email adress ?");
    email = input();

    print();

    print("What is your github account password ?");
    password = input();

    file = open(arguments[0][:-len("Create project/createProject.py")] + "githubLogin.txt","a+");
    file.write(email + "\n");
    file.write(password + "\n");
    file.close();

    

def help(): # function help that list all function and there utilisation
    print();

    print('How to use create project:');
    print("    _ createProject <project name> <optional>");
    print("    _ createProject --setPath");
    print("    _ createProject --setLoginInfos");
    print("    _ createProject --help");

    print();

    print('createProject <project name> <optinal>:');
    print('    your project name need to be one word.');
    print('    you can add "--test" arguments to create the file in your test directory.');

    print();
    
    print('!!! *** !!!');
    print();
    print('Important: before using createProject you NEED:');
    print('    to refers your general project folder and your test project folder. See setPath function for more infos');
    print('    to refers your github account email adress and github password');
    print();
    print('!!! *** !!!');



def main():
    arguments = sys.argv; # get all the arguments

    if "--help" in arguments: # run the help function
        help();
    elif "--setPath" in arguments: # run setPath function
        setPath(arguments);
    elif "--setLoginInfos" in arguments: # run setLoginInfos function
        setLoginInfos(arguments);
    else: # create the project
        createProject(arguments);

main();