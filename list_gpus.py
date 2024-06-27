# import tensorflow as tf
import torch

def list_gpus_tensorflow():
    gpus = tf.config.list_physical_devices('GPU')
    if gpus:
        print("GPUs available with TensorFlow:")
        for gpu in gpus:
            print(gpu)
    else:
        print("No GPUs available with TensorFlow.")

def list_gpus_pytorch():
    if torch.cuda.is_available():
        print("GPUs available with PyTorch:")
        for i in range(torch.cuda.device_count()):
            print(f"GPU {i}: {torch.cuda.get_device_name(i)}")
    else:
        print("No GPUs available with PyTorch.")

def main():
    # list_gpus_tensorflow()
    list_gpus_pytorch()

if __name__ == "__main__":
    main()
