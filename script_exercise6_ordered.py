#Yaml
import yaml
#JSON
import json

#Keep the order in the dictionary
from collections import OrderedDict


##############
##############
#Main Function
##############
##############

def main():
	my_cars_list = []
	my_cars_list.append({})
	my_cars_list[-1] = OrderedDict()
	my_cars_list[-1]['vendor'] = 'peugeot'
	my_cars_list[-1]['model'] = '508'
	my_cars_list[-1]['attribs'] = {}
	my_cars_list[-1]['attribs']['power_horse'] = '150'
	my_cars_list[-1]['attribs']['colour'] = 'red'

	my_cars_list.append({})
	my_cars_list[-1] = OrderedDict()
	my_cars_list[-1]['vendor'] = 'citroen'
	my_cars_list[-1]['model'] = 'ds5'
	my_cars_list[-1]['attribs'] = {}
	my_cars_list[-1]['attribs']['power_horse'] = '170'
	my_cars_list[-1]['attribs']['colour'] = 'grey'

	print'  Len of my list is:', len(my_cars_list)

	#output YAML file
	outputFile = file('./exercise6_ordered_output_yaml.yml', 'w') 
	outputFile.write('---\n')
	outputFile.write(yaml.dump(my_cars_list, default_flow_style = False))
	outputFile.close()

	#output JSON file
	outputFile = file('./exercise6_ordered_output_json.json', 'w') 
	json.dump(my_cars_list,outputFile)
	outputFile.close()

##############
#Main Program
##############

if __name__ == "__main__":
	print '\n## Script Automation Course: Exercise 6\n'
	main()
	print '\n## Script finished\n'

