from groq import Groq
def rta(a):
    client = Groq(api_key="gsk")
    completion = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
        {
            "role": "information",
            "content": "Eres un investigador de la proteccion ecologica, tu tarea es que con el material que te den, le digas al usuario como puede ayudar al planeta. La idea es que sea en menos de un parrafo, lo mas resumido que puedas"
        } , 
            
        {
            "role": "user",
            "content": a
        }
        ],
        temperature=1,
        max_completion_tokens=2048,
        top_p=1,
        reasoning_effort="medium",
        stream=True,
        stop=None
    )

    return completion.choices[0].message_content
