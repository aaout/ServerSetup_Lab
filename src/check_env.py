import torch
import matplotlib as plt
import pandas as pd
import cv2 as cv

if __name__ == "__main__":
    if torch.cuda.is_available():
        print("GPU environment")
        print(f"is_available: {torch.cuda.is_available()} ")
        print(f"device_count: {torch.cuda.device_count()} ")
        print(f"GPU name: {torch.cuda.get_device_name()} ")
        print(f"device_capability: {torch.cuda.get_device_capability()} ")
    else:
        print("CPU environment")

    print("")
    print("Pachage")
    print(f"PyTorch: {torch.__version__} ")
    print(f"Pandas: {pd.__version__} ")
    print(f"OpenCV: {cv.__version__} ")
    print(f"Matplotlib: {plt.__version__} ")
