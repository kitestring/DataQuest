import os.path
import json
import fileinput


class JSON_Tools():
		
	def dump_Data_To_File(self, dict_file_path, **kwargs):
		# Converts a Python dictionary to JSON formatted data and writes it to file
		all_dicts = {}
		
		if kwargs != None:
			for key, value in kwargs.items():
				all_dicts[key] = value
		
			with open(dict_file_path, 'w') as outfile:
				json.dump(all_dicts, outfile)
				outfile.close()
				
	def Load_Data(self, dict_file_path):
		# Converts a JSON formatted file to a Python dictionary
		with open(dict_file_path) as json_data:
			return json.load(json_data)
		
	def Parce_Data(self, json_data):
		pass
# 		key_list = []
# 		for key, value in json_data.items():
# 			key_list.append(key)
		
		return json_data['factTableColumns'], json_data['analyteTableColumns'], json_data['analyteNameDict'], json_data['chromatographyDict']
		
	def toString(self, loaded_json_data):
		pass
# 		return json.dumps(loaded_json_data, indent=4, sort_keys=True)