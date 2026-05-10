from app.retrieval import search_assessments

def handle_chat(messages):

    latest_message = messages[-1]["content"]

    if len(latest_message.split()) < 4:

        return {
            "reply": "Please specify role, skills, and experience level.",
            "recommendations": [],
            "end_of_conversation": False
        }

    recommendations = search_assessments(
        latest_message,
        top_k=5
    )

    formatted = []

    for rec in recommendations:

        formatted.append({
            "name": rec["name"],
            "url": rec["url"],
            "test_type": "Unknown"
        })

    return {
        "reply": "Here are recommended SHL assessments.",
        "recommendations": formatted,
        "end_of_conversation": False
    }