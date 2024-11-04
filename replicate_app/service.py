import httpx
from django.conf import settings

class ReplicateService:
    @staticmethod
    def generate_image(prompt: str, width: int = 768, height: int = 768) -> str:
        url = "https://api.replicate.com/v1/predictions"
        headers = {
            "Authorization": f"Bearer {settings.REPLICATE_API_TOKEN}",
            "Content-Type": "application/json",
            "Prefer": "wait"
        }
        data = {
            "version": "ac732df83cea7fff18b8472768c88ad041fa750ff7682a21affe81863cbe77e4",
            "input": {
                "width": width,
                "height": height,
                "prompt": prompt,
                "scheduler": "K_EULER",
                "num_outputs": 1,
                "guidance_scale": 7.5,
                "num_inference_steps": 50
            }
        }

        with httpx.Client() as client:
            response = client.post(url, headers=headers, json=data)

            if response.status_code != 200:
                raise Exception(f"Error generating image: {response.status_code} - {response.text}")

            result = response.json()
            return result.get("output")  # URL of generated image
