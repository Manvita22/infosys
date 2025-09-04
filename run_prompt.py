# To run this code you need to install the following dependencies:
# pip install google-genai


# # To run this code you need to install the following dependencies:
# # pip install google-genai

# import base64
# import os
# from google import genai
# from google.genai import types


# GEMINI_API_KEY="AIzaSyCAAb6uwoCG-yvedBqze6sppF62d6GHQbA"

# def execute_gemini(prompt):
#     client = genai.Client(
#         api_key=GEMINI_API_KEY,
#     )

#     model = "gemini-2.5-flash-lite"
#     contents = [
#         # types.Content( # system prompt
#         #     role="system",
#         #     parts=[
#         #         types.Part.from_text(text=
#         #         """Make Text Summarization like social media marketing"""
#         #         ),
#         #     ],
#         # ),
#         types.Content( # user prompt (same as chat input)
#             role="user",
#             parts=[
#                 types.Part.from_text(text=prompt),
#             ],
#         ),
#     ]
#     tools = [
#         # this will attach google results to the llm output
#         types.Tool(googleSearch=types.GoogleSearch()),
#     ]
#     generate_content_config = types.GenerateContentConfig(
#         thinking_config = types.ThinkingConfig(
#             thinking_budget=-1,
#         ),
#         tools=tools,
#     )

#     result = client.models.generate_content(
#         model=model,
#         contents=contents,
#         config=generate_content_config,
#     )

#     return result.text

# if __name__ == "__main__":

#     bunch_of_prompts = [
#         "How many a are there in apple ?",
#         "How many p are there in apple ?",
#         "How many l are there in apple ?",
#     ]

#     for the_prompt in bunch_of_prompts:
#         out = execute_gemini(prompt=the_prompt)
#         print(out)



import base64
import os
from google import genai
from google.genai import types

GEMINI_API_KEY="AIzaSyBD0IMoue8bUXotzPY3z3SzBrcXf5R1Vwo"

# def execute_gemini(prompt):
#     client = genai.Client(
#         api_key=GEMINI_API_KEY,
#     )

#     model = "gemini-2.5-flash-lite"
#     contents = [
#         # types.Content(#system prompt
#         #     role="system",
#         #     parts=[
#         #         types.Part.from_text(text="""Make Text Summarization like social media marketing"""),
#         #     ],
#         # ),
#         types.Content(#user prompt same as chat input
#             role="user",
#             parts=[
#                 types.Part.from_text(text=prompt),
#             ],
#         ),
#     ]
#     tools = [
#         types.Tool(googleSearch=types.GoogleSearch(
#         )),
#     ]
#     generate_content_config = types.GenerateContentConfig(
#         thinking_config = types.ThinkingConfig(
#             thinking_budget=-1,
#         ),
#         tools=tools,
#     )

#     for chunk in client.models.generate_content_stream(
#         model=model,
#         contents=contents,
#         config=generate_content_config,
#     ):
#         print(chunk.text, end="")

def execute_gemini(prompt):
    client = genai.Client(
        api_key=GEMINI_API_KEY,
    )

    model = "gemini-2.5-flash-lite"
    contents = [
        types.Content( # user prompt (same as chat input)
            role="user",
            parts=[
                types.Part.from_text(text=prompt),
            ],
        ),
    ]
    tools = [
        # types.Tool(googleSearch=types.GoogleSearch()),
    ]
    generate_content_config = types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(
            thinking_budget=0,
        ),
        response_mime_type="application/json",
        response_schema=genai.types.Schema(
            type=genai.types.Type.OBJECT,
            required=["sentiment_type", "sentiment_score", "topic", "keywords", "target_audience"],
            properties={
                "sentiment_type": genai.types.Schema(
                    type=genai.types.Type.STRING,
                    enum=["angry", "sad", "fearful", "sarcastic", "motivational", "positive", "negative", "excited",
                          "neutral"],
                ),
                "engagement_type":genai.types.Schema(
                  type=genai.types.Type.STRING,
                  enum=["like","reply","impression","retweet"],
                ),
                "sentiment_score": genai.types.Schema(
                    type=genai.types.Type.NUMBER,
                ),
                "topic": genai.types.Schema(
                    type=genai.types.Type.STRING,
                ),
                "reason_for_engagement":genai.types.Schema(
                    type=genai.types.Type.STRING,
                ),
                "engagement_score":genai.types.Schema(
                  type=genai.types.Type.NUMBER ,
                ),
                "keywords": genai.types.Schema(
                    type=genai.types.Type.ARRAY,
                    items=genai.types.Schema(
                        type=genai.types.Type.STRING,
                    ),
                ),
                "target_audience": genai.types.Schema(
                    type=genai.types.Type.STRING,
                ),
            },
        ),
    )

    result = client.models.generate_content(
        model=model,
        contents=contents,
        config=generate_content_config,
    )

    return result.text

if __name__ == "__main__":
    
    bunch=[
        "How many p are there in the word apple?",
        "How many p are there in the word apple?",
        "How many p are there in the word apple?"
    ]
    for prompt in bunch:
            execute_gemini(prompt=prompt)


def execute_gemini_for_tweets(prompt): #INFO: THIS IS FOR TWEET CREATION
    client = genai.Client(
        api_key=GEMINI_API_KEY,
    )

    model = "gemini-2.5-flash-lite"
    contents = [
        types.Content( # user prompt (same as chat input)
            role="user",
            parts=[
                types.Part.from_text(text=prompt),
            ],
        ),
    ]
    tools = [
        # types.Tool(googleSearch=types.GoogleSearch()),
    ]
    generate_content_config = types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(
            thinking_budget=0,
        ),
        response_mime_type="application/json",
        response_schema=genai.types.Schema(
            type=genai.types.Type.OBJECT,
            required=["tweet", "prediction", "explanation"],
            properties={
                "tweet": genai.types.Schema(
                    type=genai.types.Type.STRING,
                ),
                "prediction": genai.types.Schema(
                    type=genai.types.Type.STRING,
                ),
                "explanation": genai.types.Schema(
                    type=genai.types.Type.STRING,
                ),
            },
        ),
    )

    result = client.models.generate_content(
        model=model,
        contents=contents,
        config=generate_content_config,
    )

    return result.text


        
