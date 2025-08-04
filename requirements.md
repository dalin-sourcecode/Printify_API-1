# Printify API Project Requirements

## Project Overview
This project provides a comprehensive Python-based solution for automating Printify API operations, including product creation, image management, and template replication for various product types (horizontal, vertical, square, and T-shirt AOP).

## System Requirements

### Operating System
- Windows 10/11
- macOS 10.14+
- Linux (Ubuntu 18.04+, CentOS 7+)

### Python Version
- Python 3.7 or higher
- Python 3.8+ recommended for optimal performance

### Memory Requirements
- Minimum: 4GB RAM
- Recommended: 8GB+ RAM for large batch operations

### Storage
- Minimum: 100MB free space
- Recommended: 1GB+ for image caching and logs

## Python Dependencies

### Core Dependencies
```
requests>=2.25.0
```

### Optional Dependencies
```
pprint (built-in Python module)
json (built-in Python module)
argparse (built-in Python module)
```

## API Requirements

### Printify API Access
- Valid Printify API key
- Active Printify shop account
- Proper API permissions for:
  - Product management
  - Image uploads
  - Product creation and modification

### API Rate Limits
- Respect Printify API rate limits
- Implement appropriate delays between requests
- Monitor API usage to avoid throttling

## Configuration Requirements

### Essential Values (ESSENTIAL_values.py)
The following values must be configured before use:

#### API Configuration
- `API_KEY`: Your Printify API key
- `COOKIE`: Authentication cookie value
- `id_SHOP`: Your Printify shop ID

#### Product Configuration
- `PRODUCT_TITLE_0`: Base product title
- `PRODUCT_TITLE_SUFFIX_0`: Product title suffix array
- `IMAGE_VERSION_0`: Image version identifier
- `PAGINATION_0`: Number of pages to process
- `COPY_STARTSWITH_0`: Copy product identifier prefix
- `UPLOAD_STARTSWITH`: Upload file identifier prefix

#### Product IDs
- `id_SIMPLE_HORIZONTAL_PRODUCT`: Horizontal product template ID
- `id_SIMPLE_VERTICAL_PRODUCT`: Vertical product template ID
- `id_SIMPLE_SQUARE_PRODUCT`: Square product template ID
- `id_SIMPLE_TSHIRT_AOP`: T-shirt AOP template ID
- `id_SPECIFIC_HORIZONTAL_PRODUCT`: Specific horizontal product ID
- `id_SPECIFIC_VERTICAL_PRODUCT`: Specific vertical product ID

#### Variant IDs
- `id_variant_SIMPLE_PRODUCT`: Array of simple product variant IDs
- `id_variant_SIMPLE_TSHIRT_AOP`: Array of T-shirt variant IDs
- Various specific product variant ID arrays

#### T-shirt Specific
- `id_blueprint_SIMPLE_TSHIRT_AOP`: Blueprint ID for T-shirts
- `id_print_provider`: Print provider ID
- `variant_SIMPLE_TSHIRT_AOP`: T-shirt variant configuration

## File Structure Requirements

### Required Files
```
repo_API_PRINTIFY/
├── ESSENTIAL_values.py          # Configuration values
├── ESSENTIAL_instance.py        # Product instances
├── METHOD_class.py              # Core product classes
├── METHOD_controller.py         # Main controller
├── METHOD_requests.py           # HTTP request handling
├── METHOD_parse.py              # Data parsing utilities
├── METHOD_wrapper.py            # Function wrapper
└── requirements.md              # This file
```

### Optional Files
```
repo_API_PRINTIFY/
├── tester.py                    # Testing utilities
└── logs/                        # Log directory (auto-created)
```

## Setup Instructions

### 1. Environment Setup
```bash
# Clone or download the project
cd repo_API_PRINTIFY

# Install Python dependencies
pip install requests

# Verify Python version
python --version  # Should be 3.7+
```

### 2. Configuration
1. Edit `ESSENTIAL_values.py`
2. Update API credentials:
   - Replace `API_KEY` with your actual Printify API key
   - Update `COOKIE` value
   - Set your `id_SHOP` value
3. Configure product settings:
   - Set appropriate product titles and suffixes
   - Update image version and pagination settings
   - Configure product and variant IDs

### 3. Template Setup
1. Create template products in Printify
2. Note the product IDs and variant IDs
3. Update the corresponding values in `ESSENTIAL_values.py`
4. Create copy products with "COPY" prefix in titles

### 4. Image Upload
1. Upload images to Printify following naming convention
2. Images should start with `UPLOAD_STARTSWITH` + `IMAGE_VERSION_0`
3. Example: "VERSION0014.jpg"

## Usage Requirements

### Command Line Interface
The project uses argparse for command-line operations:

```bash
# Basic usage
python METHOD_controller.py <action>

# Available actions:
python METHOD_controller.py return_info
python METHOD_controller.py product_simple_horizontal
python METHOD_controller.py product_simple_square
python METHOD_controller.py product_simple_vertical
python METHOD_controller.py product_simple_t_shirt_AOP
```

### Product Types Supported
- **Simple Products**: Single design across all variants
- **Specific Products**: Custom designs for specific variants
- **T-shirt AOP**: All-over-print T-shirts
- **Multi-image Products**: Products with 1-9 images

### Image Requirements
- Format: JPEG recommended
- Naming convention: Must start with configured prefix
- Size: Follow Printify's image requirements
- Quality: High resolution for best results

## Error Handling Requirements

### Built-in Error Handling
The project includes comprehensive error handling for:
- API request failures
- Data parsing errors
- Missing configuration values
- Network connectivity issues
- Invalid product/variant IDs

### Error Recovery
- Graceful degradation on errors
- Detailed error messages
- Continuation of batch operations
- Logging of error conditions

## Performance Requirements

### API Optimization
- Efficient pagination handling
- Batch processing capabilities
- Rate limit compliance
- Connection pooling

### Memory Management
- Efficient data structures
- Proper cleanup of large datasets
- Memory-conscious image processing

## Security Requirements

### API Key Security
- Never commit API keys to version control
- Use environment variables for sensitive data
- Implement proper key rotation
- Monitor API usage for anomalies

### Data Protection
- Secure handling of product data
- Proper authentication validation
- Input sanitization
- Error message security (no sensitive data exposure)

## Testing Requirements

### Unit Testing
- Test individual functions and methods
- Validate error handling
- Test configuration loading
- Verify API response parsing

### Integration Testing
- Test complete workflows
- Validate API interactions
- Test error scenarios
- Performance testing

## Maintenance Requirements

### Regular Updates
- Monitor Printify API changes
- Update dependencies regularly
- Review and update product configurations
- Maintain error handling effectiveness

### Monitoring
- Track API usage and limits
- Monitor error rates
- Log performance metrics
- Validate data integrity

## Troubleshooting Requirements

### Common Issues
- API authentication failures
- Missing product templates
- Image upload problems
- Rate limiting issues
- Configuration errors

### Debugging Tools
- Detailed error messages
- Logging capabilities
- Configuration validation
- API response inspection

## Support and Documentation

### Required Documentation
- API endpoint documentation
- Configuration guide
- Troubleshooting guide
- Usage examples

### Support Channels
- Error logging and reporting
- Configuration validation
- Performance monitoring
- User feedback collection

## Version Compatibility

### Printify API Version
- Compatible with current Printify API
- Monitor for API version changes
- Update code for breaking changes

### Python Version Support
- Python 3.7+ compatibility
- Test with multiple Python versions
- Maintain backward compatibility where possible

## License and Legal Requirements

### Usage Terms
- Comply with Printify's Terms of Service
- Respect API usage limits
- Follow data protection regulations
- Maintain proper attribution

### Distribution
- Include license information
- Provide source code access
- Document modifications
- Maintain version history 