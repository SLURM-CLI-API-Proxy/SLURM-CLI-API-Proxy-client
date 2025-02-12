import yaml

class CliToJsonPayloadMappings():
    metadata: dict
    arguments_dict: dict
    arguments_list: list

    def __init__(self,yaml_config_path:str=None,config_mapping_dict:dict=None):
        """
        Initializes the CLI to JSON mapping object using one of two input: a YAML
        file (yaml_config_path) or its equivalent (in memory) given as a dictionary. If
        both are provided, only the YAML file is considered.
            
        Args:
            yaml_config_path (str): The file path to the YAML configuration file.
            config_mapping_dict(dict): A dictionary equivalent to the YAML config file.
            
        Attributes:
            metadata (dict): Metadata information from the YAML configuration.
            arguments_list (list): List of parameter mappings from the YAML configuration.
            arguments_dict (dict): Dictionary of parameter mappings with parameter names as keys.
        """
        if (yaml_config_path is not None):
            args_mappings:dict = yaml.safe_load(open(yaml_config_path))        
        elif (config_mapping_dict is not None):
            args_mappings = config_mapping_dict
        else:
            raise Exception("No configuration parameters provided.")

        self.metadata = args_mappings['mapping_meta']
        self.arguments_list = args_mappings['parameters']
        self.arguments_dict = {}

        for param in args_mappings['parameters']:
            self.arguments_dict[param['name']] = param  

