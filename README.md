# Printify API Automation Tool

A comprehensive Python-based solution for automating Printify API operations, including product creation, image management, and template replication for various product types.

## 🚀 Features

- **Multi-Product Support**: Horizontal, vertical, square, and T-shirt AOP products
- **Image Management**: Automated image placement and scaling
- **Template Replication**: Copy and customize existing product templates
- **Batch Operations**: Process multiple products with different image configurations
- **Error Handling**: Comprehensive error handling and logging
- **Flexible Configuration**: Easy-to-configure settings for different use cases

## 📋 Requirements

### System Requirements
- **Python**: 3.7 or higher (3.8+ recommended)
- **RAM**: Minimum 4GB, recommended 8GB+ for large operations
- **Storage**: Minimum 100MB, recommended 1GB+ for caching
- **OS**: Windows 10/11, macOS 10.14+, or Linux (Ubuntu 18.04+)

### Dependencies
```
requests>=2.25.0
```

### API Requirements
- Valid Printify API key
- Active Printify shop account
- Proper API permissions for product management and image uploads

## 🛠️ Installation

1. **Clone or download the project**
   ```bash
   git clone <repository-url>
   cd repo_API_PRINTIFY
   ```

2. **Install Python dependencies**
   ```bash
   pip install requests
   ```

3. **Configure your settings**
   - Edit `ESSENTIAL_values.py` with your API credentials
   - Set up product templates in Printify
   - Configure product IDs and variant IDs

## ⚙️ Configuration

### Essential Configuration (`ESSENTIAL_values.py`)

Before using the tool, you must configure the following values:

#### API Configuration
```python
API_KEY = "your_printify_api_key"
COOKIE = "your_authentication_cookie"
id_SHOP = "your_shop_id"
```

#### Product Configuration
```python
PRODUCT_TITLE_0 = "Your Base Product Title"
PRODUCT_TITLE_SUFFIX_0 = ["Suffix1", "Suffix2", "Suffix3"]
IMAGE_VERSION_0 = "VERSION"
PAGINATION_0 = 10
COPY_STARTSWITH_0 = "COPY"
UPLOAD_STARTSWITH = "VERSION"
```

#### Product Template IDs
```python
id_SIMPLE_HORIZONTAL_PRODUCT = "your_horizontal_template_id"
id_SIMPLE_VERTICAL_PRODUCT = "your_vertical_template_id"
id_SIMPLE_SQUARE_PRODUCT = "your_square_template_id"
id_SIMPLE_TSHIRT_AOP = "your_tshirt_template_id"
```

## 📖 Usage

### Basic Commands

```bash
# Display product information
python METHOD_controller.py return_info

# Create simple horizontal product
python METHOD_controller.py product_simple_horizontal

# Create horizontal product with specific number of images
python METHOD_controller.py product_simple_horizontal-1-images
python METHOD_controller.py product_simple_horizontal-2-images
python METHOD_controller.py product_simple_horizontal-3-images
python METHOD_controller.py product_simple_horizontal-4-images

# Create square products
python METHOD_controller.py product_simple_square
python METHOD_controller.py product_simple_square-1-images
python METHOD_controller.py product_simple_square-2-images
python METHOD_controller.py product_simple_square-3-images
python METHOD_controller.py product_simple_square-4-images

# Create vertical products
python METHOD_controller.py product_simple_vertical
python METHOD_controller.py product_simple_vertical-1-images
python METHOD_controller.py product_simple_vertical-2-images
python METHOD_controller.py product_simple_vertical-3-images
python METHOD_controller.py product_simple_vertical-4-images
python METHOD_controller.py product_simple_vertical-5-images
python METHOD_controller.py product_simple_vertical-9-images

# Create T-shirt AOP products
python METHOD_controller.py product_simple_t_shirt_AOP

# Create specific design products
python METHOD_controller.py product_specific_design-1_horizontal
python METHOD_controller.py product_specific_design-1_vertical
```

### Advanced Usage

#### Using Argument Groups
```bash
# Horizontal products
python METHOD_controller.py --horizontal product_simple_horizontal-2-images

# Square products
python METHOD_controller.py --square product_simple_square-3-images

# Vertical products
python METHOD_controller.py --vertical product_simple_vertical-4-images

# Specific design products
python METHOD_controller.py --specific product_specific_design-1_horizontal

# Other products
python METHOD_controller.py --other product_simple_t_shirt_AOP
```

## 📁 File Structure

```
repo_API_PRINTIFY/
├── README.md                    # This file
├── requirements.md              # Detailed requirements and setup
├── ESSENTIAL_values.py          # Configuration values
├── ESSENTIAL_instance.py        # Product instances
├── METHOD_class.py              # Core product classes
├── METHOD_controller.py         # Main controller
├── METHOD_requests.py           # HTTP request handling
├── METHOD_parse.py              # Data parsing utilities
├── METHOD_wrapper.py            # Function wrapper utilities
├── help_formatter.py            # Help formatting utilities
└── __pycache__/                # Python cache files
```

## 🔧 Setup Instructions

### 1. Printify Account Setup
1. Create a Printify account
2. Generate an API key from your account settings
3. Note your shop ID
4. Create product templates for each product type you want to use

### 2. Image Upload Setup
1. Upload images to Printify following the naming convention:
   - Format: `VERSION0077.jpg` (where VERSION is your IMAGE_VERSION_0)
   - Ensure images are in the correct format and size

### 3. Product Template Setup
1. Create template products in Printify for each product type
2. Note the product IDs and variant IDs
3. Create copy products with "COPY" prefix for image replacement

### 4. Configuration
1. Edit `ESSENTIAL_values.py` with your API credentials
2. Configure product IDs and variant IDs
3. Set up image version and pagination settings
4. Test with `return_info` command

## 🐛 Troubleshooting

### Common Issues

#### "list indices must be integers or slices, not list"
- **Cause**: Incorrect parameter passing to Parse_C2 function
- **Solution**: Ensure all Parse_C2 calls use single integers, not lists

#### API Authentication Errors
- **Cause**: Invalid API key or cookie
- **Solution**: Verify your API credentials in `ESSENTIAL_values.py`

#### Missing Product Templates
- **Cause**: Product IDs not configured or templates don't exist
- **Solution**: Create templates in Printify and update IDs in configuration

#### Image Not Found
- **Cause**: Images not uploaded or naming convention mismatch
- **Solution**: Upload images with correct naming convention and check IMAGE_VERSION_0

### Error Messages

- `"Error: Instance 'simple_HZ' not found"`: Check instance configuration
- `"Parse_C error"`: Verify template data structure
- `"Wrapper function error"`: Check image and copy product lists

## 📝 Naming Conventions

### Image Files
- **Format**: `VERSION0077.jpg`
- **Example**: `VERSION0077.jpg`, `VERSION0078.jpg`

### Copy Products
- **Format**: `COPY_Your_Product_Title`
- **Example**: `COPY_Horizontal_Canvas_Wrap`

### Product Titles
- **Format**: `{PRODUCT_TITLE_0}{PRODUCT_TITLE_SUFFIX_0}`
- **Example**: `Canvas Wrap - Design 1`

## 🔄 Workflow

1. **Setup Phase**
   - Configure API credentials
   - Create product templates
   - Upload images
   - Create copy products

2. **Execution Phase**
   - Run desired command
   - Monitor output for errors
   - Verify product creation in Printify

3. **Verification Phase**
   - Check created products in Printify dashboard
   - Verify image placement and scaling
   - Test product variants

## 📚 Additional Resources

- **Printify API Documentation**: [https://printify.com/docs/](https://printify.com/docs/)
- **Requirements File**: See `requirements.md` for detailed setup instructions
- **Help Command**: Run `python help_formatter.py` for formatted help

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## ⚠️ Disclaimer

This tool is designed for automation of Printify API operations. Please ensure compliance with Printify's terms of service and API usage guidelines. The authors are not responsible for any misuse or violations of Printify's policies.

---

**For support and questions**, please refer to the troubleshooting section above or check the `requirements.md` file for detailed documentation. 