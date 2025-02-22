from .comfyui_davesTextToList import davesTextToList

NODE_CLASS_MAPPINGS = {
    "davesTextToList": davesTextToList
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "davesTextToList": "Daves Text To List"
}

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]