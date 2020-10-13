from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from entries import get_all_entries, get_single_entry, delete_entry
from moods import get_all_moods

class HandleRequests(BaseHTTPRequestHandler):
    def parse_url(self, path):
        path_params = path.split("/")
        resource = path_params[1]

        if "?" in resource:
            # GIVEN: /animals?location_id=1

            param = resource.split("?")[1]  #  location_id=1
            resource = resource.split("?")[0]  #  'animals'
            pair = param.split("=")  #  ['location_id', '1']
            key = pair[0]  # "location_id"
            value = pair[1]  #  "1"

            return ( resource, key, value )

        else:
            id = None
            try:
                id = int(path_params[2])
            except IndexError:
                pass  # No route parameter exists: /animals
            except ValueError:
                pass  # Request had trailing slash: /animals/

            return (resource, id)

    # Here's a class function
    def _set_headers(self, status):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def do_GET(self):
        self._set_headers(200)

        response = {}

        parsed = self.parse_url(self.path)

        if len(parsed) == 2:
            ( resource, id ) = parsed

            if resource == "entries":
                if id is not None:
                    response = f"{get_single_entry(id)}"
                else:
                    response = f"{get_all_entries()}"
            if resource == "moods":
                response = f"{get_all_moods()}"

        # elif len(parsed) == 3:
        #     ( resource, key, value ) = parsed

        self.wfile.write(response.encode())

    # Here's a method on the class that overrides the parent's method.
    # It handles any POST request.
    # def do_POST(self):
    #     self._set_headers(201)
    #     content_len = int(self.headers.get('content-length', 0))
    #     post_body = self.rfile.read(content_len)

        # Convert JSON string to a Python dictionary
        # post_body = json.loads(post_body)

        # Parse the URL
        # (resource, id) = self.parse_url(self.path)

        # Initialize new animal
        # new_resource = None

        # Add a new items to the list.
        #if resource == "entries":
        #   new_resource = create_entry(post_body)

        # Encode the new animal and send in response
        # self.wfile.write(f"{new_resource}".encode())


    # Here's a method on the class that overrides the parent's method.
    # It handles any PUT request.
    # def do_PUT(self):
    #     self._set_headers(204)
    #     content_len = int(self.headers.get('content-length', 0))
    #     post_body = self.rfile.read(content_len)
    #     post_body = json.loads(post_body)

    #     # Parse the URL
    #     (resource, id) = self.parse_url(self.path)

    #     # Delete a single animal from the list
    #     if resource == "animals":
    #         update_animal(id, post_body)
    #     if resource == "locations":
    #         update_location(id, post_body)
    #     if resource == "employees":
    #         update_employee(id, post_body)
    #     if resource == "entries":
    #         update_entrie(id, post_body)

    #     # Encode the new animal and send in response
    #     self.wfile.write("".encode())
    
    def do_DELETE(self):
        self._set_headers(204)

        (resource, id) = self.parse_url(self.path)

        # Delete a single animal from the list
        if resource == "entries":
            delete_entry(id)

        self.wfile.write("".encode())


# This function is not inside the class. It is the starting
# point of this application.
def main():
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()