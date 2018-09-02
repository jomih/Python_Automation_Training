
#Yaml
import yaml
#JSON
import json


##############
##############
#Main Function
##############
##############

def main():

	#YAML file
	inputFile = file('./exercise6_output_yaml.yml', 'r') 
	new_list = yaml.load (inputFile)
	inputFile.close()

	print 'YAML file is as follows:\n', new_list
        print '\nYAML condensed file is as follows:\n', yaml.dump(new_list, default_flow_style = True)
	print '\nYAML expanded file is as follows:\n', yaml.dump(new_list, default_flow_style = False)

	print '\n\n'

	#JSON file
	inputFile = file('./exercise6_output_json.json', 'r') 
	new_list = json.load (inputFile)
	inputFile.close()

	print 'JSON file is as follows:\n', new_list


##############
#Main Program
##############

if __name__ == "__main__":
	print '\n## Script Automation Course: Exercise 7\n'
	main()
	print '\n## Script finished\n'

