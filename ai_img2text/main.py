from transformers import TrOCRProcessor, VisionEncoderDecoderModel
from PIL import Image

# Загружаем модель
processor = TrOCRProcessor.from_pretrained("microsoft/trocr-base-sroie")
model = VisionEncoderDecoderModel.from_pretrained("microsoft/trocr-base-sroie")

# Открываем кусок изображения
image = Image.open("chunk.png")

# OCR
pixel_values = processor(images=image, return_tensors="pt").pixel_values
generated_ids = model.generate(pixel_values)
text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]

print(text)
