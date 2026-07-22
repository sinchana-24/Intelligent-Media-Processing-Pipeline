import requests

API_TOKEN = "6d851baff7deac6bd5516f1e54ed8dfc9769fbf2"


def detect_plate(image_path):

    with open(image_path, "rb") as fp:

        response = requests.post(
            "https://api.platerecognizer.com/v1/plate-reader/",
            files={"upload": fp},
            headers={
                "Authorization": f"Token {API_TOKEN}"
            }
        )

    result = response.json()

    print(result)

    if result.get("results"):

        plate = result["results"][0]["plate"].upper()

        return plate, True

    return "", False