text = "X-DSPAM-Confidence:    0.8475"
zero_pos = text.find("0")

number = text[zero_pos:]
print float(number)