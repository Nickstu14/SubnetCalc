import sys

#will return the binary value
def BinaryConversion(octet):
	return format(octet,'08b') #bin(octet)

#Menu driven system function to hold all Menu text
def Menu(_SwitchVal, _min, _max):
	print ("\n\n---MENU---")
	#Menu text below
	m_Switcher = {
		1: "Calculate: \n    1.Network\n    2.Host"
	}

	print(m_Switcher.get(_SwitchVal, "\nMenu Invalid ")) #if a menu is called that does't exitst it will print and return menu invalid.
	
	if(int(_SwitchVal) > len(m_Switcher)): #if menu that is called is greater than the size of the list then return empty
		return

	return IntCheck(_min, _max)


#input validation for int's
def IntCheck(_min, _max):
	m_Val = -1

	while int(m_Val) != 0:
		m_Val = input("\nPlease enter value:")

		if ((int(m_Val) > _max) or (int(m_Val) < _min)):
			print("\nPlease choose a value between: ", _min, " or ", _max, "\nOr press 0 to exit")
		else:
			return m_Val

def Network():
	m_I = 0
def Host():
	m_I = 0

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

m_Bin = list()

for octet in m_IpSplit:
	m_Bin.append(BinaryConversion(int(octet)))


#debug
print('Binary:' ,m_Bin[0],'.',m_Bin[1],'.',m_Bin[2],'.',m_Bin[3])

m_MenuChose = Menu (1,1,2)

if int(m_MenuChose )== 1:
	#Network
	Network()
elif int(m_MenuChose )== 2:
	#Host
	Host()
else:
	exit()