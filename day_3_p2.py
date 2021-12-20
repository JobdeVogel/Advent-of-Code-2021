'''
gamma_rate: most common in columns
epshilon_rate: least common in rows
'''

import numpy as np

oxygen = []
scrubber = []

# Extract data from file
data = []
with open('day_3_data.txt') as f:
    for line in f:
        data.append(list(line)[:12])

# Convert to numpy data
np_data = np.array(data, dtype=np.int8)

# Flip matrix
np_data = np_data.T
oxygen_data = np.copy(np_data)
scrubber_data = np.copy(np_data)

for position in range(1):
    column_oxyg = oxygen_data[position]
    column_scrub = scrubber_data[position]
    
    if column_oxyg.shape == (0,):
        oxygen.append('0')

    elif column_oxyg.shape == (1,):
        oxygen.append(str(oxygen_data[position][0]))
        oxygen_data = np.delete(oxygen_data, 0, 1)

    else:
        oxyg_max = np.bincount(column_oxyg).argmax()
        oxyg_min = np.bincount(column_oxyg).argmin()
      
        min_oxyg_pos = np.where(column_oxyg == oxyg_min)
        
        #print(oxyg_max)
        #print(oxygen_data)
        #print(min_oxyg_pos)
        
        if oxyg_max == oxyg_min:
            oxygen.append('1')
        else:
            oxygen.append(str(oxyg_max))
        
        print(oxygen_data)
        print("\n")
        oxygen_data = np.delete(oxygen_data, min_oxyg_pos, 1)
        print(oxygen_data)
    
    if column_scrub.size == 0:
        scrubber.append('0')

    elif column_scrub.size == 1:
        scrubber.append(str(scrubber_data[position][0]))
        scrubber_data = np.delete(scrubber_data, 0, 1)

    else:
        scrub_max = np.bincount(column_scrub).argmax()
        scrub_min = np.bincount(column_scrub).argmin()

        max_scrub_pos = np.where(column_scrub == scrub_max)
        
        if scrub_max == scrub_min:
            scrubber.append('0')
        else:
            scrubber.append(str(scrub_min))
        
        scrubber_data = np.delete(scrubber_data, max_scrub_pos, 1)

print(oxygen)
print(scrubber)

oxygen = int(str(''.join(oxygen)), 2)
scrubber = int(str(''.join(scrubber)), 2)

print(oxygen)
print(scrubber)

res = oxygen * scrubber
print(res)