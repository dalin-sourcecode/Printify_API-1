def Parse_A(data,
            key_data,
            key_id,
            key_name,
            UPLOAD_STARTSWITH,
            image_version_1):
	List_A1 = []
	List_A2 = []

	try:
		for numbers in range(len(data[key_data])):

			name_B1 = str(data[key_data][numbers][key_name])
			id_B2 = str(data[key_data][numbers][key_id])

			if name_B1.startswith(f"{UPLOAD_STARTSWITH}{image_version_1}"):
				List_A1.append(name_B1)
				List_A2.append(id_B2)

	except KeyError:
		print("CLASS:PRODUCT_SIMPLE>FUNCTION:LISTS_GET_IMAGES >>> ", KeyError,
		      "THIS IS A PRINTIFY BUG, I CAN'T FIX IT BUT IT STILL WORKS, SUPPORT GAVE NO HELP ON THE MATTER")

	return List_A1, List_A2


def Parse_B(data,
            key_data,
            key_id,
            key_name,
            startswith_1):
	List_A1 = []
	List_A2 = []

	try:

		for numbers in range(len(data[key_data])):

			name_B1 = str((data[key_data][numbers][key_name]))
			id_B2 = str((data[key_data][numbers][key_id]))

			if name_B1.startswith(f"{startswith_1}"):
				List_A1.append(name_B1)
				List_A2.append(id_B2)

	except KeyError:
		print("CLASS:PRODUCT_SIMPLE>FUNCTION:LISTS_GET_COPIES >>> ", KeyError,
		      "THIS IS A PRINTIFY BUG, I CAN'T FIX IT BUT IT STILL WORKS, SUPPORT GAVE NO HELP ON THE MATTER")

	return List_A1, List_A2


def Parse_C(template_data, key_list):
	try:
		for key in key_list:
			HEIGHT = (template_data["print_areas"][0]["placeholders"][0]["images"][key]["height"])
			WIDTH = (template_data["print_areas"][0]["placeholders"][0]["images"][key]["width"])
			X = (template_data["print_areas"][0]["placeholders"][0]["images"][key]["x"])
			Y = (template_data["print_areas"][0]["placeholders"][0]["images"][key]["y"])
			SCALE = (template_data["print_areas"][0]["placeholders"][0]["images"][key]["scale"])
			ANGLE = (template_data["print_areas"][0]["placeholders"][0]["images"][key]["angle"])
			BACKGROUND = (template_data["print_areas"][0]["background"])

			yield (HEIGHT,
			       WIDTH,
			       X, Y,
			       SCALE,
			       ANGLE,
			       BACKGROUND)
	except (KeyError, IndexError) as e:
		print(f"Parse_C error: {e}")
		yield None


def Parse_C2(template_data, key):
	try:

		HEIGHT = (template_data["print_areas"][0]["placeholders"][0]["images"][key]["height"])
		WIDTH = (template_data["print_areas"][0]["placeholders"][0]["images"][key]["width"])
		X = (template_data["print_areas"][0]["placeholders"][0]["images"][key]["x"])
		Y = (template_data["print_areas"][0]["placeholders"][0]["images"][key]["y"])
		SCALE = (template_data["print_areas"][0]["placeholders"][0]["images"][key]["scale"])
		ANGLE = (template_data["print_areas"][0]["placeholders"][0]["images"][key]["angle"])
		BACKGROUND = (template_data["print_areas"][0]["background"])

		return HEIGHT, WIDTH, X, Y, SCALE, ANGLE, BACKGROUND

	except (KeyError, IndexError) as e:
		print(f"Parse_C error: {e}")
		return None


def Parse_D(template_data, key_list):
	try:
		for key in key_list:
			SPECIFIC_HEIGHT = (template_data["print_areas"][key]["placeholders"][0]["images"][0]["height"])
			SPECIFIC_WIDTH = (template_data["print_areas"][key]["placeholders"][0]["images"][0]["width"])
			SPECIFIC_X = (template_data["print_areas"][key]["placeholders"][0]["images"][0]["x"])
			SPECIFIC_Y = (template_data["print_areas"][key]["placeholders"][0]["images"][0]["y"])
			SPECIFIC_SCALE = (template_data["print_areas"][key]["placeholders"][0]["images"][0]["scale"])
			SPECIFIC_ANGLE = (template_data["print_areas"][key]["placeholders"][0]["images"][0]["angle"])
			BACKGROUND = (template_data["print_areas"][0]["background"])

			yield (SPECIFIC_HEIGHT,
			       SPECIFIC_WIDTH,
			       SPECIFIC_X,
			       SPECIFIC_Y,
			       SPECIFIC_SCALE,
			       SPECIFIC_ANGLE,
			       BACKGROUND)
	except (KeyError, IndexError) as e:
		print(f"Parse_D error: {e}")
		yield None


def Parse_E(template_data, key):
	try:

		_L_SLEEVE_IMAGE_NAME = (template_data["print_areas"][0]["placeholders"][key]["images"][0]["name"])
		_L_SLEEVE_IMAGE_ID = (template_data["print_areas"][0]["placeholders"][key]["images"][0]["id"])
		_L_SLEEVE_HEIGHT = (template_data["print_areas"][0]["placeholders"][key]["images"][0]["height"])
		_L_SLEEVE_WIDTH = (template_data["print_areas"][0]["placeholders"][key]["images"][0]["width"])
		_L_SLEEVE_X = (template_data["print_areas"][0]["placeholders"][key]["images"][0]["x"])
		_L_SLEEVE_Y = (template_data["print_areas"][0]["placeholders"][key]["images"][0]["y"])
		_L_SLEEVE_SCALE = (template_data["print_areas"][0]["placeholders"][key]["images"][0]["scale"])
		_L_SLEEVE_ANGLE = (template_data["print_areas"][0]["placeholders"][key]["images"][0]["angle"])

		return _L_SLEEVE_IMAGE_NAME,\
		       _L_SLEEVE_IMAGE_ID,\
		       _L_SLEEVE_HEIGHT,\
		       _L_SLEEVE_WIDTH,\
		       _L_SLEEVE_X,\
		       _L_SLEEVE_Y,\
		       _L_SLEEVE_SCALE,\
		       _L_SLEEVE_ANGLE
	except (KeyError, IndexError) as e:
		print(f"Parse_E error: {e}")
		return None
