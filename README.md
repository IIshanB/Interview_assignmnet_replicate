

API Usage
Generate Image

Endpoint: /api/generate/

Method: POST

Request Body:
{
  "prompt": prompt,
  "width": 768,
  "height": 768
}
Response:

    200 OK:
        {
  "generated_image_url": "https://example.com/generated_image.png"
}
    400 Bad Request:
        {
  "error": "Invalid input parameters."
}

    500 Internal Server Error:
    {
  "error": "Error during image generation."
}

