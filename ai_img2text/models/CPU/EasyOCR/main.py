import easyocr
import logging

# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

def run_easyocr_cpu(image_path: str, lang: str = "en") -> str:
    """
    OCR с помощью EasyOCR на CPU.
    :param image_path: путь к изображению
    :param lang: язык (например, 'en', 'ru')
    :return: распознанный текст
    """
    # Указываем use_gpu=False → работа только на CPU
    reader = easyocr.Reader([lang], gpu=False)

    try:
        results = reader.readtext(image_path, detail=0)
        return "\n".join(results)
    except Exception as e:
        # logger.error(f"Ошибка OCR: {e}")
        return ""

if __name__ == "__main__":
    text = run_easyocr_cpu("img/image.png", lang="en")
    print(f'\n{text}')