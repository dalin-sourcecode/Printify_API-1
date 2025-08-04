#!/usr/bin/env python3
"""
Help Formatter for Printify API Controller
This script provides a more readable help output for the METHOD_controller.py
"""

def print_formatted_help():
    """Print a formatted, readable help message"""
    
    print("=" * 80)
    print("PRINTIFY API CONTROLLER - HELP")
    print("=" * 80)
    print()
    print("DESCRIPTION:")
    print("  This tool automates Printify API operations for product creation and management.")
    print("  It supports various product types including horizontal, vertical, square, and T-shirt products.")
    print()
    
    print("USAGE:")
    print("  python METHOD_controller.py <action>")
    print("  python METHOD_controller.py -h")
    print("  python METHOD_controller.py --help")
    print()
    
    print("AVAILABLE ACTIONS:")
    print()
    
    print("  INFORMATION:")
    print("    return_info                    - Display product information and data")
    print()
    
    print("  HORIZONTAL PRODUCTS:")
    print("    product_simple_horizontal      - Create simple horizontal product")
    print("    product_simple_horizontal-1-images  - Horizontal product with 1 image")
    print("    product_simple_horizontal-2-images  - Horizontal product with 2 images")
    print("    product_simple_horizontal-3-images  - Horizontal product with 3 images")
    print("    product_simple_horizontal-4-images  - Horizontal product with 4 images")
    print()
    
    print("  SQUARE PRODUCTS:")
    print("    product_simple_square          - Create simple square product")
    print("    product_simple_square-1-images      - Square product with 1 image")
    print("    product_simple_square-2-images      - Square product with 2 images")
    print("    product_simple_square-3-images      - Square product with 3 images")
    print("    product_simple_square-4-images      - Square product with 4 images")
    print()
    
    print("  VERTICAL PRODUCTS:")
    print("    product_simple_vertical        - Create simple vertical product")
    print("    product_simple_vertical-1-images    - Vertical product with 1 image")
    print("    product_simple_vertical-2-images    - Vertical product with 2 images")
    print("    product_simple_vertical-3-images    - Vertical product with 3 images")
    print("    product_simple_vertical-4-images    - Vertical product with 4 images")
    print("    product_simple_vertical-5-images    - Vertical product with 5 images")
    print("    product_simple_vertical-9-images    - Vertical product with 9 images")
    print()
    
    print("  SPECIFIC DESIGN PRODUCTS:")
    print("    product_specific_design-1_horizontal - Specific horizontal design")
    print("    product_specific_design-1_vertical   - Specific vertical design")
    print()
    
    print("  OTHER PRODUCTS:")
    print("    product_vertical-1             - Special vertical product")
    print("    product_simple_t_shirt_AOP     - T-shirt All-Over-Print")
    print()
    
    print("EXAMPLES:")
    print("  python METHOD_controller.py return_info")
    print("  python METHOD_controller.py product_simple_horizontal")
    print("  python METHOD_controller.py product_simple_t_shirt_AOP")
    print("  python METHOD_controller.py product_simple_vertical-3-images")
    print()
    
    print("CONFIGURATION:")
    print("  Before using this tool, make sure to:")
    print("  1. Configure ESSENTIAL_values.py with your API credentials")
    print("  2. Set up product templates in Printify")
    print("  3. Upload images following the naming convention")
    print("  4. Create copy products with 'COPY' prefix")
    print()
    
    print("ERROR HANDLING:")
    print("  The tool includes comprehensive error handling for:")
    print("  - API authentication failures")
    print("  - Network connectivity issues")
    print("  - Missing configuration values")
    print("  - Invalid product/variant IDs")
    print()
    
    print("FOR MORE INFORMATION:")
    print("  See the requirements.md file for detailed setup and usage instructions.")
    print()
    print("=" * 80)

if __name__ == "__main__":
    print_formatted_help() 