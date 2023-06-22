import pandas as pd
import matplotlib.pyplot as plt

latency = []
RSSI = []
fading = []
noise = []
time = []
tot_atten = []

df = pd.read_csv(r'rf_coe_records.csv')
print(df)
df = df.dropna()
data = pd.DataFrame(df,columns=['latency','RSSI','attn1','attn2'])
data_list = data.values.tolist()

for t in range(0,680):
    time.append(t * 0.15)

for i in data_list:
    latency_intval = (i[0])
    RSSI_intval = (i[1])
    fading_intval = (i[2])
    noise_intval = (i[3])
    latency.append(latency_intval)
    RSSI.append(RSSI_intval)
    fading.append(fading_intval)
    noise.append(noise_intval)
    tot_atten.append(fading_intval )

plt.figure(1)
plt.plot(time, latency)
plt.title("Latency vs Time")
plt.ylabel("Latency (Buffer Size)")
plt.xlabel("Time (Seconds)")

plt.figure(2)
plt.plot(time, RSSI)
plt.title("RSSI vs Time")
plt.ylabel("RSSI (dB)")
plt.xlabel("Time (Seconds)")

plt.figure(3)
plt.plot(time,fading)
plt.title("Fading vs Time")
plt.ylabel("Fading (dB)")
plt.xlabel("Time (Seconds)")

plt.figure(4)
plt.scatter(latency, RSSI)
plt.title("Latency vs RSSI")
plt.xlabel("Latency (Buffer Size)")
plt.ylabel("RSSI (dB)")

fig = plt.figure(figsize=(7,7))
ax = fig.add_subplot(projection='3d')
ax.scatter(latency,RSSI,tot_atten)
ax.set_xlabel("Latency (Buffer Size)")
ax.set_ylabel("RSSI (dB)")
ax.set_zlabel("Total Attenuation (dB)")

plt.show()
