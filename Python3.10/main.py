from enum import Enum, unique


@unique
class HTTPResponse(Enum):
    OK = 200
    PERMANENT_REDIRECT = 301
    TEMPORARY_REDIRECT = 302
    NOT_FOUND = 404
    GONE = 410
    INTERNAL_SERVER_ERROR = 500
    SERVICE_UNAVAILABLE = 503


def main():

    http_response = HTTPResponse.OK

    match http_response:
        case HTTPResponse.OK:
            print(f"{http_response.name}: Page found")
        case HTTPResponse.PERMANENT_REDIRECT:
            print(HTTPResponse)
        case HTTPResponse.TEMPORARY_REDIRECT:
            print(HTTPResponse)
        case HTTPResponse.NOT_FOUND:
            print()
        case _:
            print("Code not found")


if __name__ == "__main__":
    main()
