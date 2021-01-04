#
# hello-python version 1.0.
#
# Copyright (c) 2020 Oracle, Inc.  All rights reserved.
# Licensed under the Universal Permissive License v 1.0 as shown at https://oss.oracle.com/licenses/upl.
#

import io
import json
import pickle

from fdk import response


def handler(ctx, data: io.BytesIO=None):
    print("Entering Python Hello World handler", flush=True)
    name = [3,2,0,0,1,1,2,2,1,2,5,2,0,0,1,3,2,5,4,4,3,2]
    try:
        body = json.loads(data.getvalue())
        name = body.get("name")
    except (Exception, ValueError) as ex:
        print(str(ex), flush=True)
    
    
    testing = [name]
    print("Vale of value = ", name, flush=True)
    print("Exiting Python Hello World handler", flush=True)
    filename = 'finalized_model.sav'
    
    model_dir = os.path.dirname(os.path.realpath(__file__))
    contents = os.listdir(model_dir)
    if filename in contents:
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), model_file_name), "rb") as file:
            loaded_model = pickle.load(file)
	    result = loaded_model.predict(testing)
    else:
        raise Exception('{0} is not found in model directory {1}'.format(filename, model_dir))



    #loaded_model = pickle.load(open(filename, 'rb'))
    #result = Nope

    return response.Response(
        ctx, response_data=json.dumps(
            {"message": "Your risk appetite is {0} percent".format(result)}),
        headers={"Content-Type": "application/json"}
    )
