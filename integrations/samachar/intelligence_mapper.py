def convert_to_svacs(data):

    intelligence = data.get("intelligence", {})

    confidence_obj = intelligence.get("confidence", {})

    score = confidence_obj.get("score", 0)

    confidence = score / 100

    return {

        "entities": intelligence.get("validated_entities", {}),

        "classification": intelligence.get("classification", {}),

        "confidence": confidence,

        "confidence_summary": confidence_obj.get("summary", ""),

        "processing_trace": intelligence.get("processing_trace", {}),

        "evidence": intelligence.get("evidence", {}),

        "reasoning": intelligence.get("classification", {}).get(
            "classification_explanation", ""
        )
    }
