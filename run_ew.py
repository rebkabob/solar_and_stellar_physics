import numpy as np
import matplotlib.pyplot as plt
import h5py
import matplotlib as mpl


mpl.rcParams['font.size'] = 16
mpl.rcParams['image.cmap']="Greys_r" 
mpl.rcParams['image.origin']= "lower"

sst4 = h5py.File("/mn/stornext/d19/RoCS/svenwe/lecture/AST5770/data/obssun_sst4/obssun_sst4.h5", "r")
sst4.keys()

intensity = sst4["intensity"][:]
wavelength = sst4["wavelength"][:]
time = sst4["time"][:]
time_s = sst4["time_s"][:]
x = sst4["x"][:]
y = sst4["y"][:]

xy_A_min = 394; xy_A_max = 480
xy_B_min = 118; xy_B_max = 204

x_subfield_A = sst4["x"][xy_A_min:xy_A_max]; y_subfield_A = sst4["y"][xy_A_min:xy_A_max]
subfield_A = sst4["intensity"][:, :, xy_A_min:xy_A_max, xy_A_min:xy_A_max]

x_subfield_B = sst4["x"][xy_B_min:xy_B_max]; y_subfield_B = sst4["y"][xy_B_min:xy_B_max]
subfield_B = sst4["intensity"][:, :, xy_B_min:xy_B_max, xy_B_min:xy_B_max]

doppler_cube_A = np.load("doppler_cube_A.npy")
doppler_cube_B = np.load("doppler_cube_B.npy")

ew_cube_A = np.load("ew_cube_A.npy")
ew_cube_B = np.load("ew_cube_B.npy")

data = subfield_A
for t in range(time.size):
    fig, ax = plt.subplots(figsize = (8, 6))
    print(f"Time step: {t}")
    for x_idx in range(data.shape[3]):
        for y_idx in range(data.shape[2]):
            print(f"Pixel ({x_idx}, {y_idx})")
            ax.scatter(ew_cube_A[t, y_idx, x_idx], doppler_cube_A[t, y_idx, x_idx], alpha = .1, color = "hotpink")

    ax.set_title(f't[{t}]={time_s[t]: .3f} s')
    ax.set_xlabel("Equivalent width [m$\AA$]")
    ax.set_ylabel("Doppler velocity [km/s]")
    ax.set_xlim(np.min(ew_cube_A), np.max(ew_cube_A))
    ax.set_ylim(np.min(doppler_cube_A), np.max(doppler_cube_A))
    plt.savefig(f"figures/ew_doppler_A/ew_doppler_A_{t:04d}.png")

for t in range(time.size):
    fig, ax = plt.subplots(figsize = (8, 6))
    print(f"Time step: {t}")
    for x_idx in range(data.shape[3]):
        for y_idx in range(data.shape[2]):
            print(f"Pixel ({x_idx}, {y_idx})")
            ax.scatter(ew_cube_B[t, y_idx, x_idx], doppler_cube_B[t, y_idx, x_idx], alpha = .1, color = "hotpink")

    ax.set_title(f't[{t}]={time_s[t]: .3f} s')
    ax.set_xlabel("Equivalent width [m$\AA$]")
    ax.set_ylabel("Doppler velocity [km/s]")
    ax.set_xlim(np.min(ew_cube_B), np.max(ew_cube_B))
    ax.set_ylim(np.min(doppler_cube_B), np.max(doppler_cube_B))
    plt.savefig(f"figures/ew_doppler_B/ew_doppler_B_{t:04d}.png")