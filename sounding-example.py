from arm_test_data import DATASETS
from matplotlib import pyplot as plt

import act

print("imports complete")

# Read data
filename_sonde = DATASETS.fetch('sgpsondewnpnC1.b1.20190101.053200.cdf')
print("data loaded")

ds = act.io.arm.read_arm_netcdf(filename_sonde)
print("data formatted")

# Plot enhanced Skew-T plot
display = act.plotting.SkewTDisplay(ds)
display.plot_enhanced_skewt(color_field='alt')

ds.close()
plt.savefig('sounding.png')
#plt.show()
