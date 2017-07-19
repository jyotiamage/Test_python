import os,os.path

def file_Count_in_Dir():
    print(len([name for name in os.listdir('d:') if os.path.isfile(name)]))

def file_list():
    ls=os.listdir('.')
    file_count = len(ls)
    print(file_count)
    
#This function give us the count of file in a directory 
def file_only():
    onlyfiles=next(os.walk(r'D:\TEM-Tivoli Endpoint Manager\Git_Repo\site-Patches_for_Ubuntu_1404\Fixlets\amd64\Security'))[2]
    print(len(onlyfiles))

file_only()
#file_list()
#file_Count_in_Dir()

