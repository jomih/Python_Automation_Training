
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

	print 'One way of doing it: find_parents_w_child'
	crypto_w_pfs2 = cisco_cfg.find_parents_w_child(r"^crypto map ", r"set pfs group2") 
	print ' Result is type:', type(crypto_w_pfs2)
	print ' crypto_w_pfs2 is:', crypto_w_pfs2
	for item in crypto_w_pfs2:
		print ' ', item


	print '\nA different way of doing it:find_objects_w_child'
	crypto_w_pfs2 = cisco_cfg.find_objects_w_child(r"^crypto map ", r"set pfs group2") 
	print ' Result is type:', type(crypto_w_pfs2)
	print ' crypto_w_pfs2 is:', crypto_w_pfs2
	for item in crypto_w_pfs2:
		print ' ', item.text


##############
#Main Program
##############

if __name__ == "__main__":
	print '\n## Script Automation Course: Exercise 9\n'
	main()
	print '\n## Script finished\n'

