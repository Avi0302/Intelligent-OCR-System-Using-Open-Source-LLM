import re


def validate_email(email):

    return bool(
        re.match(
            r'^[\w\.-]+@[\w\.-]+\.\w+$',
            str(email)
        )
    )


def validate_phone(phone):

    phone = str(phone).replace(" ", "")

    return bool(
        re.match(
            r'^[6-9]\d{9}$',
            phone
        )
    )


def validate_pan(pan):

    return bool(
        re.match(
            r'^[A-Z]{5}[0-9]{4}[A-Z]$',
            str(pan)
        )
    )


def validate_aadhaar(aadhaar):

    return bool(
        re.match(
            r'^\d{12}$',
            str(aadhaar)
        )
    )


def validate_data(data):

    results = {}

    results["email"] = validate_email(
        data.get("email", "")
    )

    results["phone_number"] = validate_phone(
        data.get("phone_number", "")
    )

    results["pan_number"] = validate_pan(
        data.get("pan_number", "")
    )

    results["aadhaar_number"] = validate_aadhaar(
        data.get("aadhaar_number", "")
    )

    return results