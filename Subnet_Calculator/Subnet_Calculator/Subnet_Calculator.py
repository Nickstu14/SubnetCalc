import sys

#will return the binary value
def BinaryConversion(octet):
	return format(octet,'08b') #bin(octet)


#Ask for input
m_Starting_IP = input("Starting Ip: ")
m_Slash = input("/")

#debug print of full IP
print(m_Starting_IP + " /" + m_Slash)

#Split up the IP into 4 vales
m_IpSplit = m_Starting_IP.split('.')

#debug print
print(m_IpSplit)


m_Octet = int(m_Slash) / 8 #Calculate how many octets are full
m_Networkbit = int(m_Slash) % 8 #calculate how many bits left
m_HostBits = 8 - int(m_Networkbit)

print(int(m_Octet), 'octets & ', m_Networkbit, 'bits in octet', int(m_Octet) + 1, ' with ', m_HostBits, 'bits left for the host')

m_Bin = []

for octet in m_IpSplit:
	m_Bin.append(BinaryConversion(int(octet)))


#debug
print('Binary:' ,m_Bin[0],'.',m_Bin[1],'.',m_Bin[2],'.',m_Bin[3])

m_J = 0
