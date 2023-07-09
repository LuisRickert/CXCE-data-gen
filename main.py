import random
import json
import uuid


def get_part_as_spec(quant: float) -> dict:
    return {
        "childPartsCategory": "e.g. vehicle, winter wheels, bicycle rack",
        "part": [
            {
                "ownerPartId": f"urn:uuid:{uuid.uuid4()}",
                "partVersion": "05",
                "partQuantity": {
                    "quantityNumber": f"{quant}",
                    "measurementUnit": "kW"
                },
                "partDescription": "The steering wheel is nice and round",
                "partClassification": [{
                    "value": "STEEWHL",
                    "key": "BMW:PartFamily"
                }],
                "createdOn": "2022-02-03T14:48:54.709Z",
                "lastModifiedOn": "2022-02-03T14:48:54.709Z"
            }],
        "childCatenaXId": f"urn:uuid:{uuid.uuid4()}"
    }


def get_new_bom_as_spec() -> dict:
    return {
        "catenaXId": f"urn:uuid:{uuid.uuid4()}",
        "childParts": []
    }


def get_bas_with_pas(pas_amount: list[int] = None) -> dict:
    pas_amount = [random.randint(1, 10) for _ in range(10)] if pas_amount is None else pas_amount

    bas = get_new_bom_as_spec()
    bas['childParts'] = [get_part_as_spec(amt) for amt in pas_amount]

    return bas


if __name__ == "__main__":

    for i, bas in enumerate([get_bas_with_pas() for _ in range(10)]):
        print(bas)
        with open(f"./list_bom_as_spec_{i}.json", "w") as file:
            json.dump(bas, file)
