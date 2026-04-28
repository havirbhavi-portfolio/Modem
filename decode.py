import numpy as np
from scipy.io import wavfile

fs, x = wavfile.read("message.wav")
x = x.astype(np.float32) / 32768.0

BIT_N = 160
FRAME_N = 1600

t = np.arange(BIT_N)

f0 = 2025
f1 = 2225

c0 = np.cos(2*np.pi*f0*t/fs)
s0 = np.sin(2*np.pi*f0*t/fs)

c1 = np.cos(2*np.pi*f1*t/fs)
s1 = np.sin(2*np.pi*f1*t/fs)

def power(block, c, s):
    I = np.dot(block, c)
    Q = np.dot(block, s)
    return I*I + Q*Q

bits = []

# STEP 1: decode bits
for i in range(0, len(x), BIT_N):
    block = x[i:i+BIT_N]
    if len(block) < BIT_N:
        break

    p0 = power(block, c0, s0)
    p1 = power(block, c1, s1)

    bits.append(1 if p1 > p0 else 0)

# STEP 2: decode bytes
msg = []

for i in range(0, len(bits), 10):
    frame = bits[i:i+10]
    if len(frame) < 10:
        break

    start = frame[0]
    stop = frame[9]
    data = frame[1:9]

    if start != 0 or stop != 1:
        continue

    val = 0
    for j, b in enumerate(data):
        val |= (b << j)   # LSB first

    msg.append(val)

text = ''.join(chr(c) for c in msg)
print("Decoded message:")
print(text)

with open("message.txt", "w") as f:
    f.write(text)