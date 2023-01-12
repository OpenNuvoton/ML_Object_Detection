import requests as req
from tqdm import tqdm
import os
from py_setenv import setenv
import argparse

def download(url, dir_path):
    filename = "mu_visual_cpp_build_tools_2015_update_3_x64_dvd_dfd9a39c.iso"
    download_loc = os.path.join(dir_path, filename)
    r = req.get(url, stream=True)
    with open(download_loc, 'wb') as f:
        for data in tqdm(r.iter_content(1024)):
            f.write(data)
        print("download finish!")    
    return filename

def env_variable_VS(dir_path):
    setenv("VCINSTALLDIR", value=dir_path, user=True)
        
def install_cocoAPI():
   
    print("install_cocoAPI")
    #p = subprocess.Popen("protoc object_detection/protos/*.proto --python_out=.", shell=True, stdout=subprocess.PIPE)
    #r = p.stdout.read()
    #print(r)
    
    f = os.popen(r"pip install git+https://github.com/philferriere/cocoapi.git#subdirectory=PythonAPI", "r")
    l = f.read()
    print(l)
    f.close()

def cocoapi_setup():
    print("================================")  
    print("== COCOAPI Installation step ==")
    print("================================")        
    
    #env_variable_VS(FLAGS.folder_path)
    install_cocoAPI()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--folder_path',
        type=str,
        default=r'C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC',
        help='The install location of Microsoft Visual Studio 14.0 which is used for env variable.')
    parser.add_argument(
        '--url',
        type=str,
        default='https://myvs.download.prss.microsoft.com/dbazure/mu_visual_cpp_build_tools_2015_update_3_x64_dvd_dfd9a39c.iso?t=61dd1ca3-f85f-4192-86bb-07f91a31378d&e=1669900920&h=c4b3f02af8bd60abf870b0dd9c3b69c967aaf33e85758226edbd58080f30c7fc&su=1',
        help='url of mu_visual_cpp_build_tools_2015.')
    parser.add_argument(
        '--download_step',
        type=bool,
        default=False,
        help='True will run only build tool download.')
    

    FLAGS, _ = parser.parse_known_args()
    if FLAGS.download_step:
       print("download visual_cpp_build_tools")
       download(FLAGS.url, os.getcwd())
    else:
       cocoapi_setup()    






