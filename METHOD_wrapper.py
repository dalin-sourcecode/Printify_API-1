def wrapper_func(func):

	def wrapper(self):
		try:
			for (product_title_suffix,
			     image_name,
			     image_id,
			     copy_id) in (zip(self.PRODUCT_TITLE_SUFFIX,
			                      self.list_image_name,
			                      self.list_image_id,
			                      self.list_copy_id)):  # Here we loop through 4 lists at the same time using zip

				func(self,
				     self.PRODUCT_TITLE,
				     product_title_suffix,
				     image_name,
				     image_id,
				     copy_id,
				     self.template_data)
		except Exception as e:
			print(f"Wrapper function error: {e}")

	return wrapper