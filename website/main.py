from flask import Flask

# Создаём приложение (сайт)
app = Flask(__name__)

# Меню (один раз пишем, потом вставляем в каждую страницу)
menu_width= str(75)+"px"
menu_padding= str(5)+"px"
# fon_color= "#F5F5F5"
fon_color= "#E8F5E9" # E8F5E9 - класс - не менять !!!!
menu_color= "#3CB371" # 4/10 3CB371
# menu_color= "#00FF7F" # 1/10
# menu_color= "#66CDAA" # 3.5/10
# menu_color= "#2E8B57" # 3/10
# menu_color= "#0EDC12" # 2/10


def set_link(
        text, 
        link,
        # color="black",
        color="#ADFF2F",
        ):
    return f'<p><a href="{link}" style="color:{color}";>{text}</a></p>'

menu = f"""
<div style="float:left; width:{menu_width}; background:{menu_color}; padding:{menu_padding};">
    Site menu:
    {set_link("Main page","http://127.0.0.1:8000/")}
    {set_link("Test page","http://127.0.0.1:8000/test")}
    {set_link("About","http://127.0.0.1:8000/about")}
</div>
"""
# Когда открываешь главную страницу "/", будет выполняться эта функция
@app.route("/")
def home():
    #------------------
    # Как создать HTML5
    #------------------

    # <!DOCTYPE html> # обязательно !!!
    # <html> # начяло html
    # <head> # начяло "заголовок"
    # </head> # конец "заголовок"
    # </html> # конец html
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Main page</title>
    </head>
    <body style="background-color:{fon_color};">
        {menu}
        <h1>My main page.</h1>
        <p> I wants to create somfing unusial</p>
    </body>
    </html>
    """
    # return "Hello world 2"

@app.route("/test")
def home_test():

        # <span>- <a href="http://127.0.0.1:8000/">Main page</a></span>
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Test page</title>
    </head>
    <body style="background-color:{fon_color};">
        {menu}
        <h1>Hello world</h1>
        <p> This page is for testing new ideas.</p>
    </body>
    </html>
"""

@app.route("/about")
def about():
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>About page</title>
    </head>
    <body style="background-color:{fon_color};">
        {menu}
        <h1>Abote</h1>
        <p> Here will be ifnormation:</p>
    </body>
    </html>
"""

# Запускаем сайт
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000)
