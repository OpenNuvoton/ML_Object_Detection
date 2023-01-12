import requests as req
from tqdm import tqdm
import os
import zipfile
from py_setenv import setenv
import argparse

def download(url, dir_path):
    filename = url.split('/')[-1]
    download_loc = os.path.join(dir_path, filename)
    r = req.get(url, stream=True)
    with open(download_loc, 'wb') as f:
        for data in tqdm(r.iter_content(1024)):
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
    create_folder(FLAGS.folder_path)
    download(FLAGS.url, FLAGS.folder_path)
    zip_extract(FLAGS.url, FLAGS.folder_path)
    #env_variable_protobuf(FLAGS.folder_path)
    compile_protobuf()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--folder_path',
        type=str,
        default=r'C:\Program Files\Google Protobuf',
        help='The create folder name & path env variable value.')
    parser.add_argument(
        '--url',
        type=str,
        default='https://github.com/protocolbuffers/protobuf/releases/download/v21.9/protoc-21.9-win64.zip',
        help='url of protoc.')

    FLAGS, _ = parser.parse_known_args()
    Protobuf_setup()






