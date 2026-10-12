class iz_FloatSplitNode_01:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "value": (
                    "FLOAT",
                    {
                        "default": 1.0,
                        "min": 0.1,
                        "max": 100000.0,
                        "step": 0.1,
                        "round": 0.1,
                    },
                ),
            }
        }

    RETURN_TYPES = ("FLOAT", "STRING", "INT")
    RETURN_NAMES = ("float", "string", "int")
    FUNCTION = "iz_split_float_01"
    CATEGORY = "IZmake/tools"

    def iz_split_float_01(self, value):
        float_val = float(value)
        int_val = int(value)
        str_val = f"{float_val:g}"

        return (float_val, str_val, int_val)


NODE_CLASS_MAPPINGS = {
    "iz_float_split_01": iz_FloatSplitNode_01,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "iz_float_split_01": "iz float Split 0.1",
}
