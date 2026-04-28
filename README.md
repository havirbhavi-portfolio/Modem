Havirbhavi Pothugunta

Bell 103 Modem Decoder

This program decodes an audio signal encoded using Bell 103 FSK at 300 baud.

Approach:
- The audio is divided into 160-sample blocks (1 bit).
- For each block, power is computed at 2025 Hz and 2225 Hz using I/Q correlation.
- The higher power determines the bit value.
- Bits are grouped into 10-bit frames (start, 8 data bits, stop).
- Data bits are decoded in LSB-first order to form ASCII characters.

Result:
"You will be aided greatly by a person whom you thought to be unimportant."

Challenges:
- Ensuring correct bit alignment
- Handling LSB-first decoding
- Validating start and stop bits
