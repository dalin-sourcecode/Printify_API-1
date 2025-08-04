#############################################################
import json
import pprint
from METHOD_requests import GET_request, PUT_request
from METHOD_parse import Parse_A, Parse_B, Parse_C, Parse_C2, Parse_D, Parse_E
from METHOD_wrapper import wrapper_func

#############################################################

class PRODUCT_SIMPLE:
	def __init__(self, SHOP_ID,
	             API_KEY,
	             COOKIE,
	             PRODUCT_TITLE,
	             PRODUCT_TITLE_SUFFIX,
	             IMAGE_VERSION,
	             PAGINATION,
	             STARTSWITH,
	             UPLOAD_STARTSWITH,
	             PRODUCT_ID,
	             VARIANT_ID):

		self.SHOP_ID = SHOP_ID
		self.API_KEY = API_KEY
		self.COOKIE = COOKIE
		self.PRODUCT_TITLE = PRODUCT_TITLE
		self.PRODUCT_TITLE_SUFFIX = PRODUCT_TITLE_SUFFIX
		self.IMAGE_VERSION = IMAGE_VERSION
		self.PAGINATION = PAGINATION
		self.STARTSWITH = STARTSWITH
		self.UPLOAD_STARTSWITH = UPLOAD_STARTSWITH
		self.PRODUCT_ID = PRODUCT_ID
		self.VARIANT_ID = VARIANT_ID

		self.template_data = self.JSON_GET_TEMPLATE_DATA(
			self.PRODUCT_ID)  #GETS DATA FROM THE SAMPLE PRODUCT THAT YOU WANT TO DUPLICATE

		self.list_image_name, self.list_image_id = self.LISTS_GET_IMAGES(self.IMAGE_VERSION,
		                                                                 self.PAGINATION)  # Here is we return the list of the image filenames and the image id's that are associated with them
		self.list_copy_title, self.list_copy_id = self.LISTS_GET_COPIES(self.STARTSWITH, self.PAGINATION)

	def JSON_GET_TEMPLATE_DATA(self, template_id_1):
		print("Getting Template Data")

		data = None

		try:

			url = f"https://api.printify.com/v1/shops/{self.SHOP_ID}/products/{template_id_1}.json"  #getting the data of my template product so that data can be mimmicked

			data = GET_request(url,
			                   self.API_KEY,
			                   self.COOKIE)
		except Exception as Ex:
			print("CLASS:PRODUCT_SIMPLE>FUNCTION:JSON_GET_TEMPLATE_DATA >>> ", Ex)

		return data

	def LISTS_GET_IMAGES(self, image_version_1,
	                     number_of_pages_1):  # HERE WE ARE GETTING A LIST OF THE IMAGE NAME AND ID, THEN SEPARATING THE LIST INTO 2
		print("Getting images list")

		List_A1 = []  #image name
		List_A2 = []  #image id

		try:
			for page in range(number_of_pages_1):  # if you have added more images you will need to increase this number

				url = f"https://api.printify.com/v1/uploads.json?page={page}"  #get images url

				data = GET_request(url,
				                   self.API_KEY,
				                   self.COOKIE)

				if data is not None:
					List_B1, List_B2 = Parse_A(data,  #image name, image id
					                           "data",
					                           "id",
					                           "file_name",
					                           self.UPLOAD_STARTSWITH,
					                           image_version_1)

					List_A1.extend(List_B1)  #image name list extending
					List_A2.extend(List_B2)  #image id list extending

		except Exception as e:
			print(f"LISTS_GET_IMAGES error: {e}")

		return List_A1, List_A2  #image name list, image id list

	def LISTS_GET_COPIES(self, startswith_1,
	                     number_of_pages_1):  # HERE WE ARE GETTING A LIST OF THE IMAGE NAME AND ID, THEN SEPARATING THE LIST INTO 2

		print("getting copy list")
		print("This stage will take awhile depending on your pagination value")

		List_A1 = []  #copy title name
		List_A2 = []  #copy id

		try:
			for page in range(number_of_pages_1):  # if you have added more images you will need to increase this number

				url = f"https://api.printify.com/v1/shops/{self.SHOP_ID}/products.json?page={page}"  #getting products page

				data = GET_request(url,
				                   self.API_KEY,
				                   self.COOKIE)

				if data is not None:
					List_B1, List_B2 = Parse_B(data,  #copy title list, copy id list
					                           "data",
					                           "id",
					                           "title",
					                           startswith_1)

					List_A1.extend(List_B1)  #extending the copy title name list
					List_A2.extend(List_B2)  #extending the copy id list

		except Exception as e:
			print(f"LISTS_GET_COPIES error: {e}")

		return List_A1, List_A2

	def RETURN_INFO(self):
		try:
			pprint.pprint("Getting tdata")
			pprint.pprint(self.template_data)
			pprint.pprint("Getting image list")
			pprint.pprint(f"{self.list_image_name}")
			pprint.pprint("Getting image id")
			pprint.pprint(f"{self.list_image_id}")
			pprint.pprint("Getting copy title")
			pprint.pprint(f"{self.list_copy_title}")
			pprint.pprint("Getting copy id")
			pprint.pprint(f"{self.list_copy_id}")
		except Exception as e:
			print(f"RETURN_INFO error: {e}")

	@wrapper_func
	def REPLICATE_TEMPLATE_SIMPLE_PRODUCT(self,
	                                      product_title,
	                                      product_title_suffix,
	                                      img_name,
	                                      img_id,
	                                      COPY_1_ID,
	                                      template_data):
		print("Replicating: SIMPLE GALLARY CANVAS WRAP")
		try:

			################################################################################
			key = 0
			parse_result = Parse_C2(template_data, key)
			
			if parse_result is None:
				print("Error: Could not parse template data")
				return
				
			(HEIGHT, WIDTH, X, Y, SCALE, ANGLE, BACKGROUND) = parse_result
			################################################################################

			url = f"https://api.printify.com/v1/shops/{self.SHOP_ID}/products/{COPY_1_ID}.json"
			payload = json.dumps({
				"id": f"{COPY_1_ID}",
				"title": f"{product_title}{product_title_suffix}",
				"print_areas": [
					{
						"variant_ids": self.VARIANT_ID,
						# Copy and paste Add all variants here manually and remove the ones that are being used below #keep the ones that belong to the first in line

						"placeholders": [
							{
								"position": "front",
								"images": [
									{
										"id": f"{img_id}",
										"name": f"{img_name}",
										"type": "image/jpeg",
										"height": HEIGHT,
										"width": WIDTH,
										"x": X,
										"y": Y,
										"scale": SCALE,
										"angle": ANGLE,
									},

								]
							}
						],
						"background": f"{BACKGROUND}"
					}
				]
			})

			PUT_request(url,
			            payload,
			            self.API_KEY,
			            self.COOKIE)

		except Exception as Ex:
			print("CLASS:PRODUCT_SIMPLE>FUNCTION:REPLICATE_TEMPLATE_SIMPLE_PRODUCT >>> ", Ex)


class PRODUCT_SPECIFIC(PRODUCT_SIMPLE):
	def __init__(self,
	             SHOP_ID,
	             API_KEY,
	             COOKIE,
	             PRODUCT_TITLE,
	             PRODUCT_TITLE_SUFFIX,
	             IMAGE_VERSION,
	             PAGINATION,
	             STARTSWITH,
	             UPLOAD_STARTSWITH,
	             PRODUCT_ID,
	             VARIANT_ID,
	             VARIANT_ID2):  #UPGRADED INSTANCE

		super().__init__(SHOP_ID,
		                 API_KEY,
		                 COOKIE,
		                 PRODUCT_TITLE,
		                 PRODUCT_TITLE_SUFFIX,
		                 IMAGE_VERSION,
		                 PAGINATION,
		                 STARTSWITH,
		                 UPLOAD_STARTSWITH,
		                 PRODUCT_ID,
		                 VARIANT_ID)  #INHERITED INSTANCE

		self.VARIANT_ID2 = VARIANT_ID2
	@wrapper_func
	def REPLICATE_TEMPLATE_SPECIFIC_PRODUCT(self,
	                                        product_title,
	                                        product_title_suffix,
	                                        img_name,
	                                        img_id,
	                                        COPY_1_ID,
	                                        template_data):

		################################################################################
		key = 0
		
		(HEIGHT, WIDTH, X, Y, SCALE, ANGLE, BACKGROUND)\
			= Parse_C2(template_data, key)

		key = 1
		
		(SPECIFIC_HEIGHT,
		 SPECIFIC_WIDTH,
		 SPECIFIC_X,
		 SPECIFIC_Y,
		 SPECIFIC_SCALE,
		 SPECIFIC_ANGLE, _)\
			= Parse_D(template_data, key)
		################################################################################
		url = f"https://api.printify.com/v1/shops/{self.SHOP_ID}/products/{COPY_1_ID}.json"
		payload = json.dumps({
			"id": f"{COPY_1_ID}",
			"title": f"{product_title}{product_title_suffix}",
			"print_areas": [
				{
					"variant_ids": self.VARIANT_ID,
					"placeholders": [
						{
							"position": "front",
							"images": [
								{
									"id": f"{img_id}",
									"name": f"{img_name}",
									"type": "image/jpeg",
									"height": f"{HEIGHT}",
									"width": f"{WIDTH}",
									"x": f"{X}",
									"y": f"{Y}",
									"scale": f"{SCALE}",
									"angle": f"{ANGLE}",
								},

							]
						}
					],
					"background": f"{BACKGROUND}"
				},
				{
					"variant_ids": self.VARIANT_ID2,
					"placeholders": [
						{
							"position": "front",
							"images": [
								{
									"id": f"{img_id}",
									"name": f"{img_name}",
									"type": "image/jpeg",
									"height": f"{SPECIFIC_HEIGHT}",
									"width": f"{SPECIFIC_WIDTH}",
									"x": f"{SPECIFIC_X}",
									"y": f"{SPECIFIC_Y}",
									"scale": f"{SPECIFIC_SCALE}",
									"angle": f"{SPECIFIC_ANGLE}",
								}
							]
						}
					],
					"background": f"{BACKGROUND}"
				}
			]
		})

		data = PUT_request(url,
		                   payload,
		                   self.API_KEY,
		                   self.COOKIE)

	@wrapper_func
	def REPLICATE_TEMPLATE_SPECIFIC_PRODUCT1(self,
	                                         product_title,
	                                         product_title_suffix,
	                                         img_name,
	                                         img_id,
	                                         COPY_1_ID,
	                                         template_data):

		try:

			################################################################################
			key = 0
			(HEIGHT, WIDTH, X, Y, SCALE, ANGLE, BACKGROUND) = Parse_C2(template_data, key)


			################################################################################

			url = f"https://api.printify.com/v1/shops/{self.SHOP_ID}/products/{COPY_1_ID}.json"
			payload = json.dumps({
				"id": f"{COPY_1_ID}",
				"title": f"{product_title}{product_title_suffix}",
				"print_areas": [
					{
						"variant_ids": self.VARIANT_ID,
						"placeholders": [
							{
								"position": "front",
								"images": [

									{
										"id": f"{img_id}",
										"name": f"{img_name}",
										"type": "image/jpeg",
										"height": HEIGHT,
										"width": WIDTH,
										"x": X,
										"y": Y,
										"scale": SCALE,
										"angle": ANGLE,
									}

								]
							}
						],
						"background": f"{BACKGROUND}"
					},
				]
			})

			PUT_request(url,
			            payload,
			            self.API_KEY,
			            self.COOKIE)

		except Exception as Ex:
			print("Hellppo", Ex)

	@wrapper_func
	def REPLICATE_TEMPLATE_SPECIFIC_PRODUCT2(self,
	                                         product_title,
	                                         product_title_suffix,
	                                         img_name,
	                                         img_id,
	                                         COPY_1_ID,
	                                         template_data):

		################################################################################
		key_list = [0, 1]

		(HEIGHT, WIDTH, X, Y, SCALE, ANGLE, BACKGROUND,
		 HEIGHT2, WIDTH2, X2, Y2, SCALE2, ANGLE2, _)\
			= Parse_C(template_data, key_list)
		################################################################################

		url = f"https://api.printify.com/v1/shops/{self.SHOP_ID}/products/{COPY_1_ID}.json"
		payload = json.dumps({
			"id": f"{COPY_1_ID}",
			"title": f"{product_title}{product_title_suffix}",
			"print_areas": [
				{
					"variant_ids": self.VARIANT_ID,
					"placeholders": [
						{
							"position": "front",
							"images": [
								{
									"id": f"{img_id}",
									"name": f"{img_name}",
									"type": "image/jpeg",
									"height": HEIGHT,
									"width": WIDTH,
									"x": X,
									"y": Y,
									"scale": SCALE,
									"angle": ANGLE,
								},
								{
									"id": f"{img_id}",
									"name": f"{img_name}",
									"type": "image/jpeg",
									"height": HEIGHT2,
									"width": WIDTH2,
									"x": X2,
									"y": Y2,
									"scale": SCALE2,
									"angle": ANGLE2,
								},

							]
						}
					],
					"background": f"{BACKGROUND}"
				},
			]
		})

		PUT_request(url,
		            payload,
		            self.API_KEY,
		            self.COOKIE)

	@wrapper_func
	def REPLICATE_TEMPLATE_SPECIFIC_PRODUCT3(self,
	                                         product_title,
	                                         product_title_suffix,
	                                         img_name,
	                                         img_id,
	                                         COPY_1_ID,
	                                         template_data):

		################################################################################
		key_list = [0, 1, 2]

		(HEIGHT, WIDTH, X, Y, SCALE, ANGLE, BACKGROUND,
		 HEIGHT2, WIDTH2, X2, Y2, SCALE2, ANGLE2, _,
		 HEIGHT3, WIDTH3, X3, Y3, SCALE3, ANGLE3, _)\
			= Parse_C(template_data, key_list)
		################################################################################

		url = f"https://api.printify.com/v1/shops/{self.SHOP_ID}/products/{COPY_1_ID}.json"
		payload = json.dumps({
			"id": f"{COPY_1_ID}",
			"title": f"{product_title}{product_title_suffix}",
			"print_areas": [
				{
					"variant_ids": self.VARIANT_ID,
					"placeholders": [
						{
							"position": "front",
							"images": [
								{
									"id": f"{img_id}",
									"name": f"{img_name}",
									"type": "image/jpeg",
									"height": HEIGHT,
									"width": WIDTH,
									"x": X,
									"y": Y,
									"scale": SCALE,
									"angle": ANGLE,
								},
								{
									"id": f"{img_id}",
									"name": f"{img_name}",
									"type": "image/jpeg",
									"height": HEIGHT2,
									"width": WIDTH2,
									"x": X2,
									"y": Y2,
									"scale": SCALE2,
									"angle": ANGLE2,
								},
								{
									"id": f"{img_id}",
									"name": f"{img_name}",
									"type": "image/jpeg",
									"height": HEIGHT3,
									"width": WIDTH3,
									"x": X3,
									"y": Y3,
									"scale": SCALE3,
									"angle": ANGLE3,
								},

							]
						}
					],
					"background": f"{BACKGROUND}"
				},
			]
		})

		PUT_request(url,
		            payload,
		            self.API_KEY,
		            self.COOKIE)

	@wrapper_func
	def REPLICATE_TEMPLATE_SPECIFIC_PRODUCT4(self,
	                                         product_title,
	                                         product_title_suffix,
	                                         img_name,
	                                         img_id,
	                                         COPY_1_ID,
	                                         template_data):

		################################################################################
		key_list = [0, 1, 2, 3]

		(HEIGHT, WIDTH, X, Y, SCALE, ANGLE, BACKGROUND,
		 HEIGHT2, WIDTH2, X2, Y2, SCALE2, ANGLE2, _,
		 HEIGHT3, WIDTH3, X3, Y3, SCALE3, ANGLE3, _,
		 HEIGHT4, WIDTH4, X4, Y4, SCALE4, ANGLE4, _)\
			= Parse_C(template_data, key_list)
		################################################################################

		url = f"https://api.printify.com/v1/shops/{self.SHOP_ID}/products/{COPY_1_ID}.json"
		payload = json.dumps({
			"id": f"{COPY_1_ID}",
			"title": f"{product_title}{product_title_suffix}",
			"print_areas": [
				{
					"variant_ids": self.VARIANT_ID,
					"placeholders": [
						{
							"position": "front",
							"images": [
								{
									"id": f"{img_id}",
									"name": f"{img_name}",
									"type": "image/jpeg",
									"height": f"{HEIGHT}",
									"width": f"{WIDTH}",
									"x": f"{X}",
									"y": f"{Y}",
									"scale": f"{SCALE}",
									"angle": ANGLE,
								},
								{
									"id": f"{img_id}",
									"name": f"{img_name}",
									"type": "image/jpeg",
									"height": f"{HEIGHT2}",
									"width": f"{WIDTH2}",
									"x": f"{X2}",
									"y": f"{Y2}",
									"scale": f"{SCALE2}",
									"angle": ANGLE2,
								},
								{
									"id": f"{img_id}",
									"name": f"{img_name}",
									"type": "image/jpeg",
									"height": HEIGHT3,
									"width": WIDTH3,
									"x": X3,
									"y": Y3,
									"scale": SCALE3,
									"angle": ANGLE3,
								},
								{
									"id": f"{img_id}",
									"name": f"{img_name}",
									"type": "image/jpeg",
									"height": HEIGHT4,
									"width": WIDTH4,
									"x": X4,
									"y": Y4,
									"scale": SCALE4,
									"angle": ANGLE4,
								},

							]
						}
					],
					"background": f"{BACKGROUND}"
				},
			]
		})

		PUT_request(url,
		            payload,
		            self.API_KEY,
		            self.COOKIE)

	@wrapper_func
	def REPLICATE_TEMPLATE_SPECIFIC_PRODUCT5(self,
	                                         product_title,
	                                         product_title_suffix,
	                                         img_name,
	                                         img_id,
	                                         COPY_1_ID,
	                                         template_data):

		################################################################################
		key_list = [0, 1, 2, 3, 4]

		(HEIGHT, WIDTH, X, Y, SCALE, ANGLE, BACKGROUND,
		 HEIGHT2, WIDTH2, X2, Y2, SCALE2, ANGLE2, _,
		 HEIGHT3, WIDTH3, X3, Y3, SCALE3, ANGLE3, _,
		 HEIGHT4, WIDTH4, X4, Y4, SCALE4, ANGLE4, _,
		 HEIGHT5, WIDTH5, X5, Y5, SCALE5, ANGLE5, _)\
			= Parse_C(template_data, key_list)
		################################################################################

		url = f"https://api.printify.com/v1/shops/{self.SHOP_ID}/products/{COPY_1_ID}.json"
		payload = json.dumps({
			"id": f"{COPY_1_ID}",
			"title": f"{product_title}{product_title_suffix}",
			"print_areas": [
				{
					"variant_ids": self.VARIANT_ID,
					"placeholders": [
						{
							"position": "front",
							"images": [
								{
									"id": f"{img_id}",
									"name": f"{img_name}",
									"type": "image/jpeg",
									"height": HEIGHT,
									"width": WIDTH,
									"x": X,
									"y": Y,
									"scale": SCALE,
									"angle": ANGLE,
								},
								{
									"id": f"{img_id}",
									"name": f"{img_name}",
									"type": "image/jpeg",
									"height": HEIGHT2,
									"width": WIDTH2,
									"x": X2,
									"y": Y2,
									"scale": SCALE2,
									"angle": ANGLE2,
								},
								{
									"id": f"{img_id}",
									"name": f"{img_name}",
									"type": "image/jpeg",
									"height": HEIGHT3,
									"width": WIDTH3,
									"x": X3,
									"y": Y3,
									"scale": SCALE3,
									"angle": ANGLE3,
								},
								{
									"id": f"{img_id}",
									"name": f"{img_name}",
									"type": "image/jpeg",
									"height": HEIGHT4,
									"width": WIDTH4,
									"x": X4,
									"y": Y4,
									"scale": SCALE4,
									"angle": ANGLE4,
								},
								{
									"id": f"{img_id}",
									"name": f"{img_name}",
									"type": "image/jpeg",
									"height": HEIGHT5,
									"width": WIDTH5,
									"x": X5,
									"y": Y5,
									"scale": SCALE5,
									"angle": ANGLE5,

								},

							]
						}
					],
					"background": f"{BACKGROUND}"
				},
			]
		})

		PUT_request(url,
		            payload,
		            self.API_KEY,
		            self.COOKIE)

	@wrapper_func
	def REPLICATE_TEMPLATE_SPECIFIC_PRODUCT9(self,
	                                         product_title,
	                                         product_title_suffix,
	                                         img_name,
	                                         img_id,
	                                         COPY_1_ID,
	                                         template_data):

		################################################################################
		key_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]

		(HEIGHT, WIDTH, X, Y, SCALE, ANGLE, BACKGROUND,
		 HEIGHT2, WIDTH2, X2, Y2, SCALE2, ANGLE2, _,
		 HEIGHT3, WIDTH3, X3, Y3, SCALE3, ANGLE3, _,
		 HEIGHT4, WIDTH4, X4, Y4, SCALE4, ANGLE4, _,
		 HEIGHT5, WIDTH5, X5, Y5, SCALE5, ANGLE5, _,
		 HEIGHT6, WIDTH6, X6, Y6, SCALE6, ANGLE6, _,
		 HEIGHT7, WIDTH7, X7, Y7, SCALE7, ANGLE7, _,
		 HEIGHT8, WIDTH8, X8, Y8, SCALE8, ANGLE8, _,
		 HEIGHT9, WIDTH9, X9, Y9, SCALE9, ANGLE9, _)\
			= Parse_C(template_data, key_list)
		################################################################################

		url = f"https://api.printify.com/v1/shops/{self.SHOP_ID}/products/{COPY_1_ID}.json"
		payload = json.dumps({
			"id": f"{COPY_1_ID}",
			"title": f"{product_title}{product_title_suffix}",
			"print_areas": [
				{
					"variant_ids": self.VARIANT_ID,
					"placeholders": [
						{
							"position": "front",
							"images": [
								{
									"id": f"{img_id}",
									"name": f"{img_name}",
									"type": "image/jpeg",
									"height": HEIGHT,
									"width": WIDTH,
									"x": X,
									"y": Y,
									"scale": SCALE,
									"angle": ANGLE,
								},
								{
									"id": f"{img_id}",
									"name": f"{img_name}",
									"type": "image/jpeg",
									"height": HEIGHT2,
									"width": WIDTH2,
									"x": X2,
									"y": Y2,
									"scale": SCALE2,
									"angle": ANGLE2,
								},
								{
									"id": f"{img_id}",
									"name": f"{img_name}",
									"type": "image/jpeg",
									"height": HEIGHT3,
									"width": WIDTH3,
									"x": X3,
									"y": Y3,
									"scale": SCALE3,
									"angle": ANGLE3,
								},
								{
									"id": f"{img_id}",
									"name": f"{img_name}",
									"type": "image/jpeg",
									"height": HEIGHT4,
									"width": WIDTH4,
									"x": X4,
									"y": Y4,
									"scale": SCALE4,
									"angle": ANGLE4,
								},
								{
									"id": f"{img_id}",
									"name": f"{img_name}",
									"type": "image/jpeg",
									"height": HEIGHT5,
									"width": WIDTH5,
									"x": X5,
									"y": Y5,
									"scale": SCALE5,
									"angle": ANGLE5,

								},
								{
									"id": f"{img_id}",
									"name": f"{img_name}",
									"type": "image/jpeg",
									"height": HEIGHT6,
									"width": WIDTH6,
									"x": X6,
									"y": Y6,
									"scale": SCALE6,
									"angle": ANGLE6,

								},
								{
									"id": f"{img_id}",
									"name": f"{img_name}",
									"type": "image/jpeg",
									"height": HEIGHT7,
									"width": WIDTH7,
									"x": X7,
									"y": Y7,
									"scale": SCALE7,
									"angle": ANGLE7,

								},
								{
									"id": f"{img_id}",
									"name": f"{img_name}",
									"type": "image/jpeg",
									"height": HEIGHT8,
									"width": WIDTH8,
									"x": X8,
									"y": Y8,
									"scale": SCALE8,
									"angle": ANGLE8,

								},
								{
									"id": f"{img_id}",
									"name": f"{img_name}",
									"type": "image/jpeg",
									"height": HEIGHT9,
									"width": WIDTH9,
									"x": X9,
									"y": Y9,
									"scale": SCALE9,
									"angle": ANGLE9,

								},

							]
						}
					],
					"background": f"{BACKGROUND}"
				},
			]
		})

		PUT_request(url,
		            payload,
		            self.API_KEY,
		            self.COOKIE)


class PRODUCT_TSHIRT_AOP(PRODUCT_SIMPLE):
	def __init__(self,
	             SHOP_ID,
	             API_KEY,
	             COOKIE,
	             PRODUCT_TITLE,
	             PRODUCT_TITLE_SUFFIX,
	             id_blueprint_SIMPLE_TSHIRT_AOP,
	             id_print_provider,
	             IMAGE_VERSION,
	             PAGINATION,
	             STARTSWITH,
	             UPLOAD_STARTSWITH,
	             PRODUCT_ID,
	             VARIANT_ID,
	             variant_SIMPLE_TSHIRT_AOP):  #UPGRADED INSTANCE

		super().__init__(SHOP_ID,
		                 API_KEY,
		                 COOKIE,
		                 PRODUCT_TITLE,
		                 PRODUCT_TITLE_SUFFIX,
		                 IMAGE_VERSION,
		                 PAGINATION,
		                 STARTSWITH,
		                 UPLOAD_STARTSWITH,
		                 PRODUCT_ID,
		                 VARIANT_ID)  #INHERITED INSTANCE

		self.variant_SIMPLE_TSHIRT_AOP = variant_SIMPLE_TSHIRT_AOP
		self.id_blueprint_SIMPLE_TSHIRT_AOP = id_blueprint_SIMPLE_TSHIRT_AOP
		self.id_print_provider = id_print_provider
	
	@wrapper_func
	def REPLICATE_TEMPLATE_SIMPLE_TSHIRT_AOP(self,
	                                         product_title,
	                                         product_title_suffix,
	                                         img_name,
	                                         img_id,
	                                         template_data):
		print(img_name)
		template_description_2 = template_data["description"]

		################################################################################
		key = 3

		(FRONT_HEIGHT, FRONT_WIDTH, FRONT_X, FRONT_Y, FRONT_SCALE, FRONT_ANGLE, BACKGROUND)\
			= Parse_C2(template_data, key)

		key = 4

		(_L_SLEEVE_IMAGE_NAME,
		 _L_SLEEVE_IMAGE_ID,
		 _L_SLEEVE_HEIGHT,
		 _L_SLEEVE_WIDTH,
		 _L_SLEEVE_X,
		 _L_SLEEVE_Y,
		 _L_SLEEVE_SCALE,
		 _L_SLEEVE_ANGLE)\
			= Parse_E(template_data, key)
		################################################################################

		url = f"https://api.printify.com/v1/shops/{self.SHOP_ID}/products.json"
		payload = json.dumps({
			"title": f"{product_title}{product_title_suffix}",
			"description": f"{template_description_2}",
			"blueprint_id": self.id_blueprint_SIMPLE_TSHIRT_AOP,  # <<<<<<<<<<CHANGE
			"print_provider_id": self.id_print_provider,  # <<<<<<<<<<CHANGE
			"variants": self.variant_SIMPLE_TSHIRT_AOP,
			"print_areas": [
				{
					"variant_ids": self.VARIANT_ID,
					"placeholders": [  # 36x36inch
						{
							"position": "front",
							"images": [
								{
									"id": f"{img_id}",
									"name": f"{img_name}",
									"type": "image/jpeg",
									"height": FRONT_HEIGHT,
									"width": FRONT_WIDTH,
									"x": FRONT_X,
									"y": FRONT_Y,
									"scale": FRONT_SCALE,
									"angle": FRONT_ANGLE,
								}
							]
						},
						{
							"position": "left_sleeve",
							"images": [
								{
									"id": f"{_L_SLEEVE_IMAGE_ID}",
									"name": f"{_L_SLEEVE_IMAGE_NAME}",
									"type": "image/png",
									"height": _L_SLEEVE_HEIGHT,
									"width": _L_SLEEVE_WIDTH,
									"x": _L_SLEEVE_X,
									"y": _L_SLEEVE_Y,
									"scale": _L_SLEEVE_SCALE,
									"angle": _L_SLEEVE_ANGLE,

								}
							]
						}
					],
					"background": f"{BACKGROUND}"
				},
			]
		})

		PUT_request(url,
		            payload,
		            self.API_KEY,
		            self.COOKIE)
