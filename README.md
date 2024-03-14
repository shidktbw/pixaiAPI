# 💬 Pixai.art

![pixai-1651286186430165996-和風？](https://github.com/shidktbw/pixaiAPI/assets/112849918/68e99857-3851-428c-952f-1f256eefacba)

An *unofficial* API for Pixai.art for Python using request


## 💻 Installation
```bash
pip install PixaiAPI
```


## 🔑 Get Token
The token is needed for authorization and operation of requests from your account
1. Open DevTools in your browser
2. Go to Storage -> Local Storage -> `api.pixai.art:token`
3. Copy `value`

 ᅠ 
## 📙 Example
```Python
from pixai import PixaiAPI

client = PixaiAPI('TOKEN')

startGeneration = client.createGenerationTask(
    prompts='girl, white hair, winter',
    steps='20',
    modelId='1648918127446573124'
)

imageurlurl = client.getTaskById(startGeneration)
image = client.DownloadImage(imageurlurl)
```

## ⛏️How is work (briefly)
Due to the unofficial nature of the API, the approach to image generation deviates from standard methods

1. Send `createGenerationTask` to initiate image generation
2. Receive `generationId` as acknowledgment

To track the progress or retrieve the generated image, use the getTaskById endpoint, passing in your generationId

3. Use `getTaskById` with your `generationId` to get a link to the image
4. Dowload image by link

Workflow Summary
createGenerationTask -> receive generationId -> getTaskById with generationId -> receive url_to_image -> Download image from link

For all generation parameters check [it](https://github.com/shidktbw/pixaiAPI/blob/main/pixai/payloads.py#L5)https://github.com/shidktbw/pixaiAPI/blob/main/pixai/payloads.py#L5

