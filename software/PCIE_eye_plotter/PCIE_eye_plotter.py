import matplotlib.pyplot as plt
import numpy as np


def plot_pcie_eye(data_matrix, title="PCIe Gen4 Lane 0 - In-System Eye Scan"):
    """
    Plots a heat map of PCIe eye margins.
    data_matrix: 2D array representing Bit Error Rate (BER) or hit counts.
    """
    # Using a logarithmic scale to highlight the 'open' part of the eye
    # 0 values (no errors) are set to a very small number for log visibility
    plot_data = np.where(data_matrix == 0, 1e-12, data_matrix)

    plt.figure(figsize=(10, 6))
    plt.imshow(np.log10(plot_data), cmap='viridis', aspect='auto',
               extent=[-0.5, 0.5, -255, 255])

    plt.colorbar(label='Log10(BER)')
    plt.title(title)
    plt.xlabel('Phase Offset (UI)')
    plt.ylabel('Voltage Offset (mV / Codes)')
    plt.grid(alpha=0.3)
    plt.show()


# Example: Simulated Eye Data (0 = clean, higher = more errors)
# In a real scenario, this would be parsed from a CSV or JTAG log
eye_grid = np.random.rand(64, 64)
# Create a 'clean' center (the eye opening)
eye_grid[20:44, 20:44] = 0

if __name__ == "__main__":
    plot_pcie_eye(eye_grid)

