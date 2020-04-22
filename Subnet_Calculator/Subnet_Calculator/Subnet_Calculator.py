import sys



#Menu driven system function to hold all Menu text
def Menu(_SwitchVal, _min, _max):
	print("\n\n---MENU---")
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

#calc CIDR Notation from subnet
def CalcCIDRNotation(_val):
	m_I = 0

#calc subnet from CIDR Notation
def CalcSubnetMask(_val):
	m_Octet = int(int(_val.c_IPCIDR) / 8) #Calculate how many octets are full
	m_Networkbit = int(_val.c_IPCIDR) % 8 #calculate how many bits left
	_val.c_HostBits = 8 - int(m_Networkbit)

#calc binary value for both IP and subnetmask
def CalcBinary(_val):
	m_I = 0

def BinaryConversion(octet):
	return format(octet,'08b') #bin(octet)

#Calculate breakdown after asking how many networks
def Network():
	m_I = 0

#calcualte breakdown after asking how many hosts
def Host():
	m_I = 0

class IPInfo:
	c_IPAddress = list()
	c_IPAddressBinary = list()
	c_IPSubnet = list()
	c_IPSubnetBinary = list()
	
	c_HostBits = int(0)
	c_IPCIDR = int(0)

#-------------MAIN-------------------

#class to hold IP information
m_IP = IPInfo()


#Ask for input
m_Starting_IP = input("Starting Ip: ")

#if there is a "/" in the IP address then take the remaining number and
#calculate the CIDR notation
#if the size of the array is 8 then there is a subnet version
m_IpSplit = m_Starting_IP.split('.')


# if the input has a / 
if m_Starting_IP.find('/') != -1: #found
	m_CIDRSplit = m_Starting_IP.split('/')
	m_IP.c_IPCIDR = m_CIDRSplit[len(m_CIDRSplit) - 1]

	for val in m_IpSplit:
		if val.find('/')!= -1:
			m_TempSplit = val.split('/')
			m_IP.c_IPAddress.append(m_TempSplit[0])
		else:
			m_IP.c_IPAddress.append(val)

	CalcSubnetMask(m_IP)

#if the input doesnt have a / and is longer than 4 segments
elif len(m_IpSplit) > 4:
	m_Subnet = list()
	for m_Sub in m_IpSplit[3:]:
		if m_Sub.find(' ') != -1: #found
			m_TempSub = m_Sub.split(' ')
			m_Subnet.append(m_TempSub[len(m_TempSub) - 1])
		else:
			m_Subnet.append(m_Sub)
	CalcCIDRNotation(m_IP)

else:
	m_InputVal = input("Please type in Subnet mask or CIDR notation: ")


#m_Slash = input("/")

#debug print of full IP
#print(m_Starting_IP + " /" + m_Slash) #cidr

#Split up the IP into 4 vales





print(int(m_Octet), 'octets & ', m_Networkbit, 'bits in octet', int(m_Octet) + 1, ' with ', m_HostBits, 'bits left for the host')

m_Bin = list()

for octet in m_IpSplit:
	m_Bin.append(BinaryConversion(int(octet)))


#debug
print('Binary:' ,m_Bin[0],'.',m_Bin[1],'.',m_Bin[2],'.',m_Bin[3])

m_MenuChose = Menu(1,1,2)

if int(m_MenuChose) == 1:
	#Network
	Network()
elif int(m_MenuChose) == 2:
	#Host
	Host()
else:
	exit()