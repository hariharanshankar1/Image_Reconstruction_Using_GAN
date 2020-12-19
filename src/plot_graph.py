# The values in the list are taken after the model was run with 10 epochs.

# Importing various packages

import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# Plotting the graph for PSNR

train_psnr_list = [18.267, 19.559, 19.969, 20.536, 20.826, 21.198, 21.355, 21.515, 21.725, 21.721]
val_psnr_list = [22.687, 22.398, 22.458, 25.895, 22.284, 25.967, 24.066, 24.722, 26.563, 23.843]

plt.plot(range(1, 11), train_psnr_list, label = "Training PSNR")
plt.plot(range(1, 11), val_psnr_list, label = "Validation PSNR")
plt.xlabel("Epochs")
plt.ylabel("Peak signal-to-noise ratio")
plt.title("Epochs vs PSNR")
plt.ylim(0, 30)
plt.legend()
plt.show()


# Plotting the graph for SSIM

train_ssim_list = [0.701, 0.740, 0.750, 0.767, 0.773, 0.783, 0.789, 0.794, 0.800, 0.803]
val_ssim_list = [0.821, 0.824, 0.837, 0.860, 0.839, 0.871, 0.863, 0.872, 0.884, 0.885]

plt.plot(range(1, 11), train_ssim_list, label = "Training SSIM")
plt.plot(range(1, 11), val_ssim_list, label = "Validation SSIM")
plt.xlabel("Epochs")
plt.ylabel("Structural Similarity Index")
plt.title("Epochs vs SSIM")
plt.ylim(0.000, 1.000)
plt.legend()
plt.show()


# Plotting the graph for Error

train_error_list = [0.019, 0.0116, 0.010, 0.008, 0.008, 0.007, 0.007, 0.007, 0.006, 0.006]
val_error_list = [0.006, 0.005, 0.006, 0.003, 0.006, 0.003, 0.004, 0.002, 0.002, 0.004]

plt.plot(range(1, 11), train_error_list, label = "Training error")
plt.plot(range(1, 11), val_error_list, label = "Validation error")
plt.xlabel("Epochs")
plt.ylabel("Error")
plt.title("Epochs vs Error")
plt.ylim(0.0000, 0.0300)
plt.legend()
plt.show()
