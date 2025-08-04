import pprint
import requests

def GET_request(url,
                API_KEY,
                COOKIE):
	data = None
	try:

		payload = ""
		headers = {
			'Authorization': f"Bearer {API_KEY}",
			'Cookie': COOKIE
		}

		response = requests.request("GET", url, headers=headers, data=payload)
		# print(response.status_code)

		data = response.json()

	except Exception as e:
		print(f"GET_request error: {e}")

	return data


def PUT_request(url,
                payload,
                API_KEY,
                COOKIE):
	data = None
	try:
		headers = {
			'Content-Type': 'application/json',
			'Authorization': f"Bearer {API_KEY}",
			'Cookie': COOKIE
		}

		response = requests.request("PUT", url, headers=headers, data=payload)
		# print(response.status_code)

		data = response.json()

		pprint.pprint(data)
		pprint.pprint(response.text)
		pprint.pprint(response.request)
		pprint.pprint(response.reason)

	except Exception as e:
		print(f"PUT_request error: {e}")
		data = None

	return data
