class iz_FloatSplitNode_05:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "value": (
                    "FLOAT",
                    {
                        "default": 1.0,
                        "min": 0.5,
                        "max": 100000.0,
                        "step": 0.5,
                        "round": 0.5,
                    },
                ),
            }
        }

    RETURN_TYPES = ("FLOAT", "STRING", "INT")
    RETURN_NAMES = ("float", "string", "int")
    FUNCTION = "iz_split_float_05"
    CATEGORY = "IZmake/tools"

    def iz_split_float_05(self, value):
        float_val = float(value)
        int_val = int(value)
        str_val = f"{float_val:g}"

        return (float_val, str_val, int_val)


NODE_CLASS_MAPPINGS = {
    "iz_float_split_05": iz_FloatSplitNode_05,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "iz_float_split_05": "iz float Split 0.5",
}
