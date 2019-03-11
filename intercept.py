import requests
import json
from mitmproxy import http

interceptEndpoints = [
    "lookup/makemodel"
]

def request(flow: http.HTTPFlow):
    if flow.request.path.endswith("enquire/"):
        with open('/Users/hungnguyen/Response/err_reponse.json', 'r') as myfile:
            data = myfile.read()
            print(data)
        flow.response = http.HTTPResponse.make(
            403,
            data,
            {"Content-Type": "application/json"}
        )

    # for endpoint in interceptEndpoints:
    #     if endpoint in flow.request.path:
    #         print(flow.request.method)
    #         # with open('make_model.json', 'r') as myfile:
    #         #     data = myfile.read()
    #         #     print(flow.request.path)
    #         # data = json.loads(flow.request.content)
    #         h = {}
    #         for k, v in flow.request.headers.items():
    #             if k != ':authority':
    #                 h[k] = v
    #         h['authorization'] = 'Token d7ff4455e6e309ea6a1fb85779cf923570b87856'

    #         if flow.request.method == 'GET':
    #             r = requests.get(url = "http://localhost:9286" + flow.request.path, headers = h)
    #             flow.response = http.HTTPResponse.make(
    #                 200,
    #                 r.text,
    #                 {"Content-Type": "application/json"}
    #             )
    #             return
    #         else:
    #             data = json.loads(flow.request.content)
    #             r = requests.post(url = "http://localhost:9282" + flow.request.path, data = json.dumps(data), headers = h)
    #             flow.response = http.HTTPResponse.make(
    #                 200,
    #                 r.text,
    #                 {"Content-Type": "application/json"}
    #             )
    #             return
    # if flow.request.path.endswith("axa_quote/post_form/"):
    #     data = json.loads(flow.request.content)

    #     h = {}
    #     for k, v in flow.request.headers.items():
    #         if k != ':authority':
    #             h[k] = v
    #     h['authorization'] = 'Token d7ff4455e6e309ea6a1fb85779cf923570b87856'

    #     r = requests.post(url = "http://localhost:9282/vs/1.0/axa_quote/post_form/", data = json.dumps(data), headers = h)
    #     flow.response = http.HTTPResponse.make(
    #         200,
    #         r.text,
    #         {"Content-Type": "application/json"}
    #     )
    # if "lookup/makemodel" in flow.request.path:
    #     print(flow.request.method)
    #     # with open('make_model.json', 'r') as myfile:
    #     #     data = myfile.read()
    #     #     print(flow.request.path)
    #     # data = json.loads(flow.request.content)

    #     h = {}
    #     for k, v in flow.request.headers.items():
    #         if k != ':authority':
    #             h[k] = v
    #     h['authorization'] = 'Token d7ff4455e6e309ea6a1fb85779cf923570b87856'
    #     print("http://localhost:9286/" + flow.request.path)
    #     r = requests.get(url = "http://localhost:9286" + flow.request.path, headers = h)
    #     flow.response = http.HTTPResponse.make(
    #         200,
    #         r.text,
    #         {"Content-Type": "application/json"}
    #     ) 
    #     # flow.response = http.HTTPResponse.make(
    #     #     200,
    #     #     data,
    #     #     {"Content-Type": "application/json"}
    #     # )

    # if flow.request.path.endswith("smart_homescreen/22/?journey=main"):
    #     with open('/Users/tuan/Documents/working/carousell/backend/FieldSetGenerator/staging/smart_homescreen/22/main.json', 'r') as myfile:
    #         data = myfile.read()
    #         print(data)
    #     flow.response = http.HTTPResponse.make(
    #         200,
    #         data,
    #         {"Content-Type": "application/json"}
    #     )
    #
    # if flow.request.path.endswith("smart_homescreen/22/?journey=more"):
    #     with open('/Users/tuan/Documents/working/carousell/backend/FieldSetGenerator/staging/smart_homescreen/22/more.json', 'r') as myfile:
    #         data = myfile.read()
    #         print(data)
    #     flow.response = http.HTTPResponse.make(
    #         200,
    #         data,
    #         {"Content-Type": "application/json"}
    #     )
    #
    # if flow.request.path.endswith("smart_homescreen/1241/?journey=main"):
    #     with open('/Users/tuan/Documents/working/carousell/backend/FieldSetGenerator/staging/smart_homescreen/1241/main.json', 'r') as myfile:
    #         data = myfile.read()
    #         print(data)
    #     flow.response = http.HTTPResponse.make(
    #         200,
    #         data,
    #         {"Content-Type": "application/json"}
    #     )

    # if flow.request.path.endswith("axa_quote/get_place_order_form/"):
    #     data = json.loads(flow.request.content)

    #     h = {}
    #     for k, v in flow.request.headers.items():
    #         if k != ':authority':
    #             h[k] = v
    #     h['authorization'] = 'Token d7ff4455e6e309ea6a1fb85779cf923570b87856'

    #     r = requests.post(url = "http://localhost:9282/vs/1.0/axa_quote/get_place_order_form/", data = json.dumps(data), headers = h)
    #     flow.response = http.HTTPResponse.make(
    #         200,
    #         r.text,
    #         {"Content-Type": "application/json"}
    #     )
    # if flow.request.path.endswith("axa_quote/make_order/"):
    #     data = json.loads(flow.request.content)

    #     h = {}
    #     for k, v in flow.request.headers.items():
    #         if k != ':authority':
    #             h[k] = v
    #     h['authorization'] = 'Token d7ff4455e6e309ea6a1fb85779cf923570b87856'

    #     r = requests.post(url = "http://localhost:9282/vs/1.0/axa_quote/make_order/", data = json.dumps(data), headers = h)
    #     flow.response = http.HTTPResponse.make(
    #         200,
    #         r.text,
    #         {"Content-Type": "application/json"}
    #     )
    # if flow.request.path.endswith("axa_quote/get_place_order_form/"):
    #     with open('test.json', 'r') as myfile:
    #         data = myfile.read()
    #     flow.response = http.HTTPResponse.make(
    #         200,
    #         data,
    #         {"Content-Type": "application/json"}
    #     )

