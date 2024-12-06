import sqlite3
from config import DB_PATH


def add_post(title: str, content: str) -> None:
    add_post_query = """
    INSERT INTO posts(title, content) VALUES (?, ?);
    """

    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute(add_post_query, (title, content))
    connection.commit()
    connection.close()

    print("Пост добавлен")


def get_posts():
    get_posts_query = """
    SELECT * FROM posts;
    """
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute(get_posts_query)
    posts = cursor.fetchall()
    connection.close()

    return posts


def delete_post(post_id: int) -> None:
    delete_post_query = """
    DELETE FROM posts WHERE post_id = ?;
    """

    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute(delete_post_query, (post_id,))
    connection.commit()
    connection.close()

    print(f"Удалено постов: {cursor.rowcount}")


def get_post(post_id: int) -> None:
    get_post_query = """
    SELECT * FROM posts WHERE post_id = ?;
    """
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute(get_post_query, (post_id,))
    post = cursor.fetchone()
    connection.close()

    print(f"Вот пост с id {post_id}: {post}")


get_post(4)


def update_post(post_id: int, new_title: str = None, new_content: str = None) -> None:
    update_post_query = """
    UPDATE posts
    SET title = COALESCE(?, title), content = COALESCE(?, content)
    WHERE post_id = ?;
    """

    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute(
        update_post_query,
        (
            new_title,
            new_content,
            post_id,
        ),
    )
    connection.commit()

    if cursor.rowcount > 0:
        print(f"Пост с id {post_id} успешно обновлен")
    else:
        print(f"Пост с id {post_id} не найден или не были изменены значения")


update_post(4, "успешно обновлен")
