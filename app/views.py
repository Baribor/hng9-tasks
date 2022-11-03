import os
import openai
from django.http import JsonResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt


operation_types = {"multiplicatio n": "*", "addition": "+", "subtraction": "-"}

openai.api_key = os.environ.get("API_KEY")


@csrf_exempt
def get_evaluation(request: HttpRequest):

    payload = request.POST

    result = None
    operation_type = None
    payload_ot = payload["operation_type"].strip().lower()

    if payload_ot in operation_types:

        operation_type = payload_ot
        result = eval(f'{payload["x"]}{operation_types[payload_ot]}{payload["y"]}')

    else:

        response = openai.Completion.create(
            model="text-davinci-002",
            prompt=f"{payload_ot} \n\n| solution | operation_type |",
            temperature=0,
            max_tokens=100,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
        )
        _, result, operation_type, _ = [
            x.strip() for x in response.choices[0].text.split("\n")[-1].split("|")
        ]

    return JsonResponse(
        {
            "slackUsername": "BarryDee",
            "result": int(result),
            "operation_type": operation_type,
        }
    )
