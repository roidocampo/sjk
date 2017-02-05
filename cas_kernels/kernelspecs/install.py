#!/usr/bin/env python

import shutil
import sys
import os

kernelspec_template = """
{{
    "display_name": "{kernel_name}",
    "argv": [
        "{python_exec}",
        "-m", "cas_kernels.{module_name}", 
        "-f", "{{connection_file}}"
    ],
    "env": {{
        "PYTHONPATH": "{python_path}"
    }}
}}
"""

kernels = [
    ("Singular",    "singular"),
    ("Macaulay 2",  "macaulay2"),
    ("GAP",         "gap"),
    ("Risa/Asir",   "asir"),
    ("Mathematica", "mathematica"),
]

def install_kernelspecs(target_dir, python_path):
    image_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images")
    for name, mod in kernels:
        kernel_dir = os.path.join(target_dir, "kernels", "cas" + mod)
        if os.path.exists(kernel_dir):
            try:
                shutil.rmtree(kernel_dir)
            except:
                print("Error: cannot install kernel `%s`." % name)
                continue
        try: 
            os.makedirs(kernel_dir)
        except OSError:
            if not os.path.isdir(kernel_dir):
                print("Error: cannot install kernel `%s`." % name)
                continue
        kernel_file = os.path.join(kernel_dir, "kernel.json")
        with open(kernel_file, "w") as fo:
            fo.write(kernelspec_template.format(
                kernel_name = name,
                module_name = mod,
                python_exec = sys.executable,
                python_path = python_path
            ))
        for ext in [ "-128x128.png", "-64x64.png"]:
            orig_image = os.path.join(image_dir, mod+ext)
            if os.path.exists(orig_image):
                target_image = os.path.join(kernel_dir, "logo"+ext)
                shutil.copy(orig_image, target_image)

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
    install_kernelspecs(target_dir, python_path)

if __name__ == "__main__":
    main()
