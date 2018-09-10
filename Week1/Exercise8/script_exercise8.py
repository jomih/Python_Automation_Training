
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

	crypto_sections = cisco_cfg.find_objects(r"^crypto map CRYPTO")
	#print 'Len of crypto_sections is', len(crypto_sections)
	
	for item in crypto_sections:
		print item.children

	print'\n'
	for index in range(0,len(crypto_sections)):
		print crypto_sections[index].text
		for item in crypto_sections[index].all_children:
			print item.text

	print'\n'

##############
#Main Program
##############

if __name__ == "__main__":
	print '\n## Script Automation Course: Exercise 8\n'
	main()
	print '\n## Script finished\n'

