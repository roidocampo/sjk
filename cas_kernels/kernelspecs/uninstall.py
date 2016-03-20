#!/usr/bin/env python

import shutil
import sys
import os

from .install import kernels

def uninstall_kernelspecs(target_dir):
    for name, mod in kernels:
        kernel_dir = os.path.join(target_dir, "kernels", "cas" + mod)
        if os.path.exists(kernel_dir):
            try:
                shutil.rmtree(kernel_dir)
            except:
                print("Error: could not uninstall kernel `%s`." % name)
                continue

def unlink_sage_kernelspec(target_dir):
    kernels_dir = os.path.join(target_dir, "kernels")
    if not os.path.isdir(kernels_dir):
        return
    sage_target_kernel = os.path.join(kernels_dir, "sagemath")
    if os.path.exists(sage_target_kernel):
        try:
            os.remove(sage_target_kernel)
        except:
            print("Error: could not uninstall sage kernel.")
            return

def unlink_sage_nbextensions(target_dir):
    nbext_dir = os.path.join(target_dir, "nbextensions")
    if not os.path.isdir(nbext_dir):
        return
    for ext in [ "jsmol", "mathjax" ]:
        ext_target_dir = os.path.join(nbext_dir, ext)
        if os.path.exists(ext_target_dir):
            try:
                os.remove(ext_target_dir)
            except:
                print("Error: could not uninstall sage nbextension `%s'." % ext)
                continue

def main():
    if len(sys.argv) == 1:
        target_dir = os.path.join(
            os.path.expanduser("~"), 
            "Library", 
            "Jupyter")
    elif len(sys.argv) != 2:
        print("Error: wrong arguments.")
        return
    else:
        target_dir = sys.argv[1]
    if not os.path.isdir(target_dir):
        return
    uninstall_kernelspecs(target_dir)
    unlink_sage_kernelspec(target_dir)
    unlink_sage_nbextensions(target_dir)

if __name__ == "__main__":
    main()
