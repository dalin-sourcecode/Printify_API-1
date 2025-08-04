#####################################################################################
from ESSENTIAL_instance import INSTANCES
import argparse
#####################################################################################

"""
YOU MAY WANT TO COLLAPSE ALL FUNCTIONS WITH THIS SCRIPT TO GET A BIRD'S EYE VIEW ON THE CODE.
 
PRODUCT: THIS IS BASED ON THE GALLERY CANVAS WRAP AND UNISEX AOP TSHIRT
ALL FIELDS: I LEFT EXAMPLES OF WHAT IS NEEDED 
THE if __name__ == "__main__": WILL BE YOUR MAIN FOCUS
SIMPLE PRODUCT: THIS IS A PRODUCT THAT DOES NOT HAVE A SPECIFIC DESIGN, ALL SIZES OR VARIANTS WILL HAVE THE SAME DESIGN

SPECIFIC PRODUCT: THIS IS A PRODUCT THAT YOU HAVE CHOSEN TO HAVE A SPECIFIC DESIGN. THIS SCRIPT ONLY EXPECTS ONE DESIGN
BUT YOU CAN USE IT AS A TEMPLATE TO BUILD ON BY ADDING MORE IMAGES TO THE SPECIFIC

THIS SCRIPT DEPENDS ON THE FILE NAME OF YOUR UPLOADS AND THE STARTING NAME OF THE DUPLICATES WHICH IS "COPY"

MY UPLOAD FILE NAMING CONVENTION: VERSION0077.jpg

DUPLICATE PRODUCT NAMING CONVENTION: COPY_YOUR_PRODUCT_TITLE (the underscores are just for example purposes, the "COPY" IS THE MOST IMPORTANT

YOU MAY NOT WANT TO CREATE THE DUPLICATES BUT BELIEVE ME I LOOKED FOR A WAY AROUND IT AND PRINTIFY HAS A BUG WHEN USING THE MIRROR EFFECT, 
IT WILL NOT WORK PROPERLY FROM THE API. BELIEVE ME I TRIED.
SO,
IF YOU HAVE 7 IMAGES THAT YOU WANT TO PUT ON A PRODUCT, YOU WILL NEED TO MAKE 7 DUPLICATES OF THE TEMPLATE PRODUCT THAT YOU HAVE SETUP, 
THIS SCRIPT WILL LOOK FOR "COPY" IN THE TITLE NAME AND CHANGE THE IMAGE TO THE NEXT AVAILABLE ACCORDING TO THE NAMING CONVENTION 
THE PRODUCT ID'S REPRESENT YOUR TEMPLATE PRODUCT THAT YOU WANT TO COPY ITS CONFIG TO A DUPLICATE PRODUCT

IN THIS CASE IT WILL LOOK FOR THE UPLOAD THAT STARTS WITH "VERSION" 

THEN IT WILL LOOK FOR THE NEXT DUPLICATE PRODUCT THAT STARTS WITH "COPY"
"""
"""
This script does work. If you run into an issue where you add more images down the 
line and for whatever reason it is only creating one product, you may need to increase
the pagination. Because the image is probably at the beginning
"""

def main():
	parser = argparse.ArgumentParser(
		description="PRINTIFY API Operations - Automate product creation and management",
		formatter_class=argparse.RawDescriptionHelpFormatter,
		epilog="""
Examples:
  python METHOD_controller.py return_info
  python METHOD_controller.py product_simple_horizontal
  python METHOD_controller.py product_simple_t_shirt_AOP

For more information, see the requirements.md file.
		"""
	)
	
	# Group the actions by category for better organization
	horizontal_group = parser.add_argument_group('Horizontal Products')
	horizontal_group.add_argument("--horizontal", choices=[
		"return_info",
		"product_simple_horizontal",
		"product_simple_horizontal-1-images",
		"product_simple_horizontal-2-images",
		"product_simple_horizontal-3-images",
		"product_simple_horizontal-4-images"
	], help="Horizontal product operations")
	
	square_group = parser.add_argument_group('Square Products')
	square_group.add_argument("--square", choices=[
		"product_simple_square",
		"product_simple_square-1-images",
		"product_simple_square-2-images",
		"product_simple_square-3-images",
		"product_simple_square-4-images"
	], help="Square product operations")
	
	vertical_group = parser.add_argument_group('Vertical Products')
	vertical_group.add_argument("--vertical", choices=[
		"product_simple_vertical",
		"product_simple_vertical-1-images",
		"product_simple_vertical-2-images",
		"product_simple_vertical-3-images",
		"product_simple_vertical-4-images",
		"product_simple_vertical-5-images",
		"product_simple_vertical-9-images"
	], help="Vertical product operations")
	
	specific_group = parser.add_argument_group('Specific Design Products')
	specific_group.add_argument("--specific", choices=[
		"product_specific_design-1_horizontal",
		"product_specific_design-1_vertical"
	], help="Specific design product operations")
	
	other_group = parser.add_argument_group('Other Products')
	other_group.add_argument("--other", choices=[
		"product_vertical-1",
		"product_simple_t_shirt_AOP"
	], help="Other product operations")
	
	# Main action argument (keeping for backward compatibility)
	parser.add_argument("action", nargs='?', choices=[
		"return_info",
		"product_simple_horizontal",
		"product_simple_horizontal-1-images",
		"product_simple_horizontal-2-images",
		"product_simple_horizontal-3-images",
		"product_simple_horizontal-4-images",
		#########################################
		"product_simple_square",
		"product_simple_square-1-images",
		"product_simple_square-2-images",
		"product_simple_square-3-images",
		"product_simple_square-4-images",
		#########################################
		"product_simple_vertical",
		"product_simple_vertical-1-images",
		"product_simple_vertical-2-images",
		"product_simple_vertical-3-images",
		"product_simple_vertical-4-images",
		"product_simple_vertical-5-images",
		"product_simple_vertical-9-images",
		#########################################
		"product_specific_design-1_horizontal",
		"product_specific_design-1_vertical",
		#########################################
		"product_vertical-1",
		"product_simple_t_shirt_AOP"
		#########################################
	], help="Action to perform")

	args = parser.parse_args()

	# Show help if no action specified
	if not any([args.horizontal, args.square, args.vertical, args.specific, args.other, args.action]):
		parser.print_help()
		return

	try:

		if args.horizontal == "return_info" or args.action == "return_info":
			try:
				return_info(INSTANCES["simple_HZ"]())
			except KeyError:
				print("Error: Instance 'simple_HZ' not found in INSTANCES dictionary")
			except Exception as e:
				print(f"Error accessing simple_HZ instance: {e}")

		elif args.horizontal == "product_simple_horizontal" or args.action == "product_simple_horizontal":
			try:
				simple_HZ(INSTANCES["simple_HZ"]())
			except KeyError:
				print("Error: Instance 'simple_HZ' not found in INSTANCES dictionary")
			except Exception as e:
				print(f"Error in product_simple_horizontal: {e}")

		elif args.horizontal == "product_simple_horizontal-1-images" or args.action == "product_simple_horizontal-1-images":
			try:
				simple_HZ_1(INSTANCES["simple_HZ_max4"]())
			except KeyError:
				print("Error: Instance 'simple_HZ_max4' not found in INSTANCES dictionary")
			except Exception as e:
				print(f"Error in product_simple_horizontal-1-images: {e}")

		elif args.horizontal == "product_simple_horizontal-2-images" or args.action == "product_simple_horizontal-2-images":
			try:
				simple_HZ_2(INSTANCES["simple_HZ_max4"]())
			except KeyError:
				print("Error: Instance 'simple_HZ_max4' not found in INSTANCES dictionary")
			except Exception as e:
				print(f"Error in product_simple_horizontal-2-images: {e}")

		elif args.horizontal == "product_simple_horizontal-3-images" or args.action == "product_simple_horizontal-3-images":
			try:
				simple_HZ_3(INSTANCES["simple_HZ_max4"]())
			except KeyError:
				print("Error: Instance 'simple_HZ_max4' not found in INSTANCES dictionary")
			except Exception as e:
				print(f"Error in product_simple_horizontal-3-images: {e}")

		elif args.horizontal == "product_simple_horizontal-4-images" or args.action == "product_simple_horizontal-4-images":
			try:
				simple_HZ_4(INSTANCES["simple_HZ_max4"]())
			except KeyError:
				print("Error: Instance 'simple_HZ_max4' not found in INSTANCES dictionary")
			except Exception as e:
				print(f"Error in product_simple_horizontal-4-images: {e}")
		##########################################################
		elif args.square == "product_simple_square" or args.action == "product_simple_square":
			try:
				simple_SQ(INSTANCES["simple_SQ"]())
			except KeyError:
				print("Error: Instance 'simple_SQ' not found in INSTANCES dictionary")
			except Exception as e:
				print(f"Error in product_simple_square: {e}")

		elif args.square == "product_simple_square-1-images" or args.action == "product_simple_square-1-images":
			try:
				simple_SQ_1(INSTANCES["simple_SQ_max4"]())
			except KeyError:
				print("Error: Instance 'simple_SQ_max4' not found in INSTANCES dictionary")
			except Exception as e:
				print(f"Error in product_simple_square-1-images: {e}")

		elif args.square == "product_simple_square-2-images" or args.action == "product_simple_square-2-images":
			try:
				simple_SQ_2(INSTANCES["simple_SQ_max4"]())
			except KeyError:
				print("Error: Instance 'simple_SQ_max4' not found in INSTANCES dictionary")
			except Exception as e:
				print(f"Error in product_simple_square-2-images: {e}")

		elif args.square == "product_simple_square-3-images" or args.action == "product_simple_square-3-images":
			try:
				simple_SQ_3(INSTANCES["simple_SQ_max4"]())
			except KeyError:
				print("Error: Instance 'simple_SQ_max4' not found in INSTANCES dictionary")
			except Exception as e:
				print(f"Error in product_simple_square-3-images: {e}")

		elif args.square == "product_simple_square-4-images" or args.action == "product_simple_square-4-images":
			try:
				simple_SQ_4(INSTANCES["simple_SQ_max4"]())
			except KeyError:
				print("Error: Instance 'simple_SQ_max4' not found in INSTANCES dictionary")
			except Exception as e:
				print(f"Error in product_simple_square-4-images: {e}")
		##########################################################
		elif args.vertical == "product_simple_vertical" or args.action == "product_simple_vertical":
			try:
				simple_VT(INSTANCES["simple_VT"]())
			except KeyError:
				print("Error: Instance 'simple_VT' not found in INSTANCES dictionary")
			except Exception as e:
				print(f"Error in product_simple_vertical: {e}")

		elif args.vertical == "product_simple_vertical-1-images" or args.action == "product_simple_vertical-1-images":
			try:
				simple_VT_1(INSTANCES["simple_VT_max9"]())
			except KeyError:
				print("Error: Instance 'simple_VT_max9' not found in INSTANCES dictionary")
			except Exception as e:
				print(f"Error in product_simple_vertical-1-images: {e}")

		elif args.vertical == "product_simple_vertical-2-images" or args.action == "product_simple_vertical-2-images":
			try:
				simple_VT_2(INSTANCES["simple_VT_max9"]())
			except KeyError:
				print("Error: Instance 'simple_VT_max9' not found in INSTANCES dictionary")
			except Exception as e:
				print(f"Error in product_simple_vertical-2-images: {e}")

		elif args.vertical == "product_simple_vertical-3-images" or args.action == "product_simple_vertical-3-images":
			try:
				simple_VT_3(INSTANCES["simple_VT_max9"]())
			except KeyError:
				print("Error: Instance 'simple_VT_max9' not found in INSTANCES dictionary")
			except Exception as e:
				print(f"Error in product_simple_vertical-3-images: {e}")

		elif args.vertical == "product_simple_vertical-4-images" or args.action == "product_simple_vertical-4-images":
			try:
				simple_VT_4(INSTANCES["simple_VT_max9"]())
			except KeyError:
				print("Error: Instance 'simple_VT_max9' not found in INSTANCES dictionary")
			except Exception as e:
				print(f"Error in product_simple_vertical-4-images: {e}")

		elif args.vertical == "product_simple_vertical-5-images" or args.action == "product_simple_vertical-5-images":
			try:
				simple_VT_5(INSTANCES["simple_VT_max9"]())
			except KeyError:
				print("Error: Instance 'simple_VT_max9' not found in INSTANCES dictionary")
			except Exception as e:
				print(f"Error in product_simple_vertical-5-images: {e}")

		elif args.vertical == "product_simple_vertical-9-images" or args.action == "product_simple_vertical-9-images":
			try:
				simple_VT_9(INSTANCES["simple_VT_max9"]())
			except KeyError:
				print("Error: Instance 'simple_VT_max9' not found in INSTANCES dictionary")
			except Exception as e:
				print(f"Error in product_simple_vertical-9-images: {e}")
		##########################################################
		elif args.specific == "product_specific_design-1_horizontal" or args.action == "product_specific_design-1_horizontal":
			try:
				simple_HZ_spc(INSTANCES["specific_HZ"]())
			except KeyError:
				print("Error: Instance 'specific_HZ' not found in INSTANCES dictionary")
			except Exception as e:
				print(f"Error in product_specific_design-1_horizontal: {e}")

		elif args.specific == "product_specific_design-1_vertical" or args.action == "product_specific_design-1_vertical":
			try:
				simple_VT_spc(INSTANCES["specific_VT"]())
			except KeyError:
				print("Error: Instance 'specific_VT' not found in INSTANCES dictionary")
			except Exception as e:
				print(f"Error in product_specific_design-1_vertical: {e}")
		##########################################################
		elif args.other == "product_vertical-1" or args.action == "product_vertical-1": #not sure come back to this
			try:
				simple_VT_prd(INSTANCES["simple_SQ"]())
			except KeyError:
				print("Error: Instance 'simple_SQ' not found in INSTANCES dictionary")
			except Exception as e:
				print(f"Error in product_vertical-1: {e}")

		elif args.other == "product_simple_t_shirt_AOP" or args.action == "product_simple_t_shirt_AOP":
			try:
				simple_TAOP(INSTANCES["simple_TAOP"]())
			except KeyError:
				print("Error: Instance 'simple_TAOP' not found in INSTANCES dictionary")
			except Exception as e:
				print(f"Error in product_simple_t_shirt_AOP: {e}")

	except Exception as e:
		print(f"Main error: {e}")

#####################################################################

def return_info(class_instance):
	try:
		class_instance.RETURN_INFO()
	except Exception as e:
		print(f"return_info error: {e}")

def simple_HZ(class_instance):
	try:
		class_instance.REPLICATE_TEMPLATE_SIMPLE_PRODUCT()
	except Exception as e:
		print(f"simple_HZ error: {e}")

def simple_HZ_1(class_instance):
	try:
		class_instance.REPLICATE_TEMPLATE_SPECIFIC_PRODUCT1()
	except Exception as e:
		print(f"simple_HZ_1 error: {e}")

def simple_HZ_2(class_instance):
	try:
		class_instance.REPLICATE_TEMPLATE_SPECIFIC_PRODUCT2()
	except Exception as e:
		print(f"simple_HZ_2 error: {e}")

def simple_HZ_3(class_instance):
	try:
		class_instance.REPLICATE_TEMPLATE_SPECIFIC_PRODUCT3()
	except Exception as e:
		print(f"simple_HZ_3 error: {e}")

def simple_HZ_4(class_instance):
	try:
		class_instance.REPLICATE_TEMPLATE_SPECIFIC_PRODUCT4()
	except Exception as e:
		print(f"simple_HZ_4 error: {e}")
##########################################################
def simple_SQ(class_instance):
	try:
		class_instance.REPLICATE_TEMPLATE_SIMPLE_PRODUCT()
	except Exception as e:
		print(f"simple_SQ error: {e}")

def simple_SQ_1(class_instance):
	try:
		class_instance.REPLICATE_TEMPLATE_SPECIFIC_PRODUCT1()
	except Exception as e:
		print(f"simple_SQ_1 error: {e}")

def simple_SQ_2(class_instance):
	try:
		class_instance.REPLICATE_TEMPLATE_SPECIFIC_PRODUCT2()
	except Exception as e:
		print(f"simple_SQ_2 error: {e}")

def simple_SQ_3(class_instance):
	try:
		class_instance.REPLICATE_TEMPLATE_SPECIFIC_PRODUCT3()
	except Exception as e:
		print(f"simple_SQ_3 error: {e}")

def simple_SQ_4(class_instance):
	try:
		class_instance.REPLICATE_TEMPLATE_SPECIFIC_PRODUCT4()
	except Exception as e:
		print(f"simple_SQ_4 error: {e}")
##########################################################
def simple_VT(class_instance):
	try:
		class_instance.REPLICATE_TEMPLATE_SIMPLE_PRODUCT()
	except Exception as e:
		print(f"simple_VT error: {e}")

def simple_VT_1(class_instance):
	try:
		class_instance.REPLICATE_TEMPLATE_SPECIFIC_PRODUCT1()
	except Exception as e:
		print(f"simple_VT_1 error: {e}")

def simple_VT_2(class_instance):
	try:
		class_instance.REPLICATE_TEMPLATE_SPECIFIC_PRODUCT2()
	except Exception as e:
		print(f"simple_VT_2 error: {e}")

def simple_VT_3(class_instance):
	try:
		class_instance.REPLICATE_TEMPLATE_SPECIFIC_PRODUCT3()
	except Exception as e:
		print(f"simple_VT_3 error: {e}")

def simple_VT_4(class_instance):
	try:
		class_instance.REPLICATE_TEMPLATE_SPECIFIC_PRODUCT4()
	except Exception as e:
		print(f"simple_VT_4 error: {e}")

def simple_VT_5(class_instance):
	try:
		class_instance.REPLICATE_TEMPLATE_SPECIFIC_PRODUCT5()
	except Exception as e:
		print(f"simple_VT_5 error: {e}")

def simple_VT_9(class_instance):
	try:
		class_instance.REPLICATE_TEMPLATE_SPECIFIC_PRODUCT9()
	except Exception as e:
		print(f"simple_VT_9 error: {e}")
##########################################################
def simple_VT_spc(class_instance):
	try:
		class_instance.REPLICATE_TEMPLATE_SPECIFIC_PRODUCT()
	except Exception as e:
		print(f"simple_VT_spc error: {e}")

def simple_HZ_spc(class_instance):
	try:
		class_instance.REPLICATE_TEMPLATE_SPECIFIC_PRODUCT()
	except Exception as e:
		print(f"simple_HZ_spc error: {e}")
##########################################################
def simple_VT_prd(class_instance):
	try:
		class_instance.REPLICATE_TEMPLATE_SPECIFIC_PRODUCT()
	except Exception as e:
		print(f"simple_VT_prd error: {e}")

def simple_TAOP(class_instance):
	try:
		class_instance.REPLICATE_TEMPLATE_SIMPLE_TSHIRT_AOP()
	except Exception as e:
		print(f"simple_TAOP error: {e}")

if __name__ == "__main__":
	main()