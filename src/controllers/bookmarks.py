from models.bookmarks import create_bookmark, get_all_bookmarks, get_bookmark_by_id, delete_bookmark as _delete_bookmark

# Função para adicionar um novo bookmark
def add_bookmark(user_id, school_id):
    create_bookmark(user_id, school_id)
    return f"Bookmark criado com sucesso."

# Função para listar todos os bookmarks
def list_bookmarks(filters=None):
    return get_all_bookmarks(filters)

# Função para buscar bookmark por ID
def get_bookmark(bookmark_id):
    return get_bookmark_by_id(bookmark_id)

# Função para excluir um bookmark
def delete_bookmark(bookmark_id):
    _delete_bookmark(bookmark_id)
    return f"Bookmark {bookmark_id} excluído com sucesso."