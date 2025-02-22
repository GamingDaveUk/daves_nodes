
class davesTextToList:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required":{
                "multiline_text": ("STRING", {"multiline": True, "default": "text"}),
                "delimiter": ("STRING", {"default": "<split>"}),
                "remove_empty": ("BOOLEAN", {"default": False}),
            }
        }
    
    RETURN_TYPES = ("STRING", )
    RETURN_NAMES = ("list Out", )
    OUTPUT_IS_LIST = (True,)
    FUNCTION = "toList"
    CATAGORY = "Daves"
    DESCRIPTION = "Converts a multiline text to a list"

    def toList(self, multiline_text, delimiter, remove_empty):
        if not multiline_text:
            return ([],)  # Ensure return is always a tuple
        
        # First, split the text into a list of strings
        split_list = multiline_text.split(delimiter)

        # Process each line: strip whitespace, and optionally remove empty ones
        processed_list = [line.strip() for line in split_list if not remove_empty or line.strip()]

        return (processed_list,)  # ComfyUI requires a tuple

# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "davesTextToList": davesTextToList,
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "davesTextToList": "Daves Text To List"
}