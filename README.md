## API Usage

### Generate Image

**Endpoint**: `/api/generate/`  
**Method**: `POST`

#### Request Body

The request should be a JSON object containing the following parameters:

```json
{
  "prompt": prompt,
  "width": 768,
  "height": 768
}

prompt (string, required): The text prompt for image generation.
width (integer, optional): The width of the generated image (default is 768).
height (integer, optional): The height of the generated image (default is 768).

Responses

    200 OK
        Description: The image was generated successfully.
        Response Body:
{
  "generated_image_url": "https://example.com/generated_image.png"
}
400 Bad Request

    Description: Invalid input parameters.
    Response Body:
{
  "error": "Invalid input parameters."
}


### Explanation of Formatting

1. **Heading**: The section is clearly labeled as "API Usage" and the specific action is titled "Generate Image."
2. **Endpoint and Method**: Clearly states the HTTP method and endpoint URL.
3. **Request Body**: Describes the expected request format and parameters. This includes both the example and the required/optional statuses of the fields.
4. **Responses**: Provides detailed descriptions and examples for each possible response, ensuring users understand what to expect.

Feel free to incorporate this section into your README file to ensure clear and concise documentation for your API usage. Let me know if you need any further adjustments or additions!
