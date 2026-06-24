import json


def parse_json(llm_output):

    try:

        start = llm_output.find("{")
        end = llm_output.rfind("}") + 1

        json_text = llm_output[start:end]

        data = json.loads(json_text)

        return data

    except Exception:

        return {}