# Simplest form of match compares against one or more literals
def http_error(status):
    match status:
        case 400:
            return "bad request"
        case 401 | 402 | 403| 404:
            return "Not allowed"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"

# the last case, variable _, acts as a wildcard that never fails to match

print("http_error(400):", http_error(400))
print("http_error(401):", http_error(401))
print("http_error(402):", http_error(402))
print("http_error(403):", http_error(403))
print("http_error(404):", http_error(404))
print("http_error(418):", http_error(418))
print("http_error(419):", http_error(419))
