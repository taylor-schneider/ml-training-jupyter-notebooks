#!/usr/bin/env python


'''
This is a simple Python REST Web Server. It will accept the following web methods:

   GET
   POST
   PUT
   DELETE

It can be tested using the following curl commands:

   GET:  	curl http://localhost:8000/test-dir/test.txt
   POST		curl -X POST http://localhost:8000/test-dir/test.txt --upload-file test.txt 
   PUT		curl http://localhost:8000/test-dir/test.txt --upload-file test.txt
   DELETE:      curl -X DELETE http://localhost:8000/test-dir/test.txt

'''

import sys
import argparse
import json
from flask import Flask, jsonify, request, jsonify
import os
import pathlib
import shutil
import logging
import urllib.parse

def run_server(port, web_root, debug=False):
    
    logging.info("Starting server on port {0}".format(port))
    logging.info("Web root specified as: {0}".format(web_root))
    
    app = Flask(__name__, root_path=web_root)

    @app.route('/', defaults={'path': ''}, methods=['PUT', 'POST'])
    @app.route('/<path:path>', methods=['PUT', 'POST'])
    def upload_file(path):
        x = request
        file_path = request.path
        full_file_path = os.path.join(web_root, file_path.strip("/"))
        file_data = request.data

        # Create the directory if it does not exist
        file_directory = os.path.dirname(full_file_path)
        pathlib.Path(file_directory).mkdir(parents=True, exist_ok=True)

        # Write the file data to disk
        with open(full_file_path, 'wb') as file:
            file.write(file_data)
        logging.info("Uploaded {0}".format(full_file_path))
        return "Successfully uploaded {0}\n".format(file_path)

    @app.route('/', defaults={'path': ''}, methods=['GET'])
    @app.route('/<path:path>', methods=['GET'])
    def get_file(path):
        file_path = request.path
        file_path = urllib.parse.unquote(file_path)
        full_file_path = os.path.join(web_root, file_path.strip("/"))
        file_contents = None
        logging.info("Get {0}".format(full_file_path))
        with open(full_file_path, 'r') as file:
            file_contents = file.read()
        return file_contents + "\n"

    @app.route('/', defaults={'path': ''}, methods=['DELETE'])
    @app.route('/<path:path>', methods=['DELETE'])
    def delete_file(path):
        file_path = request.path
        full_file_path = os.path.join(web_root, file_path.strip("/"))
        logging.info("Delete {0}".format(full_file_path))

        if os.path.isfile(full_file_path):
            os.remove(full_file_path)

        if os.path.isdir(full_file_path):
            shutil.rmtree(full_file_path)

        return "Successfully deleted {0} deleted\n".format(file_path)

    app.run(debug=debug, port=port, host="0.0.0.0")

def main(argv):

   parser = argparse.ArgumentParser(description='A Python Web Server')
   parser.add_argument('--port', help='An integer representing the port that the server should bind to.', required=True)
   parser.add_argument('--dir', help='The full directory path of the web root.', required=True)
   args = parser.parse_args()

   logging.info(dir(args))
   logging.info("The port is {0}".format(args.port))

   run_server(args.port, args.dir)

if __name__ == '__main__':
    main(sys.argv[1:])