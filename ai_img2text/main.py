import logging
from PIL import Image
import pytesseract

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    logger.info("\nstart")
    image_path = "img/image.png"

    try:
        image = Image.open(image_path).convert("RGB")
        text = pytesseract.image_to_string(image, lang="eng")  # можно указать "rus" для русского

    except FileNotFoundError:
        logger.critical(f"no such file {image_path}")
    except Exception as e:
        logger.error(f"Другая ошибка: {e}")
    else:
        print(text)
    finally:
        logger.info("\nend")
