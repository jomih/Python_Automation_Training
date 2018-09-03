
#Cisco parser
from ciscoconfparse import CiscoConfParse


##############
##############
#Main Function
##############
##############

def main():

	#YAML file
	cisco_cfg = CiscoConfParse("./cisco_file.txt")

	transform_set = cisco_cfg.find_objects(r"^crypto ipsec transform-set")
	t_set_list = []
	for t_set in transform_set:
		if ('esp-aes' not in t_set.text):
			t_set_list.append(t_set.text)

	print 'Transform sets found without AES are:', t_set_list

	print '\nCrypto Maps without AES are:\n'

	for t_set in t_set_list:
		var_tmp1 = t_set.split()
		reference = var_tmp1[3].strip()
		#print 'reference es', reference
		var_tmp1 = cisco_cfg.find_objects_w_child(r"^crypto map ", reference)
		#print 'var_tmp1 es', var_tmp1[0].text

		for index in range(0, len(var_tmp1)):
			config_crypto_map = cisco_cfg.find_children(var_tmp1[index].text)
			for item in config_crypto_map:
				print ' ', item


##############
#Main Program
##############

if __name__ == "__main__":
	print '\n## Script Automation Course: Exercise 10\n'
	main()
	print '\n## Script finished\n'

