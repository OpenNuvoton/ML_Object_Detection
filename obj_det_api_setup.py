import os
from py_setenv import setenv
import argparse
import pycocotools
import shutil
import google.protobuf.internal
        
def fix_pycocotools():
    print("fix pycocotools cocoeval.py")
    fix_path = os.path.abspath(pycocotools.__file__)
    fix_path = os.path.join(fix_path.split("__init__.py")[0], "cocoeval.py")
    src_location = os.path.join(os.getcwd(), 'tool/cocoeval.py')
    shutil.copyfile(src_location, fix_path)

def fix_protobuf():
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
    src_setup = os.path.join(new_path, "object_detection", "packages", "tf2", "setup.py")
    shutil.copyfile(src_setup, dst_setup)
    ##Excute the cmd
    f = os.popen(r"python -m pip install .", "r")
    l = f.read()
    print(l)
    f.close()
    
    os.chdir(cwd)
    print("Change back working directory: {0}".format(cwd))

def obj_det_api_setup():
    print("======================================")  
    print("== Install the Object Detection API ==")
    print("======================================")        
    
    fix_pycocotools()
    install_obj_det_api()
    if FLAGS.fix_protobuf_builder:
        fix_protobuf()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
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
    obj_det_api_setup()    






