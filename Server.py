from flask import Flask

from sql_practice import add_post, delete_post, update_post, get_posts

app = Flask(__name__)

weather = {
    "astana": -10.3,
    "almaty": -6.7,
    "vienna": -2.5,
}

todos = [
    "Brush teeth",
    "Wash dishes",
    "Buy groceries",
]


@app.route("/")
def welcome():
    return "Это моё первое API"


@app.route("/name")
def second():
    return "моё первое"


@app.route("/city/<city_name>")
def weather_by_city(city_name):
    if city_name in weather:
        return f"Текущая погода в {city_name}: {weather[city_name]}"
    else:
        return f"Город {city_name} не найден", 404


@app.route("/todos")
def todos_list():
    return f"Список задач: {', '.join(todos)}"


@app.route("/todos/new/<title>")
def add_todo(title):
    todos.append(title)
    return f"Задача '{title}' добавлена. Текущий список задач: {', '.join(todos)}", 201


@app.route("/todos/removed/<int:index>")
def remove_todos(index):
    if 0 <= index < len(todos):
        removed_todo = todos.pop(index)
        return (
            f"Задача '{removed_todo}' удалена. Текущий список задач: {', '.join(todos)}",
            200,
        )
    else:
        return f"Задача с индексом {index} не найдена", 404


@app.route("/todos/edit/<int:index>/<new_title>")
def edit_todo(index, new_title):
    if 0 <= index < len(todos):
        todos[index] = new_title
        return (
            f"Задача с индексом {index} обновлена на '{new_title}'. Текущий список задач: {', '.join(todos)}",
            200,
        )
    else:
        return f"Задача с индексом {index} не найдена", 404


@app.route("/posts/add/<post_title>/<post_content>")
def add_new_posts(post_title, post_content):
    result = add_post(post_title, post_content)
    return (f"Пост добавлен: {result}", 201)


@app.route("/posts")
def get_all_posts():
    posts = get_posts()
    return (f"Список постов:{posts}", 200)


@app.route("/posts/delete/<post_id>")
def delete_post_by_id(post_id):
    result = delete_post(post_id)
    return (f"Пост удален: {result}", 200)


@app.route("/posts/update/<post_id>/<new_title>/<new_content>")
def update_post_by_id(post_id, new_title, new_content):
    result = update_post(post_id, new_title, new_content)
    return (f"Пост обновлен: {result}", 200)


if __name__ == "__main__":
    app.run(port=5025, host="0.0.0.0", debug=True)
