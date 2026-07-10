def convert_to_svacs(data):

    intelligence = data.get("intelligence", {})

    return {

        "entities": intelligence.get("validated_entities", {}),

        "classification": intelligence.get("classification", {}),

        "confidence": intelligence.get("confidence", {}),

        "processing_trace": intelligence.get("processing_trace", {}),

        "evidence": intelligence.get("evidence", {})

    }
