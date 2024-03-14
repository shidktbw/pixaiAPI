#default settings
createGenerationTask = r"""
{
  "query": "mutation createGenerationTask($parameters: JSONObject!) {createGenerationTask(parameters: $parameters) {    ...TaskBase}} fragment TaskBase on Task {id  userId  parameters  outputs  artworkId  artworkIds  artworks {createdAt  hidePrompts  id  isNsfw  isSensitive  mediaId  title  updatedAt  flag {      ...ModerationFlagBase}}  status\n  priority  runnerId\n  startedAt\n  endAt createdAt  updatedAt  favoritedAt  media {...MediaBase} type {type model} retryCount}fragment ModerationFlagBase on ModerationFlag {  status  isSensitive  isMinors  isRealistic  shouldBlur  isWarned  isAppealable} fragment MediaBase on Media {  id type  width  height  urls {variant url} imageType  fileUrl  duration  thumbnailUrl  hlsUrl  size  flag {...ModerationFlagBase}}",
  "variables": {
    "parameters": {
      "prompts": "girl",
      "extra": {},
      "negativePrompts": "worst quality, large head, low quality, extra digits, bad eye,  EasyNegativeV2,  ng_deepnegative_v1_75t",
      "samplingSteps": 1,
      "samplingMethod": "DPM++ 2M Karras",
      "cfgScale": 6,
      "autoPublish": false,
      "priority": 1000,
      "width": 512,
      "height": 768,
      "clipSkip": 2,
      "modelId": "1648918127446573124",
      "controlNets": []
    }
  }
}

"""

getTaskById = r"""
{"query": " query getTaskById($id: ID!) {task(id: $id) {...TaskBase}}fragment TaskBase on Task {id artworks {mediaId}media {...MediaBase}}fragment MediaBase on Media {urls {variant url}}",
  "variables": {
    "id":""}}		
"""
