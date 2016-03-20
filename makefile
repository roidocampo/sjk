
TARGET_DIR=${HOME}/Library/Jupyter

install:
	python -m cas_kernels.kernelspecs.install "${TARGET_DIR}"

uninstall:
	python -m cas_kernels.kernelspecs.uninstall "${TARGET_DIR}"
