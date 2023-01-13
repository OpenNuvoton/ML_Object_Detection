import requests as req
import os
import zipfile
from py_setenv import setenv
import argparse
import shutil

def download(url, dir_path):
    filename = url.split('/')[-1]
    download_loc = os.path.join(dir_path, filename)
    r = req.get(url, stream=True)
    with open(download_loc, 'wb') as f:
        for data in r.iter_content(1024):
            f.write(data)
        print("download finish!")    
    return filename

def create_folder(dir_path):
    try:
        os.mkdir(dir_path)
        print('create folder finish!') 
    except OSError as error:
        print(error)
        print('skip create folder.')
        
def zip_extract(url, dir_path):
    filename = url.split('/')[-1]
    zip_file_loc = os.path.join(dir_path, filename)
   
    if (zipfile.is_zipfile(zip_file_loc)):
        print("Start to extract: {}".format(zip_file_loc))
        with zipfile.ZipFile(zip_file_loc, 'r') as zf:
            # Test CRC
            crc_result = zf.testzip()
            if crc_result:
                print(crc_result)
            # extract the ZIP
            try:
                zf.extractall(path = dir_path)
                print("extract finish!")
            except zipfile.BadZipfile as e:
                print("ZIP file error：", e)
        
    else:
        print('The file is not a ZIP.')

def env_variable_protobuf(dir_path):
    dir_path = os.path.join(dir_path, 'bin')
    setenv("path", value=dir_path, append=True, user=False)
        
def compile_protobuf():
    cwd = os.getcwd()
    new_path = os.path.join(cwd, "models", "research")
    print("New working directory: {0}".format(new_path))
    os.chdir(new_path)
    print("compile protobuf")
    #p = subprocess.Popen("protoc object_detection/protos/*.proto --python_out=.", shell=True, stdout=subprocess.PIPE)
    #r = p.stdout.read()
    #print(r)
    
    f = os.popen(r"protoc object_detection/protos/*.proto --python_out=.", "r")
    l = f.read()
    #print(l)
    f.close()
    
    os.chdir(cwd)
    print("Change back working directory: {0}".format(cwd))

def Protobuf_setup():
    print("================================")  
    print("== Protobuf Installation step ==")
    print("================================")        
    create_folder(FLAGS.folder_path_proto)
    download(FLAGS.url_proto, FLAGS.folder_path_proto)
    zip_extract(FLAGS.url_proto, FLAGS.folder_path_proto)
    #env_variable_protobuf(FLAGS.folder_path_proto)
    compile_protobuf()

def download_VSBT(url, dir_path):
    filename = "mu_visual_cpp_build_tools_2015_update_3_x64_dvd_dfd9a39c.iso"
    download_loc = os.path.join(dir_path, filename)
    r = req.get(url, stream=True)
    with open(download_loc, 'wb') as f:
        for data in r.iter_content(1024):
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

def fix_pycocotools():
    import pycocotools
    print("fix pycocotools cocoeval.py")
    fix_path = os.path.abspath(pycocotools.__file__)
    fix_path = os.path.join(fix_path.split("__init__.py")[0], "cocoeval.py")
    src_location = os.path.join(os.getcwd(), 'tool/cocoeval.py')
    shutil.copyfile(src_location, fix_path)

def fix_protobuf():
    import google.protobuf.internal
    print("fix protobuf builder.py")
    fix_path = os.path.abspath(google.protobuf.internal.__file__)
    fix_path = os.path.join(fix_path.split("__init__.py")[0], "builder.py")
    src_location = os.path.join(os.getcwd(), 'tool/builder.py')
    shutil.copyfile(src_location, fix_path)    

def install_obj_det_api():
    cwd = os.getcwd()
    print("Current working directory: {0}".format(cwd))
    new_path = os.path.join(cwd, "models", "research")
    print("New working directory: {0}".format(new_path))
    os.chdir(new_path)
    
    ## copy setup
    dst_setup = os.path.join(new_path, "setup.py")
    src_setup = os.path.join(new_path, "object_detection", "packages", "tf1", "setup.py")
    shutil.copyfile(src_setup, dst_setup)
    ##Excute the cmd
    f = os.popen(r"python -m pip install .", "r")
    l = f.read()
    print(l)
    f.close()
    
    os.chdir(cwd)
    print("Change back working directory: {0}".format(cwd))

def check_fix_proto_missing():
    import object_detection 
    fix_path = os.path.join(os.path.abspath(object_detection.__file__).split("__init__.py")[0], 'protos')
    cwd = os.getcwd()
    src_path = os.path.join(cwd, "models", "research", "object_detection", "protos")
    
    isExist = os.path.exists(fix_path)
    if not isExist:
        print("The protos folder is missing at here: {}".format(fix_path))
        shutil.copytree(src_path, fix_path)
        # add a __init__.py
        f = open(os.path.join(fix_path, "__init__.py"), 'w')
        f.close()
        print("Copy from my ML_tf2_object_detection_nu, total files: {}".format(len(os.listdir(fix_path))))
    else:
        print("The protos folder is good.")

def obj_det_api_setup():
    print("======================================")  
    print("== Install the Object Detection API ==")
    print("======================================")        
    
    fix_pycocotools()
    install_obj_det_api()
    if FLAGS.fix_protobuf_builder:
        fix_protobuf()
    check_fix_proto_missing()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # Protobuf_setup #
    parser.add_argument(
        '--folder_path_proto',
        type=str,
        default=r'C:\Program Files\Google Protobuf',
        help='The create folder name & path env variable value.')
    parser.add_argument(
        '--url_proto',
        type=str,
        default='https://github.com/protocolbuffers/protobuf/releases/download/v21.9/protoc-21.9-win64.zip',
        help='url of protoc.')
    # cocoapi_setup #    
    parser.add_argument(
        '--folder_path_VSBT',
        type=str,
        default=r'C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC',
        help='The install location of Microsoft Visual Studio 14.0 which is used for env variable.')
    parser.add_argument(
        '--url_VSBT',
        type=str,
        default='https://myvs.download.prss.microsoft.com/dbazure/mu_visual_cpp_build_tools_2015_update_3_x64_dvd_dfd9a39c.iso?t=61dd1ca3-f85f-4192-86bb-07f91a31378d&e=1669900920&h=c4b3f02af8bd60abf870b0dd9c3b69c967aaf33e85758226edbd58080f30c7fc&su=1',
        help='url of mu_visual_cpp_build_tools_2015.')
    parser.add_argument(
        '--download_step_VSBT',
        type=bool,
        default=False,
        help='True will run only build tool download.')
    # obj_det_api_setup #
    parser.add_argument(
        '--fix_protobuf_builder',
        action='store_true',
        help='This will add builder.py to protobuf install location to fix protobuf old version issue.')
    parser.add_argument(
        '--no-fix_protobuf_builder',
        action='store_false',
        dest='fix_protobuf_builder',
        help='This will skip add builder.py.')
    parser.set_defaults(feature=False)     

    FLAGS, _ = parser.parse_known_args()
    
    # Protobuf_setup #
    #Protobuf_setup() # TF1 skip, if TF2 is installed
    # cocoapi_setup #
    if FLAGS.download_step_VSBT:
       print("download visual_cpp_build_tools")
       download_VSBT(FLAGS.url_VSBT, os.getcwd())
    else:
       cocoapi_setup()
    # obj_det_api_setup #
    obj_det_api_setup()    





