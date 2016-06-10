#!/usr/bin/env python

import shutil
import sys
import os

def link_sage_kernelspec(target_dir):
    kernels_dir = os.path.join(target_dir, "kernels")
    try: 
        os.makedirs(kernels_dir)
    except OSError:
        if not os.path.isdir(kernels_dir):
            print("Error: cannot install sage kernel.")
            return
    sage_target_kernel = os.path.join(kernels_dir, "sagemath")
    sage_source_kernel = "/sage/current/local/share/jupyter/kernels/sagemath"
    if os.path.exists(sage_source_kernel):
        if os.path.exists(sage_target_kernel):
            try:
                os.remove(sage_target_kernel)
            except:
                print("Error: cannot install sage kernel.")
                return
        os.symlink(sage_source_kernel, sage_target_kernel)

def link_sage_nbextensions(target_dir):
    nbext_dir = os.path.join(target_dir, "nbextensions")
    try: 
        os.makedirs(nbext_dir)
    except OSError:
        if not os.path.isdir(nbext_dir):
            print("Error: cannot install sage kernel.")
            return
    for ext in [ "jsmol", "mathjax" ]:
        ext_target_dir = os.path.join(nbext_dir, ext)
        ext_source_dir = "/sage/current/local/share/jupyter/nbextensions/" + ext
        if os.path.exists(ext_source_dir):
            if os.path.exists(ext_target_dir):
                try:
                    os.remove(ext_target_dir)
                except:
                    print("Error: cannot install sage nbextension `%s'." % ext)
                    continue
            os.symlink(ext_source_dir, ext_target_dir)

def main():
    if len(sys.argv) == 1:
        target_dir = ""
        python_path = ""
    elif len(sys.argv) == 2:
        target_dir = sys.argv[1]
        python_path = ""
    elif len(sys.argv) != 3:
        print("Error: wrong arguments.")
        return
    else:
        target_dir = sys.argv[1]
        python_path = sys.argv[2]
    if target_dir == "":
        target_dir = os.path.join(
            os.path.expanduser("~"), 
            "Library", 
            "Jupyter")
    if python_path == "":
        python_path = os.path.dirname(
            os.path.dirname(
                os.path.dirname(
                    os.path.abspath(__file__))))
    try: 
        os.makedirs(target_dir)
    except OSError:
        if not os.path.isdir(target_dir):
            print("Error: cannot install.")
            return
    link_sage_kernelspec(target_dir)
    link_sage_nbextensions(target_dir)

if __name__ == "__main__":
    main()
