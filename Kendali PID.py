import numpy as np
import control as ct
import matplotlib.pyplot as plt

#1a
num = [1, 20]
den = [1, 19, 80, -100]
G = ct.TransferFunction(num, den)
plt.figure()
ct.nyquist_plot(G)
plt.title("Nyquist Plot")
plt.grid(True)
plt.show()

#1b
Kcr = ct.db2mag(64.2)
wg = 41.2
Pcr = (2 * np.pi) / wg
print("Kcr: ", Kcr)
print("Pcr: ", Pcr)

#1c
s = ct.TransferFunction.s
Kp = 0.6 * Kcr
Td = 0.125 * Pcr
Gc = Kp*(1 + Td * s)
G = ct.TransferFunction(num, den)
G_cl = ct.feedback(Gc * G, 1)
t, y = ct.step_response(G_cl)
plt.figure()
plt.plot(t, y)
plt.title("Step Response Sistem Kendali PD")
plt.xlabel("Waktu (s)")
plt.ylabel("Amplitudo")
plt.grid()
plt.show()

#1d
s = ct.TransferFunction.s
Kp = 0.45 * Kcr
Ti = Pcr / 1.2
Gc = Kp*(1 + 1 / (Ti * s))
G = ct.TransferFunction(num, den)
G_cl = ct.feedback(Gc * G, 1)
t, y = ct.step_response(G_cl)
plt.figure()
plt.plot(t, y)
plt.title("Step Response Sistem Kendali PI")
plt.xlabel("Waktu (s)")
plt.ylabel("Amplitudo")
plt.grid()
plt.show()

#1e
s = ct.TransferFunction.s
Kp = 0.6 * Kcr
Ti = 0.5 * Pcr
Td = 0.125 * Pcr
Gc = Kp*(1 + 1 / (Ti * s) + Td * s)
G = ct.TransferFunction(num, den)
G_cl = ct.feedback(Gc * G, 1)
t, y = ct.step_response(G_cl)
plt.figure()
plt.plot(t, y)
plt.title("Step Response Sistem Kendali PID")
plt.xlabel("Waktu (s)")
plt.ylabel("Amplitudo")
plt.grid()
plt.show()

#2g
num = [18, 360]
den = [1, 3, -18]
G = ct.TransferFunction(num, den)
plt.figure()
ct.nyquist_plot(G)
plt.title("Nyquist Plot")
plt.grid(True)
plt.show()

#2h
Kcr = ct.db2mag(-26)
wg = 22.9
Pcr = (2 * np.pi) / wg
print("Kcr: ", Kcr)
print("Pcr: ", Pcr)

#2i
s = ct.TransferFunction.s
Kp = 0.6 * Kcr
Td = 0.125 * Pcr
Gc = Kp*(1 + Td * s)
G = ct.TransferFunction(num, den)
G_cl = ct.feedback(Gc * G, 1)
t, y = ct.step_response(G_cl)
plt.figure()
plt.plot(t, y)
plt.title("Step Response Sistem Kendali PD")
plt.xlabel("Waktu (s)")
plt.ylabel("Amplitudo")
plt.grid()
plt.show()

#2j
s = ct.TransferFunction.s
Kp = 0.45 * Kcr
Ti = Pcr / 1.2
Gc = Kp*(1 + 1 / (Ti * s))
G = ct.TransferFunction(num, den)
G_cl = ct.feedback(Gc * G, 1)
t, y = ct.step_response(G_cl)
plt.figure()
plt.plot(t, y)
plt.title("Step Response Sistem Kendali PI")
plt.xlabel("Waktu (s)")
plt.ylabel("Amplitudo")
plt.grid()
plt.show()

#2k
s = ct.TransferFunction.s
Kp = 0.6 * Kcr
Ti = 0.5 * Pcr
Td = 0.125 * Pcr
Gc = Kp*(1 + 1 / (Ti * s) + Td * s)
G = ct.TransferFunction(num, den)
G_cl = ct.feedback(Gc * G, 1)
t, y = ct.step_response(G_cl)
plt.figure()
plt.plot(t, y)
plt.title("Step Response Sistem Kendali PID")
plt.xlabel("Waktu (s)")
plt.ylabel("Amplitudo")
plt.grid()
plt.show()