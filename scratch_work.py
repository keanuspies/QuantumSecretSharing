### ALICE

alicepq = Program()
pq = Program()
ro = pq.declare('ro', 'BIT', 3)

alicepq = entangle(pq)

alicepq += X(ghz['alice'])
# alicepq += H(ghz['alice'])

alicepq = unentangle(alicepq)

alicepq += MEASURE(ghz['alice'], ro[0])
# rentangle the qubits
# alicepq = entangle(alicepq) 
wf = qvm.wavefunction(alicepq)
# plot_wf(wf)
print(wf)

### BOB

wrongpq = Program()
wrongpq += alicepq

wrongpq += H(ghz['bob'])
wrongpq += CNOT(ghz['bob'], ghz['charlie'])
# wrongpq = entangle(wrongpq, 'bob')
wrongpq += X(ghz['bob'])
# wrongpq = unentangle(wrongpq, 'alice')
wrongpq += CNOT(ghz['charlie'], ghz['bob'])
wrongpq += H(ghz['bob'])

wrongpq += MEASURE(ghz['bob'], ro[1])
# rentangle the qubits
wf = qvm.wavefunction(wrongpq)
print(wf)

### CHARLIE

cwrongpq = Program()
cwrongpq += wrongpq

# cwrongpq += H(ghz['charlie'])
# cwrongpq = entangle(cwrongpq, 'charlie')
cwrongpq += X(ghz['charlie'])
# cwrongpq = unentangle(cwrongpq, 'charlie')
# cwrongpq += H(ghz['charlie'])

# cwrongpq = unentangle(cwrongpq)
cwrongpq += MEASURE(ghz['charlie'], ro[2])

# cwrongpq = entangle(cwrongpq) 
wf = qvm.wavefunction(cwrongpq)
print(wf)
print(cwrongpq)