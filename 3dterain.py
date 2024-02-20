import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Generate sample terrain data (replace this with your own data)
terrain_data = np.random.rand(1000, 1000)  # Example 1000x1000 grid

# Downsample the data
downsample_factor = 10
downsampled_data = terrain_data[::downsample_factor, ::downsample_factor]

# Create meshgrid for downsampled x and y coordinates
x = np.arange(0, terrain_data.shape[0], downsample_factor)
y = np.arange(0, terrain_data.shape[1], downsample_factor)
X, Y = np.meshgrid(x, y)

# Create figure and 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot downsampled terrain surface
ax.plot_surface(X, Y, downsampled_data, cmap='terrain')

# Set labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Terrain Model (Downsampled)')

# Add grid
ax.grid(True)

# Add interactive controls for rotation and zoom
ax.view_init(elev=30, azim=45)  # Set initial viewpoint
plt.show()
