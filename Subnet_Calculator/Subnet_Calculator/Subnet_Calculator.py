import sys

#will return the binary value
def BinaryConversion(octet):
	return format(octet,'08b') #bin(octet)
def DebugPrint(_val):
	print(_val)


#Ask for input
m_Starting_IP = input("Starting Ip: ")
m_Slash = input("/")

#debug print of full IP
print(m_Starting_IP + " /" + m_Slash)

#Split up the IP into 4 vales
m_IpSplit = m_Starting_IP.split('.')

#debug print
DebugPrint(m_IpSplit)


m_Octet = int(m_Slash) / 8 #Calculate how many octets are full
m_Networkbit = int(m_Slash) % 8 #calculate how many bits left
m_HostBits = 8 - int(m_Networkbit)

DebugPrint(int(m_Octet) + 'octets & ' + m_Networkbit + 'bits in octet' + int(m_Octet) + 1 + ' with ' + m_HostBits + 'bits left for the host')

m_Bin = []

for octet in m_IpSplit:
	m_Bin.append(BinaryConversion(int(octet)))

#m_Bin =
#[binaryConversion(int(m_StringSplit[0])),binaryConversion(int(m_StringSplit[1])),binaryConversion(int(m_StringSplit[2])),binaryConversion(int(m_StringSplit[3]))]

#debug
DebugPrint('Binary:' ,m_Bin[0],'.',m_Bin[1],'.',m_Bin[2],'.',m_Bin[3])


