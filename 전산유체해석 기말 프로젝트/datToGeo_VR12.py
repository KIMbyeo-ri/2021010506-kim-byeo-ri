import numpy as np

dat_file = "vr-12.dat"         
geo_file = "vr12_airfoil.geo" 

with open(dat_file, "r") as f:
    title = f.readline()              # "BOEING-VERTOL VR-12 AIRFOIL"
    counts_line = f.readline()        # "       43.       41."
    parts = counts_line.split()
    n_top = int(float(parts[0]))      # 43
    n_bottom = int(float(parts[1]))   # 41

data = np.loadtxt(dat_file, skiprows=3)

top = data[:n_top]        # 상부: LE -> TE
bottom = data[n_top:]     # 하부: LE -> TE

top_rev = top[::-1]

with open(geo_file, "w") as f:
    
    for i, (x, y) in enumerate(coords, start=1):
        f.write(f"Point({i}) = {{{x:.8f}, {y:.8f}, 0}};\n")

    n = len(coords)
    idx_list = ", ".join(str(i) for i in range(1, n + 1))
    f.write(f"Spline(1) = {{{idx_list}, 1}};\n")

    f.write("Line Loop(1) = {1};\n")
    f.write("Plane Surface(1) = {1};\n")

print(f"생성 완료: {geo_file}")
