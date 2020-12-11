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
    loaded_model = pickle.load(open(filename, 'rb'))
    result = loaded_model.predict(testing)

    return response.Response(
        ctx, response_data=json.dumps(
            {"message": "Your risk appetite is {0} percent".format(result)}),
        headers={"Content-Type": "application/json"}
    )
